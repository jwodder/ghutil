import os.path
import click
import requests
from   ..api     import show_response
from   ..showing import print_json, gist_info

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
    r = requests.post('https://api.github.com/gists', json=data)
    if r.ok:
        print_json(gist_info(r.json()))
    else:
        show_response(r)
