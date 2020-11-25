from   ghutil.regex import API_REPO_RGX, WEB_REPO_RGX
from   .repo        import Repository
from   .util        import Resource, cacheable

class Comment(Resource):
    URL_REGEXES = [
        WEB_REPO_RGX + r'/(?:issues|pull)/\d+/?#issuecomment-(?P<i_id>\d+)',
        API_REPO_RGX + r'/issues/comments/(?P<i_id>\d+)',
    ]

    ARGUMENT_REGEXES = [
        ### ???
    ]

    DISPLAY_FIELDS = [
        "body",
        "body_text",
        "body_html",
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
