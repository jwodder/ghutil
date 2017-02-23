#!/usr/bin/python3
import re
import sys
import requests
from   ghutil import show_response

for url in sys.argv[1:]:
    m = re.match(r'^(?:https?://)?(?:www\.)?github\.com'
                 r'/(?P<owner>[^/]+)'
                 r'/(?P<repo>[^/]+)'
                 r'/(?:issues|pull)'
                 r'/(?P<issue>\d+)'
                 r'(?:#issuecomment-(?P<comment>\d+))?$', url)
    if not m:
        print('{}: could not parse {!r}'.format(sys.argv[0], url),
              file=sys.stderr)
        continue
    if m.group('comment') is None:
        target = '/repos/{owner}/{repo}/issues/{issue}/reactions'
    else:
        target = '/repos/{owner}/{repo}/issues/comments/{comment}/reactions'
    # requests uses .netrc automatically
    r = requests.post(
        'https://api.github.com' + target.format(**m.groupdict()),
        headers={"Accept": "application/vnd.github.squirrel-girl-preview"},
        json={"content": "+1"},
    )
    if not r.ok:
        show_response(r)
