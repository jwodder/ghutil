import click
import requests
from   ..api     import show_response
from   ..showing import print_json, repo_info

@click.command('fork')
@click.argument('owner')
@click.argument('repo')
def cli(owner, repo):
    """ Fork a GitHub repository """
    r = requests.post(
        'https://api.github.com/repos/{}/{}/forks'.format(owner, repo)
    )
    if r.ok:
        print_json(repo_info(r.json()))
    else:
        show_response(r)
