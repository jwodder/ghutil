import os.path
import click
from   ghutil.showing import print_json, gist_info

@click.command()
@click.option('-d', '--description')
@click.option('-f', '--filename')
@click.option('-P', '--private', is_flag=True)
@click.option('-v', '--verbose', is_flag=True)
@click.argument('file', type=click.Path(exists=True, dir_okay=False, readable=True, allow_dash=False))
@click.pass_obj
def cli(gh, description, private, filename, file, verbose):
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
    print_json(gist_info(gh.gists.post(json=data), verbose))
