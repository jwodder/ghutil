import re
import click
from   ghutil       import git  # Import module to keep mocking easy
from   ghutil.regex import GH_USER_RGX
from   .util        import Resource, cacheable

GIST_ID_RGX = r'(?P<id>[A-Fa-f0-9]+)'

class Gist(Resource):
    URL_REGEXES = [
        r'(?:https?://)?gist\.github\.com/(?:{user}/)?{id}(?:\.git)?/?'
            .format(user=GH_USER_RGX, id=GIST_ID_RGX),
        r'(?:https?://)?api\.github\.com/gists/{}'.format(GIST_ID_RGX),
        r'git@(?:gist\.)?github\.com:{}\.git'.format(GIST_ID_RGX),
    ]

    ARGUMENT_REGEXES = [GIST_ID_RGX]

    DISPLAY_FIELDS = [
        "id",
        "url",
        "git_pull_url",
        ("files", lambda files: {
            fname: {k:v for k,v in about.items() if k != 'content'}
            for fname, about in files.items()
        }),
        "public",
        "html_url",
        ("owner", "login"),
        "description",
        "created_at",
        "updated_at",
        "comments",
        ("fork_of", "id"),
        ("forks", "id"),
    ]

    @cacheable
    def id(self):
        return self.data["id"]

    def __str__(self):
        return self.data["id"]

    @classmethod
    def params2path(cls, gh, params):
        return ('gists', params["id"])

    @classmethod
    def default_params(cls):
        remote = git.get_remote_url()
        try:
            return cls.parse_url(remote)
        except ValueError:
            raise click.UsageError("Not a gist remote: " + remote)

    @classmethod
    def parse_arg(cls, arg):
        if arg.startswith('/') or re.match(r'^\.\.?(/|$)', arg):
            # Filepath pointing to a local repository
            remote = git.get_remote_url(chdir=arg)
            try:
                return cls.parse_url(remote)
            except ValueError:
                raise click.UsageError("Not a gist remote: " + remote)
        else:
            return super().parse_arg(arg)
