from   configparser import ConfigParser, ExtendedInterpolation
from   functools    import partial
import platform
import re
import requests
from   ghutil       import __url__, __version__
from   ghutil       import types
from   ghutil.util  import cacheable, search_query
from   .endpoint    import GHEndpoint
from   .util        import API_ENDPOINT, paginate

ACCEPT = ','.join([
    'application/vnd.github.drax-preview',           # Licenses
    'application/vnd.github.mercy-preview',          # Topics
    'application/vnd.github.squirrel-girl-preview',  # Reactions
    'application/vnd.github.v3+json',
])

USER_AGENT = 'ghutil/{} ({}) requests/{} {}/{}'.format(
    __version__,
    __url__,
    requests.__version__,
    platform.python_implementation(),
    platform.python_version(),
)

class GitHub:
    def __init__(self, session=None):
        self.session = session or requests.Session()
        self.session.headers["Accept"] = ACCEPT
        self.session.headers["User-Agent"] = USER_AGENT

    def configure(self, cfg_file):
        parser = ConfigParser(interpolation=ExtendedInterpolation())
        parser.read(cfg_file)
        try:
            auth = parser['api.auth']
        except KeyError:
            auth = {}
        if 'token' in auth:
            self.session.headers["Authorization"] = "token " + auth['token']
        elif 'username' in auth and 'password' in auth:
            self.session.auth = (auth['username'], auth['password'])
        ### Do something if only one of (username, password) is set?
        try:
            extra_accept = parser['api']['accept']
        except KeyError:
            pass
        else:
            extra_accept = ','.join(
                filter(
                    None,
                    map(
                        partial(re.sub, r'^[\s,]+|[\s,]+$', ''),
                        extra_accept.splitlines(),
                    )
                )
            )
            if extra_accept:
                if parser.getboolean('api', 'append-accept', fallback=True):
                    self.session.headers["Accept"] += ',' + extra_accept
                else:
                    self.session.headers["Accept"] = extra_accept
            elif not parser.getboolean('api', 'append-accept', fallback=True):
                self.session.headers.pop("Accept", None)

    def __getattr__(self, key):
        return self[key]

    def __getitem__(self, name):
        return GHEndpoint(self.session, name)

    @cacheable
    def me(self):
        return self.user.get()["login"]

    def search(self, objtype, *terms, **params):
        r = self.session.get(
            API_ENDPOINT + '/search/' + objtype,
            params=dict(params, q=search_query(*terms)),
        )
        for page in paginate(self.session, r):
            yield from page["items"]
        ### Return total_count?
        ### Do something on incomplete_results?

    def repository(self, obj=None):
        if obj is None:
            return types.Repository.default(self)
        elif isinstance(obj, str):
            return types.Repository.from_arg(self, obj)
        else:
            return types.Repository.from_data(self, obj)

    def issue(self, obj):
        if isinstance(obj, str):
            return types.Issue.from_arg(self, obj)
        else:
            return types.Issue.from_data(self, obj)

    def pull_request(self, obj):
        if isinstance(obj, str):
            return types.PullRequest.from_arg(self, obj)
        else:
            return types.PullRequest.from_data(self, obj)

    def gist(self, obj=None):
        if obj is None:
            return types.Gist.default(self)
        elif isinstance(obj, str):
            return types.Gist.from_arg(self, obj)
        else:
            return types.Gist.from_data(self, obj)

    def release(self, obj=None):
        if obj is None:
            return types.Release.default(self)
        elif isinstance(obj, str):
            return types.Release.from_arg(self, obj)
        else:
            return types.Release.from_data(self, obj)

    def comment(self, obj):
        if isinstance(obj, str):
            return types.Comment.from_arg(self, obj)
        else:
            return types.Comment.from_data(self, obj)
