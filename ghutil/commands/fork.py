import click
from   ..showing import print_json, repo_info
from   ..types   import GHRepo

@click.command('fork')
@click.argument('repo', type=GHRepo())
def cli(repo):
    """ Fork a GitHub repository """
    print_json(repo_info(repo.forks.post()))
