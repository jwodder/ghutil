import json
import click
from   ..api import paginate

@click.command('gists')
def cli():
    """ List your gists """
    keep = 'id url git_push_url files public'.split()
    click.echo(json.dumps(
        [{k: repo[k] for k in keep}
         for repo in paginate('https://api.github.com/gists')],
        sort_keys=True,
        indent=4,
    ))
