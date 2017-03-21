import click
import requests
from   ..api import show_response

@click.command('new')
@click.option('-d', '--description')
@click.option('-H', '--homepage')
@click.option('-P', '--private', is_flag=True)
@click.argument('name')
def cli(description, homepage, private, name):
    """ Create a new GitHub repository """
    data = {
        "name": name,
        "private": private,
    }
    if description is not None:
        data["description"] = description
    if homepage is not None:
        data["homepage"] = homepage
    show_response(requests.post('https://api.github.com/user/repos', json=data))
