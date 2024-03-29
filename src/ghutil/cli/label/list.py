import click
from ghutil.showing import print_json
from ghutil.types import Repository


@click.command()
@Repository.option(
    "-R", "--repo", "--repository", "repo", help="Repository to list the labels of"
)
@click.option("-v", "--verbose", is_flag=True, help="Show full response body")
def cli(repo, verbose):
    """List labels for a repository"""
    labels = repo.labels.get()
    if verbose:
        print_json(labels)
    else:
        for lb in labels:
            click.echo(lb["name"])
