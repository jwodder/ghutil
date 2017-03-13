import os.path
import click
import requests
from   ..api import show_response

@click.command('gist')
@click.option('-d', '--description')
@click.option('-f', '--filename')
@click.option('-P', '--private', is_flag=True)
@click.argument('file', type=click.Path(exists=True, dir_okay=False, readable=True, allow_dash=False))
def cli(description, private, filename, file):
    """ Convert a file into a gist """
    with open(file) as fp:  ### Use `click.open_file` instead?
        content = fp.read()
    if filename is None:
        filename = os.path.basename(file)
    data = {
        "files": {filename: {"content": content}},
        "public": not private,
    }
    if description is not None:
        data["description"] = description
    # requests uses .netrc automatically
    show_response(requests.post('https://api.github.com/gists', json=data))
