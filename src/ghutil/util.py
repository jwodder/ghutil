from   importlib        import import_module
from   mimetypes        import guess_type
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

def optional(*decls, nilstr=False, **attrs):
    """
    Like `click.option`, but no value (not even `None`) is passed to the
    command callback if the user doesn't use the option.  If ``nilstr`` is
    true, ``--opt ""`` will be converted to either `None` or (if ``multiple``)
    ``[]``.
    """
    def callback(ctx, param, value):
        if attrs.get('multiple'):
            if nilstr and value == ('',):
                ctx.params[param.name] = []
            elif value != ():
                ctx.params[param.name] = value
        else:
            if nilstr and value == '':
                ctx.params[param.name] = None
            elif value is not None:
                ctx.params[param.name] = value
    if not attrs.get('multiple'):
        attrs['default'] = None
    return click.option(*decls, callback=callback, expose_value=False, **attrs)

def mime_type(filename):
    """
    Like `mimetypes.guess_type()`, except that if the file is compressed, the
    MIME type for the compression is returned
    """
    mtype, encoding = guess_type(filename, False)
    if encoding is None:
        return mtype or 'application/octet-stream'
    elif encoding == 'gzip':
        # application/gzip is defined by RFC 6713
        return 'application/gzip'
        # Note that there is a "+gzip" MIME structured syntax suffix specified
        # in an RFC draft that may one day mean the correct code is:
        #return mtype + '+gzip'
    else:
        return 'application/x-' + encoding
