import os.path
import click
from   ghutil        import __version__
from   ghutil.config import configure
from   ghutil.util   import package_group

#DEFAULT_CFG = str(pathlib.Path.home() / '.config' / 'ghutil.cfg')  # Py3.5+
DEFAULT_CFG = os.path.join(os.path.expanduser('~'), '.config', 'ghutil.cfg')

@package_group(
    __package__, __file__,
    name='gh',
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.option(
    '-c', '--config',
    type         = click.Path(dir_okay=False),
    default      = DEFAULT_CFG,
    callback     = lambda ctx, param, value: configure(value, ctx),
    expose_value = False,
    show_default = True,
    help         = 'Use the specified configuration file',
)
@click.version_option(
    __version__, '-V', '--version', message='%(prog)s %(version)s',
)
def cli():
    """ Interact with GitHub from the command line """
    pass

if __name__ == '__main__':
    cli()
