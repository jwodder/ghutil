import click
from   ghutil.repos import repo_arg

@click.command()
@repo_arg
def cli(repo):
    """ List a repository's forks """
    for fork in repo.forks.get():
        click.echo(fork["full_name"])
