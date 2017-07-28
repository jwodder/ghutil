import os.path
import click
from   ghutil.showing import print_json

@click.command()
@click.option('-d', '--description', help='Set gist description')
@click.option('-f', '--filename', help='Set name of gist file')
@click.option('-P', '--private', is_flag=True, help='Make gist private')
@click.option('-v', '--verbose', is_flag=True, help='Show full response body')
@click.argument('file', type=click.File(), default='-')
@click.pass_obj
def cli(gh, description, private, filename, file, verbose):
    """
    Convert a file into a gist.

    If no file is specified on the command line, the gist contents will be read
    from standard input.
    """
    content = file.read()
    if filename is None:
        filename = os.path.basename(file.name)
    data = {
        "files": {filename: {"content": content}},
        "public": not private,
    }
    if description is not None:
        data["description"] = description
    print_json(gh.gist(gh.gists.post(json=data)), verbose)
