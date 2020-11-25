import click
from   ghutil.showing import print_json
from   ghutil.types   import Gist

@click.command()
@click.option('-v', '--verbose', is_flag=True, help='Show full response body')
@Gist.argument_list('gists')
@click.pass_obj
def cli(gh, gists, verbose):
    """ Show gist details """
    print_json(gists, verbose)
