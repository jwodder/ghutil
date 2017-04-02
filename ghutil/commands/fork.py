import click
from   ..showing import print_json, repo_info

@click.command('fork')
@click.argument('owner')
@click.argument('repo')
@click.pass_obj
def cli(gh, owner, repo):
    """ Fork a GitHub repository """
    print_json(repo_info(gh.repos[owner][repo].forks.post()))
