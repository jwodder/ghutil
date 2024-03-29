import click
from ghutil.regex import (
    API_REPO_RGX,
    GH_REPO_RGX,
    GH_USER_RGX,
    GIT_REFNAME_RGX,
    WEB_REPO_RGX,
)
from .asset import Asset
from .repo import Repository
from .util import Resource, cacheable


class Release(Resource):
    URL_REGEXES = [
        # https://github.com/:owner/:repo/releases/latest is always a redirect
        # to the latest release, even when there exists another release named
        # "latest".
        #
        # Note that tags that have not been made into releases still have the
        # same web URLs as they would if they were releases.
        r"{}/releases/(?:latest|(?:tag/)?(?P<tag_name>{}))/?".format(
            WEB_REPO_RGX, GIT_REFNAME_RGX
        ),
        r"{}/releases/(?:(?P<i_id>\d+)|latest|tags/(?P<tag_name>{}))".format(
            API_REPO_RGX, GIT_REFNAME_RGX
        ),
    ]

    ARGUMENT_REGEXES = [
        "latest|latest(?P<owner>)(?P<repo>)(?P<tag_name>)",
        # The second branch will never match, so we put the named capture
        # groups there in order to have them be explicitly set to `None` in
        # the resulting params
        r"(?:(?:(?:(?P<owner>{})/)?(?P<repo>{}))?:)?(?P<tag_name>{})".format(
            GH_USER_RGX, GH_REPO_RGX, GIT_REFNAME_RGX
        ),
        r"(?:(?P<owner>{})/)?(?P<repo>{}):".format(GH_USER_RGX, GH_REPO_RGX),
    ]

    DISPLAY_FIELDS = [
        "id",
        "name",
        "tag_name",
        ("author", "login"),
        "prerelease",
        "published_at",
        "created_at",
        "draft",
        "target_commitish",
        "html_url",
        "url",
        "tarball_url",
        "zipball_url",
        ("assets", Asset.DISPLAY_FIELDS),
        "body",
        "body_text",
        "body_html",
    ]

    @cacheable
    def owner(self):
        return self.parse_url(self.data["url"])["owner"]

    @cacheable
    def repo(self):
        return self.parse_url(self.data["url"])["repo"]

    @cacheable
    def id(self):
        return self.data["id"]

    @cacheable
    def tag_name(self):
        return self.data["tag_name"]

    def __str__(self):
        # return f'{self.owner}/{self.repo}:{self.tag_name}'
        return "{0[owner]}/{0[repo]}:{1}".format(
            self.parse_url(self.data["url"]),
            self.data["tag_name"],
        )

    @classmethod
    def params2path(cls, gh, params):
        if params.get("repo") is None:
            params.update(Repository.default_params())
        path = Repository.params2path(gh, params) + ("releases",)
        if params.get("id") is not None:
            path += (params["id"],)
        elif params.get("tag_name") is not None:
            path += (
                "tags",
                params["tag_name"],
            )
        else:
            path += ("latest",)
        return path

    @classmethod
    def default_params(cls):
        # "id" and "tag_name" default to `None`, thereby referring to the
        # latest tag.
        return Repository.default_params()

    def __getitem__(self, name):
        # The …/releases/latest and …/releases/tags/:tag endpoints are only
        # good for GETting; they cannot be PATCHed or DELETEd, and appending
        # `/assets` to them results in a 404.  Thus, if you want to actually
        # _do_ something with a release, you need to use the …/releases/:id
        # endpoint instead; hence, this overload.
        #
        # NOTE: This will fail horribly if GitHub ever introduces a
        # …/releases/:id/get endpoint.  Hopefully, that will never happen.
        if name.upper() == "GET":
            return super().__getitem__(name)
        else:
            return self._gh.repos[self.owner][self.repo].releases[self.id][name]

    def asset(self, arg):
        ### TODO: Could the list of assets in `.data["assets"]` ever be
        ### truncated, necessitating a request to
        ### /repos/:owner/:repo/releases/:id/assets instead?
        for s in self.data["assets"]:
            if s["name"] == arg:
                return Asset.from_data(self._gh, s)
        else:
            raise click.UsageError("Unknown asset: " + arg)
