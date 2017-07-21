from   configparser import ConfigParser, ExtendedInterpolation
import platform
import re
import requests
from   ghutil       import __url__, __version__
from   ghutil.repos import get_remote_url, parse_repo_spec
from   .util        import paginate
from   .endpoint    import GHEndpoint

API_ENDPOINT = 'https://api.github.com'

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
        self._me = None

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
        return GHEndpoint(self.session, API_ENDPOINT, name)

    def repository(self, *args):
        if not args:
            args = (None,)
        if len(args) == 1:
            url, = args
            if url is None:
                url = get_remote_url()
            owner, repo = parse_repo_spec(url)
        elif len(args) == 2:
            owner, repo = args
        else:
            raise TypeError('GitHub.repository() takes one or two arguments')
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
            API_ENDPOINT + '/search/' + objtype,
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
