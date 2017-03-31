from   shlex   import quote
import click
from   ..local import get_github_repo

@click.command('remote')
def cli():
    """ Show repo's remote URLs in sh format """
    owner, repo = get_github_repo()
    for key, value in [
        ('OWNER', owner),
        ('REPO', repo),
        ### Make an API call to get these URLs?
        ('API_URL',   'https://api.github.com/repos/{}/{}'.format(owner, repo)),
        ('HTML_URL',  'https://github.com/{}/{}'.format(owner, repo)),
        ('CLONE_URL', 'https://github.com/{}/{}.git'.format(owner, repo)),
        ('GIT_URL',   'git://github.com/{}/{}.git'.format(owner, repo)),
        ('SSH_URL',   'git@github.com:{}/{}.git'.format(owner, repo)),
    ]: click.echo('{}={}'.format(key, quote(value)))  # noqa
