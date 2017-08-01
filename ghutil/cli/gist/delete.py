import click
from   ghutil.types import Gist

@click.command()
@click.option('-f', '--force', is_flag=True, help='Delete without prompting')
@Gist.argument('gist')
@click.pass_obj
def cli(gh, gist, force):
    """ Delete a gist """
    data = gist.data
    if force or click.confirm('Delete gist {0[html_url]}?'.format(data)):
        gist.delete()
        click.echo('Gist {0[id]} deleted'.format(data))
    else:
        click.echo('Gist not deleted')
