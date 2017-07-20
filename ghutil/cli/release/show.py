import click
from   ghutil.showing import print_json, release_info

@click.command()
@click.option('-v', '--verbose', is_flag=True)
@click.argument('tags', nargs=-1)
@click.pass_obj
def cli(gh, tags, verbose):
    """ Show release details """
    endpoint = gh.repository().releases.tags
    print_json([release_info(endpoint[t].get(), verbose) for t in tags])
