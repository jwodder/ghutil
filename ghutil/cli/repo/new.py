import click
from   ghutil.showing import print_json, repo_info

@click.command()
@click.option('-d', '--description')
@click.option('-H', '--homepage')
@click.option('-P', '--private', is_flag=True)
@click.argument('name')
@click.pass_obj
def cli(gh, description, homepage, private, name):
    """ Create a new repository """
    data = {
        "name": name,
        "private": private,
    }
    if description is not None:
        data["description"] = description
    if homepage is not None:
        data["homepage"] = homepage
    print_json(repo_info(gh.user.repos.post(json=data)))
