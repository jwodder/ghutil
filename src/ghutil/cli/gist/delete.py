import click
from ghutil.types import Gist


@click.command()
@click.option("-f", "--force", is_flag=True, help="Delete without prompting")
@Gist.argument("gist")
def cli(gist, force):
    """Delete a gist"""
    data = gist.data
    if force or click.confirm(f'Delete gist {data["html_url"]}?'):
        gist.delete()
        click.echo(f'Gist {data["id"]} deleted')
    else:
        click.echo("Gist not deleted")
