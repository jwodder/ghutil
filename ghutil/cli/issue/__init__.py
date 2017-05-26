import click
from   ghutil.util import package_group, default_command

@package_group(__package__, __file__, invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """
    Manage issues.

    GitHub issues may be specified on the command line using any of the
    following formats:

    \b
        $OWNER/$REPO/$ID
        $REPO/$ID        # for repositories owned by the current user
        $ID              # for issues of the locally-cloned repository
    """
    default_command(ctx, 'list')
