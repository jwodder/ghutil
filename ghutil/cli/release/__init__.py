import click
from   ghutil.util import default_command, package_group

@package_group(__package__, __file__, invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """
    Manage releases.

    GitHub releases may be specified on the command line using any of the
    following formats:

    \b
        $OWNER/$REPO:$TAG
        $REPO:$TAG
        $TAG            # for releases of the locally-closed repository
        $OWNER/$REPO:   # for the repository's latest release
        $REPO:          # for the repository's latest release
        https://github.com/$OWNER/$REPO/releases/latest
        https://github.com/$OWNER/$REPO/releases/$TAG
        https://github.com/$OWNER/$REPO/releases/tag/$TAG
        https://api.github.com/repos/$OWNER/$REPO/releases/latest
        https://api.github.com/repos/$OWNER/$REPO/releases/$ID
        https://api.github.com/repos/$OWNER/$REPO/releases/tags/$TAG
    """
    default_command(ctx, 'list')
