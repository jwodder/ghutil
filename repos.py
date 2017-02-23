#!/usr/bin/python3
import json
from   ghutil import paginate

### Also show html_url?
print(json.dumps([{"name": repo["name"], "ssh_url": repo["ssh_url"]}
                  for repo in paginate('https://api.github.com/user/repos')],
                 sort_keys=True, indent=4))
