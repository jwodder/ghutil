import click
from   ghutil.types import Repository

@click.command()
@click.confirmation_option(prompt='Delete this repository?')
@Repository.argument('repo')
@click.pass_obj
def cli(gh, repo):
    """ Delete a repository """
    repo.delete()
