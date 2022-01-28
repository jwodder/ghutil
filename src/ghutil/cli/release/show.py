import click
from ghutil.showing import print_json
from ghutil.types import Release


@click.command()
@click.option("-v", "--verbose", is_flag=True, help="Show full response body")
@Release.argument_list("releases")
def cli(releases, verbose):
    """Show release details"""
    print_json(releases, verbose)
