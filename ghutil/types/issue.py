from   ghutil.showing import show_fields
from   ghutil.util    import GH_USER_RGX, GH_REPO_RGX, OWNER_REPO_RGX
from   .repo          import Repository
from   .util          import Resource, cacheable

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
        r'(?i)https?://github\.com/{}/(?:issues|pull)/(?P<i_number>\d+)'
            .format(OWNER_REPO_RGX),
        r'(?i)https?://api\.github\.com/repos/{}/(?:issues|pulls)/(?P<i_number>\d+)'
            .format(OWNER_REPO_RGX),
    ]

    ARGUMENT_REGEXES = [
        r'(?:(?:(?P<owner>{})/)?(?P<repo>{})[/#])?(?P<i_number>\d+)'
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
        "repository_url",
        ("reactions", lambda react: {
            k:v for k,v in react.items()
                if k not in ('total_count', 'url') and v
        })
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
        return '{0.owner}/{0.repo}/{0.number}'.format(self)

    @classmethod
    def params2path(cls, gh, params):
        if params.get("repo") is None:
            params.update(Repository.default_params())
        return Repository.params2path(gh, params) + ('issues', params["number"])

    default_params = None


show_pr_repo = show_fields(
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
        "issue_url",
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
        ("base", show_pr_repo),
        ("head", show_pr_repo),
        "mergeable",
        "mergeable_state",
        "merged",
        "merged_at",
        "merge_commit_sha",
        ("merged_by", "login"),
        ("requested_reviewers", "login"),  ### TODO: Double-check this one
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
