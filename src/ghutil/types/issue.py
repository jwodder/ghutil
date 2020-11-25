from   ghutil.regex import API_REPO_RGX, GH_REPO_RGX, GH_USER_RGX, WEB_REPO_RGX
from   .repo        import Repository
from   .util        import Resource, cacheable

class Issue(Resource):
    """
    Issue & pull request command-line arguments must have one of the following
    forms:

    - A GitHub issue/PR URL (either for the web interface or an API URL)

    - A string of the form ``owner/repo/number`` or ``owner/repo#number``

    - A string of the form ``repo/number`` or ``repo#number``.  The
      repository's owner will be taken to be the current user

    - A bare issue/PR number, in which case the current directory must be a
      clone of a GitHub repository from which the issue's repository's owner &
      name will be taken
    """

    URL_REGEXES = [
        WEB_REPO_RGX + r'/(?:issues|pull)/(?P<i_number>\d+)/?',
        API_REPO_RGX + r'/(?:issues|pulls)/(?P<i_number>\d+)',
    ]

    ARGUMENT_REGEXES = [
        r'(?:(?:(?P<owner>{})/)?(?P<repo>{})[/#:])?(?P<i_number>\d+)'
            .format(GH_USER_RGX, GH_REPO_RGX),
    ]

    DISPLAY_FIELDS = [
        ("assignees", "login"),
        "closed_at",
        ("closed_by", "login"),
        "comments",
        "created_at",
        "html_url",
        "id",
        ("labels", "name"),
        "locked",
        ("milestone", "title"),
        "number",
        "state",
        "title",
        "updated_at",
        "url",
        ("user", "login"),
        ("reactions", lambda react: {
            k:v for k,v in react.items()
                if k not in ('total_count', 'url') and v
        }),
        "body",
        "body_text",
        "body_html",
    ]

    @cacheable
    def owner(self):
        return Repository.parse_url(self.data["repository_url"])["owner"]

    @cacheable
    def repo(self):
        return Repository.parse_url(self.data["repository_url"])["repo"]

    @cacheable
    def number(self):
        return self.data["number"]

    def __str__(self):
        #return '{0.owner}/{0.repo}/{0.number}'.format(self)
        return '{owner}/{repo}/{number}'.format(
            **self.parse_url(self.data["url"])
        )

    @classmethod
    def params2path(cls, gh, params):
        if params.get("repo") is None:
            params.update(Repository.default_params())
        return Repository.params2path(gh, params) + ('issues', params["number"])

    default_params = None


PR_REPO_FIELDS = (
    "label",
    "ref",
    ("repo", "full_name"),
    "sha",
    ("user", "login"),
)

class PullRequest(Issue):
    DISPLAY_FIELDS = [
        ("assignees", "login"),
        ("user", "login"),
        "title",
        "html_url",
        "id",
        "locked",
        "maintainer_can_modify",
        "changed_files",
        "closed_at",
        "comments",
        "commits",
        "additions",
        "deletions",
        "created_at",
        "diff_url",
        "milestone",
        "number",
        "updated_at",
        "url",
        "patch_url",
        "rebaseable",
        "review_comments",
        "state",
        ("base", PR_REPO_FIELDS),
        ("head", PR_REPO_FIELDS),
        "mergeable",
        "mergeable_state",
        "merged",
        "merged_at",
        "merge_commit_sha",
        ("merged_by", "login"),
        ("requested_reviewers", "login"),  ### TODO: Double-check this one
        "body",
        "body_text",
        "body_html",
    ]

    @cacheable
    def owner(self):
        return self.data["base"]["repo"]["owner"]["login"]

    @cacheable
    def repo(self):
        return self.data["base"]["repo"]["name"]

    # number: inherited

    @classmethod
    def params2path(cls, gh, params):
        if params.get("repo") is None:
            params.update(Repository.default_params())
        return Repository.params2path(gh, params) + ('pulls', params["number"])
