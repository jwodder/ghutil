import click
from ghutil.util import default_command, package_group


@package_group(__package__, __file__, invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """
    Manage issue labels.

    Labels are specified on the command line by name.  By default, the label
    subcommands only operate on labels of the current repository; to specify a
    different repository, pass the `--repository <REPO>` option to the
    subcommands.
    """
    default_command(ctx, "list")
