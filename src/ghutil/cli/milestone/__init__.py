import click
from ghutil.util import default_command, package_group


@package_group(__package__, __file__, invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """
    Manage issue milestones.

    Milestones are specified on the command line by either URL or title.  By
    default, the milestone subcommands only operate on milestones of the
    current repository; to specify a different repository, pass the
    `--repository <REPO>` option to the subcommands.
    """
    default_command(ctx, "list")
