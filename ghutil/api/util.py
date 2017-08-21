import sys
import click
from   ghutil.showing import print_json

API_ENDPOINT = 'https://api.github.com'

def paginate(session, r):
    while True:
        if not r.ok:
            die(r)
        yield r.json()
        url = r.links.get('next', {}).get('url')
        if url is None:
            break
        r = session.get(url)

def die(r):
    if 400 <= r.status_code < 500:
        msg = '{0.status_code} Client Error: {0.reason} for url: {0.url}'
    elif 500 <= r.status_code < 600:
        msg = '{0.status_code} Server Error: {0.reason} for url: {0.url}'
    else:
        msg = '{0.status_code} Unknown Error: {0.reason} for url: {0.url}'
    click.echo(msg.format(r), err=True)
    ### Format output based on <https://developer.github.com/v3/#client-errors>?
    echo_response(r, err=True)
    sys.exit(1)

def echo_response(r, err=False):
    try:
        resp = r.json()
    except ValueError:
        click.echo(r.text, err=err)
    else:
        print_json(resp, err=err)
