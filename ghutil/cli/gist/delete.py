import click
from   ghutil.types import Gist

@click.command()
@click.confirmation_option(prompt='Delete this gist?')
@Gist.argument('gist')
@click.pass_obj
def cli(gh, gist):
    """ Delete a gist """
    gist.delete()
