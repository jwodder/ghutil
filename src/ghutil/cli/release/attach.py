import os.path
import click
from   uritemplate    import expand
from   ghutil.showing import print_json
from   ghutil.types   import Asset, Release
from   ghutil.util    import mime_type

@click.command()
@click.option('-T', '--content-type', metavar='MIME',
              help='Set asset MIME type  [default: guessed from file name]')
@click.option('-l', '--label', help='Set a short description for the asset')
@click.option('-n', '--name',
              help='Set asset file name  [default: basename of local file]')
@click.option('-v', '--verbose', is_flag=True, help='Show full response body')
@Release.argument('release', implicit=False)
@click.argument('file', type=click.File('rb'))
@click.pass_obj
def cli(gh, release, file, name, label, content_type, verbose):
    """
    Upload a release asset.

    Note: If ghutil reads your GitHub credentials from ~/.netrc, you will need
    to add a separate entry for uploads.github.com with the same username &
    password as for api.github.com in order to use this command.
    """
    if name is None:
        name = os.path.basename(file.name)
    if content_type is None:
        content_type = mime_type(name)
    url = expand(release.data["upload_url"], name=name, label=label)
    r = gh[url].post(headers={"Content-Type": content_type}, data=file.read())
    print_json(Asset.from_data(gh, r), verbose)
