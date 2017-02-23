#!/usr/bin/python3
import json
from   ghutil import paginate

keep = 'id url git_push_url files public'.split()

print(json.dumps([{k: repo[k] for k in keep}
                  for repo in paginate('https://api.github.com/gists')],
                 sort_keys=True, indent=4))
