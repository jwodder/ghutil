from   shlex   import quote
import click
from   ghutil.local import get_remote_url
from   ghutil.types import GHRepo

@click.command()
@click.argument('repo', type=GHRepo(), default=get_remote_url)
def cli(repo):
    """ Show repo's remote URLs in sh format """
    about = repo.get()
    for key, value in [
        ('OWNER',     about["owner"]["login"]),
        ('REPO',      about["name"]),
        ('API_URL',   about["url"]),
        ('HTML_URL',  about["html_url"]),
        ('CLONE_URL', about["clone_url"]),
        ('GIT_URL',   about["git_url"]),
        ('SSH_URL',   about["ssh_url"]),
    ]: click.echo('{}={}'.format(key, quote(value)))  # noqa
