import click
from ghutil.types import Repository


@click.command()
@Repository.argument("repo")
@click.argument("topics", nargs=-1)
def cli(repo, topics):
    """Set a repository's topics"""
    repo.topics.put(json={"names": topics})
