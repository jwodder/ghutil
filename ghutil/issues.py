import re
import click
from   .repos import GH_USER_RGX, GH_REPO_RGX, get_remote_url, parse_repo_url

class GHIssue(click.ParamType):
    name = 'issue'

    def convert(self, value, param, ctx):
        try:
            owner, repo, num = parse_issue_spec(value)
        except ValueError:
            self.fail('Invalid GitHub issue: ' + value, param, ctx)
        else:
            return ctx.obj.repository(owner, repo).issues[num]


class GHPull(click.ParamType):
    name = 'pull request'

    def convert(self, value, param, ctx):
        try:
            owner, repo, num = parse_issue_spec(value)
        except ValueError:
            self.fail('Invalid GitHub pull request: ' + value, param, ctx)
        else:
            return ctx.obj.repository(owner, repo).pulls[num]


def parse_issue_spec(s):
    """
    Given a GitHub issue or pull request specifier, return a triple containing
    the owner & name of the associated repository and the number of the
    issue/PR.

    Issue specifiers must have one of the following forms:

    - A GitHub issue/PR URL as accepted by `parse_issue_url`

    - A string of the form ``owner/repo/num`` or ``owner/repo#num``

    - A string of the form ``repo/num`` or ``repo#num``.  The repository's
      owner will be set to `None`, indicating that the repository belongs to
      the current user.

    - A bare issue/PR number, in which case the current directory must be a
      clone of a GitHub repository from which the issue's repository's owner &
      name will be taken.
    """
    m = re.match(r'^(?:(?:({user})/)?({repo})[/#])?(\d+)$'
                 .format(user=GH_USER_RGX, repo=GH_REPO_RGX), s, flags=re.I)
    if m:
        user, repo, num = m.groups()
        if not repo:
            user, repo = parse_repo_url(get_remote_url())
        return (user, repo, int(num))
    else:
        return parse_issue_url(s)

def parse_issue_url(s):
    """
    Given a GitHub issue or pull request URL, return a triple containing the
    owner & name of the associated repository and the number of the issue/PR.
    """
    for rgx in [
        r'^https?://github\.com/({user})/({repo})/(?:issues|pull)/(\d+)$',
        r'^https?://api\.github\.com/repos/({user})/({repo})/(?:issues|pulls)/(\d+)$',
    ]:
        m = re.match(rgx.format(user=GH_USER_RGX, repo=GH_REPO_RGX), s,
                     flags=re.I)
        if m:
            user, repo, num = m.groups()
            return (user, repo, int(num))
    raise ValueError(s)
