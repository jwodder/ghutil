import re
import click
from   .util import cmdline

# As of 2017-05-21, trying to sign up to GitHub with an invalid username gives
# the message "Username may only contain alphanumeric characters or single
# hyphens, and cannot begin or end with a hyphen"
GH_USER_RGX = r'[A-Za-z0-9](?:-?[A-Za-z0-9])*'

# Testing as of 2017-05-21 indicates that repository names can be composed of
# alphanumeric ASCII characters, hyphens, periods, and/or underscores, with the
# names ``.`` and ``..`` being reserved and names ending with ``.git``
# forbidden.
GH_REPO_RGX = r'(?:\.?[-A-Za-z0-9_][-A-Za-z0-9_.]*|\.\.[-A-Za-z0-9_.]+)'\
              r'(?<!\.git)'

class GHRepo(click.ParamType):
    name = 'repository'

    def convert(self, value, param, ctx):
        try:
            return ctx.obj.repository(value)
        except ValueError:
            self.fail('Invalid GitHub URL: ' + value, param, ctx)


def parse_repo_spec(s):
    """
    Given a GitHub repository specifier, return the repository's owner and
    name.  Repository specifiers must have one of the following forms:

    - A remote GitHub URL as accepted by `parse_repo_url`

    - A string of the form ``owner/repo``

    - A local path (beginning with ``/``, ``./``, or ``../``) pointing to a
      local clone of a GitHub repository

    - A bare repository name (not containing any slashes).  The name of the
      owner will be set to `None`; `GitHub.repository` will treat this as a
      repository belonging to the current user.

    >>> parse_repo_spec('git@github.com:jwodder/headerparser.git')
    ('jwodder', 'headerparser')

    >>> parse_repo_spec('https://github.com/jwodder/headerparser.git')
    ('jwodder', 'headerparser')

    >>> parse_repo_spec('https://api.github.com/repos/jwodder/headerparser')
    ('jwodder', 'headerparser')

    >>> parse_repo_spec('jwodder/headerparser')
    ('jwodder', 'headerparser')

    >>> parse_repo_spec('headerparser')
    (None, 'headerparser')
    """
    if s.startswith('/') or re.match(r'^\.\.?(/|$)', s):
        # Filepath pointing to a local repository
        return parse_repo_url(get_remote_url(chdir=s))
    m = re.match('^(?:({})/)?({})$'.format(GH_USER_RGX, GH_REPO_RGX), s)
    if m:
        return m.groups()
    else:
        return parse_repo_url(s)

def parse_repo_url(s):
    """
    Given a remote GitHub repository URL, return the repository's owner and
    name.

    >>> parse_repo_url('git@github.com:jwodder/headerparser.git')
    ('jwodder', 'headerparser')

    >>> parse_repo_url('https://github.com/jwodder/headerparser.git')
    ('jwodder', 'headerparser')

    >>> parse_repo_url('https://api.github.com/repos/jwodder/headerparser')
    ('jwodder', 'headerparser')
    """
    for rgx in [
        r'^(?:https?://github\.com/|git@github\.com:)({})/({})(?:\.git)?$',
        r'^https?://api\.github\.com/repos/({})/({})$',
    ]:
        m = re.match(rgx.format(GH_USER_RGX, GH_REPO_RGX), s, flags=re.I)
        if m:
            return m.groups()
    raise ValueError(s)

def get_remote_url(chdir=None, remote='origin'):
    return cmdline('git', 'remote', 'get-url', remote, cwd=chdir)

def repo_arg(cmd=None, implicit=True):
    if implicit:
        dec = click.argument('repo', type=GHRepo(), default=get_remote_url)
    else:
        dec = click.argument('repo', type=GHRepo())
    if cmd:
        return dec(cmd)
    else:
        return dec

repos_list_arg = click.argument(
    'repos', type=GHRepo(), nargs=-1,
    callback=lambda ctx, param, value: value or [ctx.obj.repository()],
)
