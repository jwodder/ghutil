import sys
import requests
from   ghutil import edit_as_mail, get_github_repo, show_response

if len(sys.argv) == 3:
    owner, repo = sys.argv[1:]
elif len(sys.argv) == 1:
    owner, repo = get_github_repo()
else:
    sys.exit('Usage: {} [<owner> <repo>]'.format(sys.argv[0]))

url = 'https://api.github.com/repos/{}/{}'.format(owner, repo)

s = requests.Session()
r = s.get(url)
if not r.ok:
    show_response(r)
about = r.json()

edited = edit_as_mail(about, 'name private description homepage default_branch has_wiki has_issues'.split())

if not edited:
    print('No modifications made; exiting')
else:
    r = s.patch(url, json=edited)
    if not r.ok:
        show_response(r)
