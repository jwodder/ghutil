#!/usr/bin/python3
import sys
import requests
from   ghutil import show_response

owner, repo = sys.argv[1:]

# requests uses .netrc automatically
r = requests.post('https://api.github.com/repos/{}/{}/forks'.format(owner,repo))

# TODO: When `r.ok`, only show the "name" & "ssh_url" (and "html_url"?) fields
show_response(r)
