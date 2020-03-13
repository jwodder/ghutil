from   pathlib       import Path
import click
from   ghutil        import __version__
from   ghutil.api    import GitHub
from   ghutil.config import configure
from   ghutil.util   import package_group

DEFAULT_CFG = str(Path.home() / '.config' / 'ghutil.cfg')

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
@click.option(
    '--debug',
    is_flag      = True,
    callback     = lambda ctx, param, value:
                        setattr(ctx.ensure_object(GitHub), 'debug', value),
    expose_value = False,
    help         = 'Show API requests made',
)
@click.version_option(
    __version__, '-V', '--version', message='%(prog)s %(version)s',
)
def cli():
    """ Interact with GitHub from the command line """
    pass

if __name__ == '__main__':
    cli()
