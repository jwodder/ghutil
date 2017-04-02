import click
from   ..api     import github_root
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
    print_json(repo_info(github_root().user.repos.post(json=data)))
