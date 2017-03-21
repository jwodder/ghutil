import json
import click
from   ..api import paginate

@click.command('list')
def cli():
    """ List your GitHub repositories """
    click.echo(json.dumps(
        ### Also show html_url?
        [{"name": repo["name"], "ssh_url": repo["ssh_url"]}
         for repo in paginate('https://api.github.com/user/repos')],
        sort_keys=True,
        indent=4,
    ))
