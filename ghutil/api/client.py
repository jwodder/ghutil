from   configparser import ConfigParser, ExtendedInterpolation
import platform
import re
import requests
from   ghutil       import __url__, __version__
from   ghutil.types import Gist, Issue, PullRequest, Repository
from   ghutil.util  import cacheable
from   .util        import API_ENDPOINT, paginate
from   .endpoint    import GHEndpoint

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

    def __getattr__(self, key):
        return self[key]

    def __getitem__(self, name):
        return GHEndpoint(self.session, name)

    @cacheable
    def me(self):
        return self.user.get()["login"]

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
            API_ENDPOINT + '/search/' + objtype,
            params=dict(params, q=q),
        )
        for page in paginate(self.session, r):
            yield from page["items"]
        ### Return total_count?
        ### Do something on incomplete_results?

    def repository(self, obj=None):
        if obj is None:
            return Repository.default(self)
        elif isinstance(obj, str):
            return Repository.from_arg(self, obj)
        else:
            return Repository.from_data(self, obj)

    def issue(self, obj):
        if isinstance(obj, str):
            return Issue.from_arg(self, obj)
        else:
            return Issue.from_data(self, obj)

    def pull_request(self, obj):
        if isinstance(obj, str):
            return PullRequest.from_arg(self, obj)
        else:
            return PullRequest.from_data(self, obj)

    def gist(self, obj=None):
        if obj is None:
            return Gist.default(self)
        elif isinstance(obj, str):
            return Gist.from_arg(self, obj)
        else:
            return Gist.from_data(self, obj)
