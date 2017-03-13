import json
import sys
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
