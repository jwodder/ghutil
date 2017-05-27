import click
from   ghutil.repos   import GHRepo, get_remote_url
from   ghutil.showing import print_json

@click.command()
@click.argument('repo', type=GHRepo(), default=get_remote_url)
@click.pass_obj
def cli(gh, repo):
    """ List forkers, stargazers, & watchers """
    print_json({
        "forkers": [f["owner"]["login"] for f in repo.forks.get()],
        "stargazers": [s["login"] for s in repo.stargazers.get()],
        "watchers": [w["login"] for w in repo.subscribers.get()],
    })
