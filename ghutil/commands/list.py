import click
from   ..api     import paginate
from   ..showing import print_json, repo_info

@click.command('list')
def cli():
    """ List your GitHub repositories """
    print_json(map(repo_info, paginate('https://api.github.com/user/repos')))
