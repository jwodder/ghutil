from   importlib        import import_module
from   pathlib          import Path
import click
from   property_manager import cached_property

def package_group(package, filepath, **kwargs):
    def wrapper(f):
        cli = click.group(**kwargs)(f)
        for fpath in Path(filepath).parent.iterdir():
            modname = fpath.stem
            if modname.isidentifier() and not modname.startswith('_') and \
                    (fpath.suffix == '' and (fpath / '__init__.py').exists()
                        or fpath.suffix == '.py'):
                submod = import_module('.' + modname, package)
                cli.add_command(submod.cli, modname.replace('_', '-'))
        return cli
    return wrapper

def default_command(ctx, cmdname):
    if ctx.invoked_subcommand is None:
        ctx.invoke(ctx.command.commands[cmdname])

cacheable = cached_property(writable=True)
