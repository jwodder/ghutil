import click
from   ghutil.util import package_group

@package_group(__package__, __file__)
@click.pass_context
def cli(ctx):
    """ Manage releases """
    pass
