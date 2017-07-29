from   ghutil.regex import OWNER_REPO_RGX
from   .repo        import Repository
from   .util        import Resource, cacheable

class Comment(Resource):
    URL_REGEXES = [
        r'(?i)https?://github\.com/{}/(?:issues|pull)/\d+/?#issuecomment-(?P<i_id>\d+)'
            .format(OWNER_REPO_RGX),
        r'(?i)https?://api\.github\.com/repos/{}/issues/comments/(?P<i_id>\d+)'
            .format(OWNER_REPO_RGX),
    ]

    ARGUMENT_REGEXES = [
        ### ???
    ]

    DISPLAY_FIELDS = [
        "body",
        "created_at",
        "html_url",
        "id",
        ("reactions", lambda react: {
            k:v for k,v in react.items()
                if k not in ('total_count', 'url') and v
        }),
        "url",
        ("user", "login"),
        "updated_at",
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

    ###def __str__(self):
    ###    return ???

    @classmethod
    def params2path(cls, gh, params):
        if params.get("repo") is None:
            params.update(Repository.default_params())
        return Repository.params2path(gh, params) + \
            ('issues', 'comments', params["id"])

    default_params = None
