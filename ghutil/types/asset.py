from   ghutil.regex import API_REPO_RGX  #, WEB_REPO_RGX
from   .repo        import Repository
from   .util        import Resource, cacheable

class Asset(Resource):
    URL_REGEXES = [
        #WEB_REPO_RGX + ???
        API_REPO_RGX + r'/releases/assets/(?P<i_id>\d+)',
    ]

    ARGUMENT_REGEXES = [
        ### ???
    ]

    DISPLAY_FIELDS = [
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

    def __str__(self):
        return self.data["name"]

    @classmethod
    def params2path(cls, gh, params):
        if params.get("repo") is None:
            params.update(Repository.default_params())
        return Repository.params2path(gh, params) + \
            ('releases', 'assets', params["id"])

    default_params = None
