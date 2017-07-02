import click
from   ghutil.gists   import gists_list_arg
from   ghutil.showing import print_json, gist_info

@click.command()
@click.option('-v', '--verbose', is_flag=True)
@gists_list_arg
@click.pass_obj
def cli(gh, gists, verbose):
    """ Show gist details """
    print_json([gist_info(g.get(), verbose) for g in gists])
