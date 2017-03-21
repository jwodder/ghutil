import click
import requests
from   ..api import show_response

@click.command('fork')
@click.argument('owner')
@click.argument('repo')
def cli(owner, repo):
    """ Fork a GitHub repository """
    r = requests.post(
        'https://api.github.com/repos/{}/{}/forks'.format(owner, repo)
    )
    # TODO: When `r.ok`, only show the "name" & "ssh_url" (and "html_url"?)
    # fields
    show_response(r)
