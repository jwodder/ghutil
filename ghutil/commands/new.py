import click
import requests
from   ..api     import show_response
from   ..showing import print_json, repo_info

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
    r = requests.post('https://api.github.com/user/repos', json=data)
    if r.ok:
        print_json(repo_info(r.json()))
    else:
        show_response(r)
