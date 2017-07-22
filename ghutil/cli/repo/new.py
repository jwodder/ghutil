import click
from   ghutil.showing import print_json

@click.command()
@click.option('-d', '--description')
@click.option('-H', '--homepage')
@click.option('-P', '--private', is_flag=True)
@click.option('-v', '--verbose', is_flag=True)
@click.argument('name')
@click.pass_obj
def cli(gh, description, homepage, private, name, verbose):
    """ Create a new repository """
    data = {
        "name": name,
        "private": private,
    }
    if description is not None:
        data["description"] = description
    if homepage is not None:
        data["homepage"] = homepage
    print_json(gh.repository(gh.user.repos.post(json=data)), verbose)
