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
        $OWNER/$REPO/$NUMBER
        $REPO/$NUMBER    # for repositories owned by the current user
        $NUMBER          # for issues of the locally-cloned repository
        https://github.com/$OWNER/$REPO/issues/$NUMBER
        https://api.github.com/repos/$OWNER/$REPO/issues/$NUMBER
    """
    default_command(ctx, 'list')
