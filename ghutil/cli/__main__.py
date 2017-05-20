import click
from   ghutil      import __version__
from   ghutil.api  import GitHub
from   ghutil.util import package_group

@package_group(
    __package__, __file__,
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.version_option(__version__, '-V', '--version',
                      message='%(prog)s %(version)s')
@click.pass_context
def cli(ctx):
    """ Interact with GitHub from the command line """
    ctx.obj = GitHub()

if __name__ == '__main__':
    cli()
