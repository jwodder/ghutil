from ghutil.regex import API_REPO_RGX, WEB_REPO_RGX
from .repo import Repository
from .util import Resource, cacheable


class Milestone(Resource):
    URL_REGEXES = [
        WEB_REPO_RGX + r"/milestone/(?P<i_number>\d+)/?",
        API_REPO_RGX + r"/milestones/(?P<i_number>\d+)",
    ]

    ARGUMENT_REGEXES = [
        ### ???
    ]

    DISPLAY_FIELDS = [
        "closed_at",
        "closed_issues",
        "created_at",
        ("creator", "login"),
        "description",
        "due_on",
        "html_url",
        "id",
        "number",
        "open_issues",
        "state",
        "title",
        "updated_at",
        "url",
    ]

    @cacheable
    def owner(self):
        return self.parse_url(self.data["url"])["owner"]

    @cacheable
    def repo(self):
        return self.parse_url(self.data["url"])["repo"]

    @cacheable
    def number(self):
        return self.data["number"]

    def __str__(self):
        return self.data["title"]

    def __int__(self):
        return self.number

    @classmethod
    def params2path(cls, gh, params):
        if params.get("repo") is None:
            params.update(Repository.default_params())
        return Repository.params2path(gh, params) + ("milestones", params["number"])

    default_params = None
