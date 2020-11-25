import click
from   ghutil.types import Gist

@click.command()
@Gist.argument_list('gists')
@click.pass_obj
def cli(gh, gists):
    """ Unstar gists """
    for g in gists:
        g.star.delete()
