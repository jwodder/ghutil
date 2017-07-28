import os.path
import click
from   ghutil      import __version__
from   ghutil.api  import GitHub
from   ghutil.util import package_group

#DEFAULT_CFG = str(pathlib.Path.home() / '.config' / 'ghutil.cfg')  # Py3.5+
DEFAULT_CFG = os.path.join(os.path.expanduser('~'), '.config', 'ghutil.cfg')

@package_group(
    __package__, __file__,
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.option('-c', '--config', type=click.Path(dir_okay=False),
              default=DEFAULT_CFG, show_default=True,
              help='Use the specified configuration file')
@click.version_option(__version__, '-V', '--version',
                      message='%(prog)s %(version)s')
@click.pass_context
def cli(ctx, config):
    """ Interact with GitHub from the command line """
    if ctx.obj is None:
        # ctx.obj is non-None when mocking with Betamax
        ctx.obj = GitHub()
    ctx.obj.configure(config)

if __name__ == '__main__':
    cli()
