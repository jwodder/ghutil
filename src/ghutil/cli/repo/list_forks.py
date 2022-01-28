import click
from ghutil.types import Repository


@click.command()
@Repository.argument("repo")
@click.pass_obj
def cli(gh, repo):
    """List a repository's forks"""
    for fork in repo.forks.get():
        click.echo(str(gh.repository(fork)))
