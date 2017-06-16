import click
from   ghutil.repos   import repo_arg
from   ghutil.showing import print_json, repo_info

@click.command()
@click.option('-v', '--verbose', is_flag=True)
@repo_arg(implicit=False)
def cli(repo, verbose):
    """ Fork a repository """
    print_json(repo_info(repo.forks.post(), verbose))
