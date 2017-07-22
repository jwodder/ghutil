from   importlib        import import_module
from   pathlib          import Path
import click
from   property_manager import cached_property

# As of 2017-05-21, trying to sign up to GitHub with an invalid username gives
# the message "Username may only contain alphanumeric characters or single
# hyphens, and cannot begin or end with a hyphen"
GH_USER_RGX = r'[A-Za-z0-9](?:-?[A-Za-z0-9])*'

# Testing as of 2017-05-21 indicates that repository names can be composed of
# alphanumeric ASCII characters, hyphens, periods, and/or underscores, with the
# names ``.`` and ``..`` being reserved and names ending with ``.git``
# forbidden.
GH_REPO_RGX = r'(?:\.?[-A-Za-z0-9_][-A-Za-z0-9_.]*|\.\.[-A-Za-z0-9_.]+)'\
              r'(?<!\.git)'

OWNER_REPO_RGX = r'(?P<owner>{})/(?P<repo>{})'.format(GH_USER_RGX, GH_REPO_RGX)

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

cacheable = cached_property(writable=True)
