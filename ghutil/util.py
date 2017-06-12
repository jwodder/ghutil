from   importlib  import import_module
import os
from   os.path    import dirname, exists, join, splitext
from   subprocess import check_output
import click

def package_group(package, filepath, **kwargs):
    def wrapper(f):
        dirpath = dirname(filepath)
        cli = click.group(**kwargs)(f)
        for fname in os.listdir(dirpath):
            modname, ext = splitext(fname)
            if modname.isidentifier() and not modname.startswith('_') and \
                    (ext == '' and exists(join(dirpath, fname, '__init__.py'))
                        or ext == '.py'):
                submod = import_module('.' + modname, package)
                cli.add_command(submod.cli, modname.replace('_', '-'))
        return cli
    return wrapper

def default_command(ctx, cmdname):
    if ctx.invoked_subcommand is None:
        ctx.invoke(ctx.command.commands[cmdname])

def cmdline(*args, **kwargs):
    return check_output(args, universal_newlines=True, **kwargs).strip()
