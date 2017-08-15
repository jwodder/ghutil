from   itertools import chain
from   .util     import API_ENDPOINT, die, paginate

class GHEndpoint:
    def __init__(self, session, *path):
        self.__session = session
        #: A tuple of the path components of the URL (strings and/or integers).
        #: An absolute URL element will cause all components before it to be
        #: discarded; if there is no absolute URL in `__path`, then
        #: `API_ENDPOINT` will be prepended when making a request.  When a
        #: `GHEndpoint` is called (but not before!), the last element of
        #: `__path` is removed and used as the HTTP method (case insensitive);
        #: this allows using, say, "get" as both a path component (e.g., if
        #: someone named their repository that) and a request method.
        self.__path = path

    def __getattr__(self, key):
        return self[key]

    def __getitem__(self, name):
        #return GHEndpoint(self.__session, *self.__path, name)  # Python 3.5+
        return GHEndpoint(self.__session, *(self.__path + (name,)))

    def __call__(self, decode=True, **kwargs):
        *path, method = self.__path
        url = API_ENDPOINT
        for p in path:
            p = str(p)
            if p.lower().startswith(('http://', 'https://')):
                url = p
            else:
                url = url.rstrip('/') + '/' + p.lstrip('/')
        r = self.__session.request(method, url, **kwargs)
        if not decode:
            return r
        elif not r.ok:
            die(r)
        elif method.lower() == 'get' and 'next' in r.links:
            return chain.from_iterable(paginate(self.__session, r))
        elif r.status_code == 204:
            return None
        else:
            return r.json()
