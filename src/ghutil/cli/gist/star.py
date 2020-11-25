import click
from   ghutil.types import Gist

@click.command()
@Gist.argument_list('gists')
@click.pass_obj
def cli(gh, gists):
    """ Star gists """
    for g in gists:
        g.star.put()
