import click
from   headerparser import HeaderParser, BOOL

def edit_as_mail(obj: dict, fields=None, bodyfield=None):
    # Returns only the fields that changed
    ### TODO: Allow the user to delete the body (including separating blank
    ### line) to leave it unchanged?
    if fields is None:
        fields = sorted(obj.keys())
    parser = HeaderParser(body=bodyfield is not None)
    msg = ''
    for f in fields:
        dispname = f.replace('_', '-').title()
        val = obj[f]
        if val is None:
            msg += '{}: \n'.format(dispname, val)
            parser.add_field(dispname, dest=f)
        elif isinstance(val, bool):
            msg += '{}: {}\n'.format(dispname, 'yes' if val else 'no')
            parser.add_field(dispname, type=BOOL, dest=f)
        elif isinstance(val, str):
            msg += '{}: {}\n'.format(dispname, val)
            parser.add_field(dispname, dest=f)
        else:
            raise TypeError('only string and boolean fields supported')
    if bodyfield is not None:
        msg += '\n' + obj[bodyfield]
    msg = click.edit(msg)
    if msg is None:
        return {}
    data = parser.parse_string(msg)
    newobj = dict(data)
    if bodyfield is not None:
        newobj[bodyfield] = data.body
    for k,v in list(newobj.items()):
        if obj[k] == v or obj[k] is None and v == '':
            del newobj[k]
    return newobj
