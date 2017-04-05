import re
import subprocess
import click

class GHRepo(click.ParamType):
    name = 'repository'

    def convert(self, value, param, ctx):
        try:
            return ctx.obj.repository(value)
        except ValueError:
            self.fail('Invalid GitHub URL: ' + value, param, ctx)


def parse_github_remote(url):
    """
    Given a remote URL ``url`` pointing to a GitHub repository or a string of
    the form ``"owner/repo"``, return the repository's owner and name.

    >>> parse_github_remote('git@github.com:jwodder/headerparser.git')
    ('jwodder', 'headerparser')

    >>> parse_github_remote('https://github.com/jwodder/headerparser.git')
    ('jwodder', 'headerparser')

    >>> parse_github_remote('jwodder/headerparser')
    ('jwodder', 'headerparser')
    """
    m = re.match(r'^(?:https://github\.com/|git@github\.com:)?'
                 r'([^/]+)/([^/]+?)(?:\.git)?$', url, flags=re.I)
    if m:
        return m.groups()
    else:
        raise ValueError(url)

def get_remote_url(chdir=None, remote='origin'):
    return subprocess.check_output(
        ['git', 'remote', 'get-url', remote],
        cwd=chdir,
        universal_newlines=True,
    ).strip()
