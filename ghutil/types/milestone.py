from   ghutil.regex import GITHUB, OWNER_REPO_RGX
from   .repo        import Repository
from   .util        import Resource, cacheable

class Milestone(Resource):
    URL_REGEXES = [
        r'(?i){}/{}/milestone/(?P<i_number>\d+)'.format(GITHUB, OWNER_REPO_RGX),
        r'(?i)https?://api\.github\.com/repos/{}/milestones/(?P<i_number>\d+)'
            .format(OWNER_REPO_RGX),
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
        return Repository.params2path(gh, params) + \
            ('milestones', params["number"])

    default_params = None
