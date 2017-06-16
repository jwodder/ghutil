import click
from   ghutil.repos import repo_arg

@click.command()
@click.confirmation_option(prompt='Delete this repository?')
@repo_arg
@click.pass_obj
def cli(gh, repo):
    """ Delete a repository """
    repo.delete()
