import click
from   ghutil.gists import GHGist

@click.command()
@click.argument('gists', type=GHGist(), nargs=-1)
@click.pass_obj
def cli(gh, gists):
    """ Unstar gists """
    for g in gists:
        g.star.delete()
