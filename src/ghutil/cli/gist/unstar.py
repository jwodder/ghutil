import click
from   ghutil.types import Gist

@click.command()
@Gist.argument_list('gists')
def cli(gists):
    """ Unstar gists """
    for g in gists:
        g.star.delete()
