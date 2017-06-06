import click
from   ghutil.repos import GHRepo, get_remote_url

@click.command()
@click.argument('repo', type=GHRepo(), default=get_remote_url)
def cli(repo):
    """ List a repository's forks """
    for fork in repo.forks.get():
        click.echo(fork["full_name"])
