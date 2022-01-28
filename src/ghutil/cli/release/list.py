import click
from ghutil.types import Repository


@click.command()
@Repository.argument("repo")
@click.pass_obj
def cli(gh, repo):
    """List releases for a repository"""
    for rel in repo.releases.get():
        click.echo(str(gh.release(rel)))
