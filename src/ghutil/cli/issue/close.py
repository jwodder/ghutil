import click
from ghutil.types import Issue


@click.command()
@Issue.argument_list("issues")
def cli(issues):
    """Close issues/PRs"""
    for i in issues:
        i.patch(json={"state": "closed"})
