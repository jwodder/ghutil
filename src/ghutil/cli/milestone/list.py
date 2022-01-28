import click
from ghutil.types import Repository


@click.command()
@Repository.option(
    "-R", "--repo", "--repository", "repo", help="Repository to list the milestones of"
)
@click.option(
    "-s",
    "--state",
    type=click.Choice(["open", "closed", "all"]),
    help="Only show milestones in the given state",
)
@click.option(
    "-A",
    "--asc",
    "--ascending",
    "direction",
    flag_value="asc",
    help="Sort in ascending order",
)
@click.option(
    "-D",
    "--desc",
    "--descending",
    "direction",
    flag_value="desc",
    help="Sort in descending order",
)
@click.option(
    "-S",
    "--sort",
    help="What to sort results by",
    type=click.Choice(["completeness", "due_on"]),
)
def cli(repo, **params):
    """List milestones for a repository"""
    for m in repo.milestones.get(params=params):
        click.echo(m["title"])
