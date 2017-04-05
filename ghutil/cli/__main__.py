import click
from   ghutil.api  import GitHub
from   ghutil.util import package_group

@package_group(
    __package__, __file__,
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.pass_context
def cli(ctx):
    ctx.obj = GitHub()

if __name__ == '__main__':
    cli()
