import re
import click
from   .util import GH_USER_RGX
from   .git  import get_remote_url

class GHGist(click.ParamType):
    name = 'gist'

    def convert(self, value, param, ctx):
        for rgx in [
            r'(\w+)',
            r'https?://gist\.github\.com/(?:{}/)?(\w+)(?:\.git)?'
                .format(GH_USER_RGX),
            r'https?://api\.github\.com/gists/(\w+)',
            r'git@gist\.github\.com:(\w+)\.git',
        ]:
            m = re.fullmatch(rgx, value, flags=re.I)
            if m:
                return ctx.obj.gists[m.group(1)]
        self.fail('Invalid GitHub gist: ' + value, param, ctx)


def gist_arg(cmd=None, implicit=True):
    if implicit:
        dec = click.argument('gist', type=GHGist(), default=get_remote_url)
    else:
        dec = click.argument('gist', type=GHGist())
    if cmd:
        return dec(cmd)
    else:
        return dec

gists_list_arg = click.argument(
    'gists', type=GHGist(), nargs=-1,
    callback=lambda ctx, param, value: value or [param.type.convert(get_remote_url(), param, ctx)],
)
