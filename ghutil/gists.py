import re
import click
from   .repos import GH_USER_RGX

class GHGist(click.ParamType):
    name = 'gist'

    def convert(self, value, param, ctx):
        for rgx in [
            r'^(\w+)$',
            r'^https?://gist\.github\.com/(?:{}/)?(\w+)(?:\.git)?$'
                .format(GH_USER_RGX),
            r'^https?://api\.github\.com/gists/(\w+)$',
            r'^git@gist\.github\.com:(\w+)\.git$',
        ]:
            m = re.match(rgx, value, flags=re.I)
            if m:
                return ctx.obj.gists[m.group(1)]
        self.fail('Invalid GitHub gist: ' + value, param, ctx)
