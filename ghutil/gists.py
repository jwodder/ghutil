import re
import click

class GHGist(click.ParamType):
    name = 'gist'

    def convert(self, value, param, ctx):
        for rgx in [
            r'^(\w+)$',
            r'^https?://gist\.github\.com/(\w+)(?:\.git)?$',
            r'^https?://api\.github\.com/gists/(\w+)$',
        ]:
            m = re.match(rgx, value, flags=re.I)
            if m:
                return ctx.obj.gists[m.group(0)]
        self.fail('Invalid GitHub gist: ' + value, param, ctx)
