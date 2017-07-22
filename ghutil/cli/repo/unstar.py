import click
from   ghutil.types import Repository

@click.command()
@Repository.argument_list('repos')
@click.pass_obj
def cli(gh, repos):
    """ Unstar repositories """
    for r in repos:
        gh.user.starred[r.owner][r.repo].delete()
