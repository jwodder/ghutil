import click
from   ghutil.gists   import GHGist
from   ghutil.showing import print_json, gist_info

@click.command()
@click.option('-v', '--verbose', is_flag=True)
@click.argument('gists', type=GHGist(), nargs=-1)
@click.pass_obj
def cli(gh, gists, verbose):
    """ Show gist details """
    print_json([gist_info(g.get(), verbose) for g in gists])
