import click
from ghutil.showing import print_json
from ghutil.types import Issue


@click.command()
@click.option("-v", "--verbose", is_flag=True, help="Show full response body")
@Issue.argument_list("issues")
def cli(issues, verbose):
    """Show issue details"""
    print_json(issues, verbose)
