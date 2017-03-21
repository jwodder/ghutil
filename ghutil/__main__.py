from   importlib import import_module
import os
from   os.path   import abspath, dirname, join
import click

# Derived from <https://github.com/pallets/click/blob/master/examples/complex/complex/cli.py>

cmd_folder = abspath(join(dirname(__file__), 'commands'))

class ComplexCLI(click.MultiCommand):
    def list_commands(self, ctx):
        return sorted(
            fname[:-3].replace('_', '-')
            for fname in os.listdir(cmd_folder)
            if  fname.endswith('.py') and fname != '__init__.py'
        )

    def get_command(self, ctx, name):
        try:
            mod = import_module(
                '.commands.' + name.replace('-', '_'),
                __package__,
            )
        except ImportError:
            return
        return mod.cli


@click.command(
    cls=ComplexCLI,
    context_settings={"help_option_names": ["-h", "--help"]},
)
def cli():
    pass

if __name__ == '__main__':
    cli()
