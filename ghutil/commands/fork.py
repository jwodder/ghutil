import click
from   ..api     import github_root
from   ..showing import print_json, repo_info

@click.command('fork')
@click.argument('owner')
@click.argument('repo')
def cli(owner, repo):
    """ Fork a GitHub repository """
    print_json(repo_info(github_root().repos[owner][repo].forks.post()))
