import platform
import click
import requests
from ghutil import __url__, __version__, types
from ghutil.util import cacheable, search_query
from .endpoint import GHEndpoint
from .util import die

ACCEPT = ",".join(
    [
        "application/vnd.github.mercy-preview",  # Topics
        "application/vnd.github.squirrel-girl-preview",  # Reactions
        "application/vnd.github.symmetra-preview+json",  # Label descriptions
        "application/vnd.github.v3+json",
    ]
)

USER_AGENT = "ghutil/{} ({}) requests/{} {}/{}".format(
    __version__,
    __url__,
    requests.__version__,
    platform.python_implementation(),
    platform.python_version(),
)


class GitHub:
    def __init__(self, session=None):
        self.debug = False
        self.session = session or requests.Session()
        self.session.headers["Accept"] = ACCEPT
        self.session.headers["User-Agent"] = USER_AGENT

    def __getattr__(self, key):
        return self[key]

    def __getitem__(self, name):
        return GHEndpoint(self, name)

    @cacheable
    def me(self):
        return self.user.get()["login"]

    def search(self, objtype, *terms, **params):
        r = self["search"][objtype].get(
            decode=False,
            params=dict(params, q=search_query(*terms)),
        )
        for page in self.paginate(r):
            yield from page["items"]
        ### Return total_count?
        ### Do something on incomplete_results?

    def paginate(self, r):
        while True:
            if not r.ok:
                die(r)
            yield r.json()
            url = r.links.get("next", {}).get("url")
            if url is None:
                break
            r = self[url].get(decode=False)

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

    def parse_team(self, organization, team):
        if team is None:
            return None
        try:
            return int(team)
        except ValueError:
            for t in self.orgs[organization].teams.get():
                if t["name"] == team:
                    return t["id"]
            else:
                raise click.UsageError("Unknown team: " + team)
