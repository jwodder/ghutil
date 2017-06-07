import click
from   ghutil.gists   import GHGist
from   ghutil.showing import print_json, gist_info

@click.command()
@click.argument('gists', type=GHGist(), nargs=-1)
@click.pass_obj
def cli(gh, gists):
    """ Show gist details """
    print_json([gist_info(g.get()) for g in gists])
