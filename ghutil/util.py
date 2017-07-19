from   importlib  import import_module
from   pathlib    import Path
from   subprocess import check_output, CalledProcessError
import click

def package_group(package, filepath, **kwargs):
    def wrapper(f):
        dirpath = Path(filepath).parent
        cli = click.group(**kwargs)(f)
        for fpath in dirpath.iterdir():
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

def cmdline(*args, **kwargs):
    try:
        return check_output(args, universal_newlines=True, **kwargs).strip()
    except CalledProcessError as e:
        click.get_current_context().exit(e.returncode)

def get_last_tag(chdir=None):
    return cmdline('git', 'describe', '--abbrev=0', '--tags', cwd=chdir)
