import click
from ghutil.util import default_command, package_group


@package_group(__package__, __file__, invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """
    Manage gists.

    Gists may be specified on the command line using any of the following
    formats:

    \b
        $ID
        git@github.com:$ID.git
        git@gist.github.com:$ID.git
        https://gist.github.com/$ID.git        # with or without trailing `.git`
        https://gist.github.com/$OWNER/$ID.git # with or without trailing `.git`
        https://api.github.com/gists/$ID
        /path/to/local/clone
        ./path/to/local/clone
        ../path/to/local/clone
    """
    default_command(ctx, "list")
