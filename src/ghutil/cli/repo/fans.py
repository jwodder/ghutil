import click
from ghutil.showing import print_json
from ghutil.types import Repository


@click.command()
@Repository.argument("repo")
def cli(repo):
    """List forkers, stargazers, & watchers"""
    print_json(
        {
            "forkers": [f["owner"]["login"] for f in repo.forks.get()],
            "stargazers": [s["login"] for s in repo.stargazers.get()],
            "watchers": [w["login"] for w in repo.subscribers.get()],
        }
    )
