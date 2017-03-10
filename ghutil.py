import json
import re
import subprocess
import sys
import click
from   headerparser import HeaderParser, BOOL
import requests

def paginate(url):
    s = requests.Session()
    while url is not None:
        r = s.get(url)
        r.raise_for_status()
        yield from r.json()
        url = r.links.get('next', {}).get('url')

def show_response(r):
    if r.ok:
        show_body(r)
    else:
        if 400 <= r.status_code < 500:
            msg = '{0.status_code} Client Error: {0.reason} for url: {0.url}'
        elif 500 <= r.status_code < 600:
            msg = '{0.status_code} Server Error: {0.reason} for url: {0.url}'
        else:
            msg = '{0.status_code} Unknown Error: {0.reason} for url: {0.url}'
        print(msg.format(r), file=sys.stderr)
        show_body(r, file=sys.stderr)
        sys.exit(1)

def show_body(r, out=None):
    if out is None:
        out = sys.stdout
    try:
        resp = r.json()
    except ValueError:
        print(r.text, file=out)
    else:
        print(json.dumps(resp, sort_keys=True, indent=4), file=out)

def parse_github_remote(url):
    """
    Given a remote URL ``url`` pointing to a GitHub repository, return the
    repository's owner and name.

    >>> parse_github_remote('git@github.com:jwodder/headerparser.git')
    ('jwodder', 'headerparser')

    >>> parse_github_remote('https://github.com/jwodder/headerparser.git')
    ('jwodder', 'headerparser')
    """
    m = re.match(r'^(?:https://github\.com/|git@github\.com:)'
                 r'([^/]+)/([^/]+)\.git$', url, flags=re.I)
    if m:
        return m.groups()
    else:
        raise ValueError(url)

def get_github_repo(chdir=None, remote='origin'):
    s = subprocess.check_output(
        ['git', 'remote', 'get-url', remote],
        cwd=chdir,
        universal_newlines=True,
    )
    return parse_github_remote(s.strip())

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
        if isinstance(val, bool):
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
        if obj[k] == v:
            del newobj[k]
    return newobj
