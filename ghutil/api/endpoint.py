from   itertools import chain
import attr
from   .util     import die, paginate

@attr.s
class GHEndpoint:
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
