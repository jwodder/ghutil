from   importlib        import import_module
from   pathlib          import Path
import re
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

def search_query(*terms):
    q = ''
    for t in terms:
        if ' ' in t and not re.match(r'^(\w+:)?".*"$', t):
            if re.match(r'^\w+:', t):
                t = '{0}:"{2}"'.format(*t.partition(':'))
            else:
                t = '"' + t + '"'
        if q:
            q += ' '
        q += t
    return q
