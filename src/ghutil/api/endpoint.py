from   itertools      import chain
import click
from   requests       import Request
from   ghutil.showing import print_json
from   .util          import API_ENDPOINT, die

class GHEndpoint:
    def __init__(self, gh, *path):
        self._gh = gh
        #: A tuple of the path components of the URL (strings and/or integers).
        #: An absolute URL element will cause all components before it to be
        #: discarded; if there is no absolute URL in `_path`, then
        #: `API_ENDPOINT` will be prepended when making a request.  When a
        #: `GHEndpoint` is called (but not before!), the last element of
        #: `_path` is removed and used as the HTTP method (case insensitive);
        #: this allows using, say, "get" as both a path component (e.g., if
        #: someone named their repository that) and a request method.
        self._path = path

    def __getattr__(self, key):
        return self[key]

    def __getitem__(self, name):
        return GHEndpoint(self._gh, *self._path, name)

    def __call__(self, decode=True, **kwargs):
        *path, method = self._path
        url = API_ENDPOINT
        for p in path:
            p = str(p)
            if p.lower().startswith(('http://', 'https://')):
                url = p
            else:
                url = url.rstrip('/') + '/' + p.lstrip('/')
        req = self._gh.session.prepare_request(Request(method, url, **kwargs))
        if self._gh.debug:
            click.echo('{0.method} {0.url}'.format(req), err=True)
            if 'json' in kwargs:
                print_json(kwargs['json'], err=True)
            elif req.body is not None:
                click.echo(req.body, err=True)
        r = self._gh.session.send(req)
        if not decode:
            return r
        elif not r.ok:
            die(r)
        elif method.lower() == 'get' and 'next' in r.links:
            return chain.from_iterable(self._gh.paginate(r))
        elif r.status_code == 204:
            return None
        else:
            return r.json()
