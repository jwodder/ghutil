import click
from   ghutil.util import package_group, default_command

@package_group(__package__, __file__, invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """ Manage gists """
    default_command(ctx, 'list')
