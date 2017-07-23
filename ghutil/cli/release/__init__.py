import click
from   ghutil.util import default_command, package_group

@package_group(__package__, __file__, invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """ Manage releases """
    default_command(ctx, 'list')
