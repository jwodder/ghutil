from   ghutil.api.util import API_ENDPOINT
from   ghutil.regex    import GH_REPO_RGX, GH_USER_RGX, GITHUB, \
                                GIT_REFNAME_RGX, OWNER_REPO_RGX
from   .repo           import Repository
from   .util           import Resource, cacheable

class Release(Resource):
    URL_REGEXES = [
        # https://github.com/:owner/:repo/releases/latest is always a redirect
        # to the latest release, even when there exists another release named
        # "latest".
        #
        # Note that tags that have not been made into releases still have the
        # same web URLs as they would if they were releases.
        r'(?i){}/{}/releases/(?:latest|(?:tag/)?(?P<tag_name>{}))/?'
            .format(GITHUB, OWNER_REPO_RGX, GIT_REFNAME_RGX),
        r'(?i)https?://api\.github\.com/repos/{}/releases/'
        r'(?:(?P<i_id>\d+)|latest|tags/(?P<tag_name>{}))'
            .format(OWNER_REPO_RGX, GIT_REFNAME_RGX),
    ]

    ARGUMENT_REGEXES = [
        'latest|latest(?P<owner>)(?P<repo>)(?P<tag_name>)',
            # The second branch will never match, so we put the named capture
            # groups there in order to have them be explicitly set to `None` in
            # the resulting params
        r'(?:(?:(?:(?P<owner>{})/)?(?P<repo>{}))?:)?(?P<tag_name>{})'
            .format(GH_USER_RGX, GH_REPO_RGX, GIT_REFNAME_RGX),
        r'(?:(?P<owner>{})/)?(?P<repo>{}):'
            .format(GH_USER_RGX, GH_REPO_RGX, GIT_REFNAME_RGX),
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
        ("assets", (
            "browser_download_url",
            "content_type",
            "created_at",
            "download_count",
            "id",
            "label",
            "name",
            "size",
            "state",
            "updated_at",
            ("uploader", "login"),
            "url",
        )),
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
        return '{0.owner}/{0.repo}:{0.tag_name}'.format(self)

    @classmethod
    def params2path(cls, gh, params):
        if params.get("repo") is None:
            params.update(Repository.default_params())
        path = Repository.params2path(gh, params) + ('releases',)
        if params.get("id") is not None:
            path += (params["id"],)
        elif params.get("tag_name") is not None:
            path += ('tags', params["tag_name"],)
        else:
            path += ('latest',)
        return path

    @classmethod
    def default_params(cls):
        # "id" and "tag_name" default to `None`, thereby referring to the
        # latest tag.
        return Repository.default_params()

    def endpoint(self):
        ### TODO: Confirm that `/tags/*` and `/latest` endpoints can't be used
        ### for anything other than GETting
        ### TODO: Replace this method with `post`, `put`, and `delete`
        ### overloads?
        return self[API_ENDPOINT].repos[self.owner][self.repo].releases[self.id]
