import re
from   ghutil.git  import get_remote_url
from   ghutil.util import GH_REPO_RGX, GH_USER_RGX, OWNER_REPO_RGX
from   .util       import Resource, cacheable

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
        r'(?i)(?:https?://github\.com/|git@github\.com:){}(?:\.git)?'
            .format(OWNER_REPO_RGX),
        r'(?i)https?://api\.github\.com/repos/{}'.format(OWNER_REPO_RGX),
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
        "watchers_count",
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
    ]

    @cacheable
    def owner(self):
        return self.data["owner"]["login"]

    @cacheable
    def repo(self):
        return self.data["name"]

    def __str__(self):
        return '{0.owner}/{0.repo}'.format(self)

    @classmethod
    def params2path(cls, gh, params):
        if params.get("owner") is None:
            params["owner"] = gh.me
        return ('repos', params["owner"], params["repo"])

    @classmethod
    def default_params(cls):
        return cls.parse_url(get_remote_url())

    @classmethod
    def parse_arg(cls, arg):  # returns a "params" dict
        if arg.startswith('/') or re.match(r'^\.\.?(/|$)', arg):
            # Filepath pointing to a local repository
            return cls.parse_url(get_remote_url(chdir=arg))
        else:
            return super().parse_arg(arg)
