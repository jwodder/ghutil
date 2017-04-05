import click
from   ghutil.showing import print_json, repo_info
from   ghutil.repos   import GHRepo

@click.command()
@click.argument('repo', type=GHRepo())
def cli(repo):
    """ Fork a repository """
    print_json(repo_info(repo.forks.post()))
