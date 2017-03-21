import re
import sys
import click
import requests
from   ..api import show_response

@click.command('plus1')
@click.argument('url', nargs=-1)
def cli(url):
    """ Thumb-up issues, PRs, or comments thereon """
    for u in url:
        m = re.match(r'^(?:https?://)?(?:www\.)?github\.com'
                     r'/(?P<owner>[^/]+)'
                     r'/(?P<repo>[^/]+)'
                     r'/(?:issues|pull)'
                     r'/(?P<issue>\d+)'
                     r'(?:#issuecomment-(?P<comment>\d+))?$', u)
        if not m:
            click.echo('{}: could not parse {!r}'.format(sys.argv[0], u),
                       err=True)
            continue
        if m.group('comment') is None:
            target = '/repos/{owner}/{repo}/issues/{issue}/reactions'
        else:
            target = '/repos/{owner}/{repo}/issues/comments/{comment}/reactions'
        r = requests.post(
            'https://api.github.com' + target.format(**m.groupdict()),
            headers={"Accept": "application/vnd.github.squirrel-girl-preview"},
            json={"content": "+1"},
        )
        if not r.ok:
            show_response(r)
