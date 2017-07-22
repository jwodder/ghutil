import click
from   ghutil.types import Repository

@click.command()
@Repository.argument('repo')
def cli(repo):
    """ List a repository's forks """
    for fork in repo.forks.get():
        click.echo(fork["full_name"])
