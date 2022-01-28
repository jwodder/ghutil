import click
from ghutil.showing import print_json
from ghutil.types import Repository


@click.command()
@Repository.option(
    "-R",
    "--repo",
    "--repository",
    "repo",
    help="Repository to which the milestones belong",
)
@click.option("-v", "--verbose", is_flag=True, help="Show full response body")
@click.argument("milestone", nargs=-1)
def cli(repo, milestone, verbose):
    """Show milestone details"""
    print_json(map(repo.milestone, milestone), verbose)
