import os.path
import click
from ghutil.showing import print_json


@click.command()
@click.option("-d", "--description", help="Set gist description")
@click.option(
    "-f",
    "--file",
    "named_files",
    type=(str, click.File()),
    multiple=True,
    help="Specify a file with explicit name",
)
@click.option("-P", "--private", is_flag=True, help="Make gist private")
@click.option("-v", "--verbose", is_flag=True, help="Show full response body")
@click.argument("files", type=click.File(), nargs=-1)
@click.pass_context
def cli(ctx, files, named_files, description, private, verbose):
    """
    Create a gist from one or more files.

    By default, each gist file will be named with the local file's basename.
    To set the name of a gist file explicitly, specify the file on the command
    line as "--file <name> <file-path>" (with no intervening arguments).

    A gist can be created from standard input by specifying "-" as a filename.
    """
    file_dict = {}
    for fp in files:
        file_dict[os.path.basename(fp.name)] = {"content": fp.read()}
    for name, fp in named_files:
        file_dict[name] = {"content": fp.read()}
    if not file_dict:
        ctx.fail("No files specified")
    data = {
        "files": file_dict,
        "public": not private,
    }
    if description is not None:
        data["description"] = description
    print_json(ctx.obj.gist(ctx.obj.gists.post(json=data)), verbose)
