import click
from   ..api     import github_root
from   ..showing import print_json, repo_info

@click.command('list')
def cli():
    """ List your GitHub repositories """
    print_json(map(repo_info, github_root().user.repos.get()))
