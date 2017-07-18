from   configparser import ConfigParser, ExtendedInterpolation
import os.path
import click
from   ghutil       import __version__
from   ghutil.api   import GitHub
from   ghutil.util  import package_group

@package_group(
    __package__, __file__,
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.option('-c', '--config', type=click.Path(dir_okay=False),
              default=os.path.expanduser('~/.config/ghutil.cfg'))
@click.version_option(__version__, '-V', '--version',
                      message='%(prog)s %(version)s')
@click.pass_context
def cli(ctx, config):
    """ Interact with GitHub from the command line """
    parser = ConfigParser(interpolation=ExtendedInterpolation())
    parser.read(config)
    try:
        auth = parser['api.auth']
    except KeyError:
        auth = {}
    ctx.obj = GitHub(
        username=auth.get('username'),
        password=auth.get('password'),
        token=auth.get('token'),
    )

if __name__ == '__main__':
    cli()
