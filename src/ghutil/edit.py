import re
import click
from   headerparser import BOOL, HeaderParser

def edit_as_mail(obj: dict, fields=None, bodyfield=None):
    # Returns only the fields that changed
    # Fields that the user deletes are considered unchanged
    if fields is None:
        fields = sorted(obj.keys())
        if bodyfield is not None:
            fields.remove(bodyfield)
    elif isinstance(fields, str):
        fields = fields.split()
    parser = HeaderParser(body=False if bodyfield is None else None)
    msg = ''
    for f in fields:
        dispname = f.replace('_', '-').title()
        val = obj[f]
        if val is None:
            msg += f'{dispname}: \n'
            parser.add_field(dispname, dest=f)
        elif isinstance(val, bool):
            msg += '{}: {}\n'.format(dispname, 'yes' if val else 'no')
            parser.add_field(dispname, type=BOOL, dest=f)
        elif isinstance(val, str):
            msg += f'{dispname}: {val}\n'
            parser.add_field(dispname, dest=f)
        elif isinstance(val, (list, tuple)):
            msg += '{}: {}\n'.format(dispname, ', '.join(map(str, val)))
            parser.add_field(dispname, type=LIST, dest=f)
        else:
            raise TypeError('only string, boolean, and list fields supported')
    if bodyfield is not None:
        msg += '\n' + (obj[bodyfield] or '')
    msg = click.edit(msg, require_save=True)
    if msg is None:
        return None
    data = parser.parse_string(msg)
    newobj = dict(data)
    if data.body is not None:
        newobj[bodyfield] = data.body
    for k,v in list(newobj.items()):
        if (list(obj[k]) if isinstance(obj[k], tuple) else obj[k]) == v or \
                obj[k] is None and v == '':
            del newobj[k]
    return newobj

def LIST(value):
    if not value or value.isspace():
        return []
    else:
        return list(filter(None, re.split(r'\s*,\s*', value)))
