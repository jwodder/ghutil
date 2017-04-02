import click
from   ..showing import print_json, repo_info

@click.command('list')
@click.pass_obj
def cli(gh):
    """ List your GitHub repositories """
    print_json(map(repo_info, gh.user.repos.get()))
