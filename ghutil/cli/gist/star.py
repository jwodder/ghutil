import click
from   ghutil.gists import GHGist

@click.command()
@click.argument('gists', type=GHGist(), nargs=-1)
@click.pass_obj
def cli(gh, gists):
    """ Star gists """
    for g in gists:
        g.star.put()
