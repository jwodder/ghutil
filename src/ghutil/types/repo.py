import re
import click
from   ghutil       import git  # Import module to keep mocking easy
from   ghutil.regex import API_REPO_RGX, GH_REPO_RGX, GH_USER_RGX, \
                            OWNER_REPO_RGX, WEB_REPO_RGX
from   .util        import Resource, cacheable

class Repository(Resource):
    """
    Command-line repository arguments must have one of the following forms:

    - A URL pointing to a GitHub repository (either the web interface, a ``git
      clone`` URL, or an API URL)

    - A string of the form ``owner/repo``

    - A local path (beginning with ``/``, ``./``, or ``../``) pointing to a
      local clone of a GitHub repository

    - A bare repository name (not containing any slashes); the repository's
      owner will be taken to be the current user
    """

    URL_REGEXES = [
        WEB_REPO_RGX + r'(?:\.git)?/?',
        API_REPO_RGX,
        r'git(?:://github\.com/|@github\.com:){}(?:\.git)?/?'
            .format(OWNER_REPO_RGX),
    ]

    ARGUMENT_REGEXES = [
        r'(?:(?P<owner>{})/)?(?P<repo>{})'.format(GH_USER_RGX, GH_REPO_RGX),
    ]

    DISPLAY_FIELDS = [
        ("owner", "login"),
        "name",
        "url",
        "html_url",
        "clone_url",
        "git_url",
        "ssh_url",
        "full_name",
        "description",
        "homepage",
        "private",
        "default_branch",
        "created_at",
        "updated_at",
        "pushed_at",
        "fork",
        "forks_count",
        "size",
        "subscribers_count",
        "stargazers_count",
        "id",
        "language",
        "network_count",
        "open_issues_count",
        ("parent", "full_name"),
        ("source", "full_name"),
        "topics",
        ("license", "spdx_id"),
        "archived",
    ]

    @cacheable
    def owner(self):
        return self.data["owner"]["login"]

    @cacheable
    def repo(self):
        return self.data["name"]

    def __str__(self):
        #return '{0.owner}/{0.repo}'.format(self)
        return self.data["full_name"]

    @classmethod
    def params2path(cls, gh, params):
        if params.get("owner") is None:
            params["owner"] = gh.me
        return ('repos', params["owner"], params["repo"])

    @classmethod
    def default_params(cls):
        remote = git.get_remote_url()
        try:
            return cls.parse_url(remote)
        except ValueError:
            raise click.UsageError("Not a GitHub remote: " + remote)

    @classmethod
    def parse_arg(cls, arg):
        if arg.startswith('/') or re.match(r'^\.\.?(/|$)', arg):
            # Filepath pointing to a local repository
            remote = git.get_remote_url(chdir=arg)
            try:
                return cls.parse_url(remote)
            except ValueError:
                raise click.UsageError("Not a GitHub remote: " + remote)
        else:
            return super().parse_arg(arg)

    def milestone(self, arg):
        from .milestone import Milestone
        try:
            ms = Milestone.from_url(self._gh, arg)
        except ValueError:
            for ms in self._milestones:
                if ms["title"] == arg:
                    return Milestone.from_data(self._gh, ms)
            else:
                raise click.UsageError("Unknown milestone: " + arg)
        else:
            if self != {"owner": ms.owner, "repo": ms.repo}:
                raise click.UsageError('Milestone belongs to different'
                                       ' repository: ' + arg)
            return ms

    @cacheable
    def _milestones(self):
        return list(self.milestones.get(params={"state": "all"}))

    def same_network(self, other):
        self_src = self.data.get("source", self.data)["id"]
        other_src = other.data.get("source", other.data)["id"]
        return self_src == other_src
