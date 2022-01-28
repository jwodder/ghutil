import click
from ghutil.types import Repository


@click.command()
@Repository.option(
    "-R",
    "--repo",
    "--repository",
    "repo",
    help="Repository to which the milestone belongs",
)
@click.argument("milestone")
def cli(repo, milestone):
    """Open a milestone"""
    repo.milestone(milestone).patch(json={"state": "open"})
