import attr
import click
import requests
from   .repos   import get_remote_url, parse_github_remote
from   .showing import print_json

ENDPOINT = 'https://api.github.com'

class GitHub:
    def __init__(self):
        self.session = requests.Session()

    def __getattr__(self, key):
        return self[key]

    def __getitem__(self, name):
        return GHResource(self.session, ENDPOINT, name)

    def repository(self, url=None):
        if url is None:
            url = get_remote_url()
        owner, repo = parse_github_remote(url)
        return self.repos[owner][repo]


@attr.s
class GHResource:
    session = attr.ib()
    url     = attr.ib()  # actually the "parent" URL
    name    = attr.ib()

    def __getattr__(self, key):
        return self[key]

    def __getitem__(self, name):
        url = self.url
        if self.name:
            url = self.url.rstrip('/') + '/' + str(self.name)
        return self.__class__(self.session, url, name)

    def __call__(self, decode=True, maybe=False, **kwargs):
        # Use self.name as HTTP method (case insensitive); this allows for
        # supporting URLs ending in, say, `/get` (e.g., because someone named
        # their repository that)
        r = self.session.request(self.name, self.url, **kwargs)
        if self.name.lower() == 'get' and 'next' in r.links:
            return self._paginate(r)
        elif r.ok:
            if decode:
                if r.status_code == 204:
                    return None
                else:
                    return r.json()
            else:
                return r
        elif r.status_code == 404 and maybe:
            return None if decode else r
        else:
            die(r)

    def _paginate(self, r):
        while True:
            if not r.ok:
                die(r)
            yield from r.json()
            url = r.links.get('next', {}).get('url')
            if url is None:
                break
            r = self.session.get(url)


def die(r):
    if 400 <= r.status_code < 500:
        msg = '{0.status_code} Client Error: {0.reason} for url: {0.url}'
    elif 500 <= r.status_code < 600:
        msg = '{0.status_code} Server Error: {0.reason} for url: {0.url}'
    else:
        msg = '{0.status_code} Unknown Error: {0.reason} for url: {0.url}'
    click.echo(msg.format(r), err=True)
    try:
        resp = r.json()
    except ValueError:
        click.echo(r.text, err=True)
    else:
        ### Format based on <https://developer.github.com/v3/#client-errors>?
        print_json(resp, err=True)
    click.get_current_context().exit(1)
