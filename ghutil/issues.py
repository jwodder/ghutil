import re
import click
from   .repos import GH_USER_RGX, GH_REPO_RGX

class GHIssue(click.ParamType):
    name = 'issue'

    def convert(self, value, param, ctx):
        m = re.match(r'^(?:((?:{}/)?{})[/#])?(\d+)$'
                     .format(GH_USER_RGX, GH_REPO_RGX), value)
        if m:
            repo_spec, issid = m.groups()
            return ctx.obj.repository(repo_spec).issues[issid]
        else:
            self.fail('Invalid GitHub issue: ' + value, param, ctx)


class GHPull(click.ParamType):
    name = 'pull request'

    def convert(self, value, param, ctx):
        m = re.match(r'^(?:((?:{}/)?{})[/#])?(\d+)$'
                     .format(GH_USER_RGX, GH_REPO_RGX), value)
        if m:
            repo_spec, issid = m.groups()
            return ctx.obj.repository(repo_spec).pulls[issid]
        else:
            self.fail('Invalid GitHub pull request: ' + value, param, ctx)
