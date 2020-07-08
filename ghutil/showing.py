from   collections.abc import Iterator
from   functools       import partial
from   inspect         import signature
import json
from   operator        import itemgetter
from   textwrap        import indent
import click

def print_json(obj, verbose=False, err=False):
    def default(obj):
        if hasattr(obj, 'for_json'):
            if 'verbose' in signature(obj.for_json).parameters:
                return obj.for_json(verbose=verbose)
            else:
                return obj.for_json()
        elif isinstance(obj, Iterator):
            return list(obj)
        else:
            try:
                data = vars(obj).copy()
            except TypeError:
                data = {"__repr__": repr(obj)}
            data["__class__"] = type(obj).__name__
            return data
    def dumps(x):
        return json.dumps(x, sort_keys=True, indent=4, ensure_ascii=False,
                          default=default)
    if isinstance(obj, Iterator):
        first = True
        click.echo('[', nl=False, err=err)
        for o in obj:
            if first:
                click.echo(err=err)
                first = False
            else:
                click.echo(',', err=err)
            click.echo(indent(dumps(o), ' '*4), nl=False, err=err)
        if not first:
            click.echo(err=err)
        click.echo(']', err=err)
    else:
        click.echo(dumps(obj), err=err)

def show_fields(fields, obj):
    about = {}
    for entry in fields:
        if isinstance(entry, str):
            entry = (entry,)
        name, *subpath = entry
        try:
            value = obj[name]
        except KeyError:
            continue
        for sp in subpath:
            if value is None:
                break
            if isinstance(sp, (list, tuple)):
                sp = partial(show_fields, sp)
            elif not callable(sp):
                sp = itemgetter(sp)
            if isinstance(value, list):
                value = [v and sp(v) for v in value]
            else:
                value = sp(value)
        about[name] = value
    return about
