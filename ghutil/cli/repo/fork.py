import click
from   ghutil.repos   import GHRepo
from   ghutil.showing import print_json, repo_info

@click.command()
@click.option('-v', '--verbose', is_flag=True)
@click.argument('repo', type=GHRepo())
def cli(repo, verbose):
    """ Fork a repository """
    print_json(repo_info(repo.forks.post(), verbose))
