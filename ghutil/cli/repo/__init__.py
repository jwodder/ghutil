import click
from   ghutil.util import default_command, package_group

@package_group(__package__, __file__, invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """
    Manage repositories.

    GitHub repositories may be specified on the command line using any of the
    following formats:

    \b
        $OWNER/$REPO
        $REPO                                # when owned by current user
        git@github.com:$OWNER/$REPO.git      # with or without trailing `.git`
        https://github.com/$OWNER/$REPO.git  # with or without trailing `.git`
        https://api.github.com/repos/$OWNER/$REPO
        /path/to/local/clone
        ./path/to/local/clone
        ../path/to/local/clone
    """
    default_command(ctx, 'list')
