import click
from   ghutil.util import default_command, package_group

@package_group(__package__, __file__, invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """
    Manage pull requests

    GitHub pull requests may be specified on the command line using any of the
    following formats:

    \b
        $OWNER/$REPO/$NUMBER
        $REPO/$NUMBER    # for repositories owned by the current user
        $NUMBER          # for PRs of the locally-cloned repository
        https://github.com/$OWNER/$REPO/pull/$NUMBER
        https://api.github.com/repos/$OWNER/$REPO/pulls/$NUMBER
    """
    default_command(ctx, 'list')
