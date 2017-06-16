from   itertools import chain
import platform
import re
import attr
import click
import requests
from   .         import __url__, __version__
from   .repos    import get_remote_url, parse_repo_spec
from   .showing  import print_json

ENDPOINT = 'https://api.github.com'

USER_AGENT = 'ghutil/{} ({}) requests/{} {}/{}'.format(
    __version__,
    __url__,
    requests.__version__,
    platform.python_implementation(),
    platform.python_version(),
)

class GitHub:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers["User-Agent"] = USER_AGENT
        self._me = None

    def __getattr__(self, key):
        return self[key]

    def __getitem__(self, name):
        return GHResource(self.session, ENDPOINT, name)

    def repository(self, url=None):
        if url is None:
            url = get_remote_url()
        owner, repo = parse_repo_spec(url)
        if owner is None:
            owner = self.me
        return self.repos[owner][repo]

    def search(self, objtype, *terms, **params):
        q = ''
        for t in terms:
            if ' ' in t:
                ### TODO: Don't add quotes when they're already there
                if re.match(r'^\w+:', t):
                    t = '{0}:"{2}"'.format(*t.partition(':'))
                else:
                    t = '"' + t + '"'
            if q:
                q += ' '
            q += t
        r = self.session.get(
            ENDPOINT + '/search/' + objtype,
            params=dict(params, q=q),
        )
        for page in paginate(self.session, r):
            yield from page["items"]
        ### Return total_count?
        ### Do something on incomplete_results?

    @property
    def me(self):
        if self._me is None:
            self._me = self.user.get()["login"]
        return self._me


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
            if str(self.name).lower().startswith(('http://', 'https://')):
                url = self.name
            else:
                url = self.url.rstrip('/') + '/' + str(self.name).lstrip('/')
        return type(self)(self.session, url, name)

    def __call__(self, decode=True, maybe=False, **kwargs):
        # Use self.name as HTTP method (case insensitive); this allows for
        # supporting URLs ending in, say, `/get` (e.g., because someone named
        # their repository that)
        r = self.session.request(self.name, self.url, **kwargs)
        if self.name.lower() == 'get' and 'next' in r.links:
            return chain.from_iterable(paginate(self.session, r))
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
    try:
        resp = r.json()
    except ValueError:
        click.echo(r.text, err=True)
    else:
        ### Format based on <https://developer.github.com/v3/#client-errors>?
        print_json(resp, err=True)
    click.get_current_context().exit(1)
