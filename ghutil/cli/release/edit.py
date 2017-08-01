import click
from   ghutil.edit  import edit_as_mail
from   ghutil.types import Release

@click.command()
@click.option('--draft/--published', ' /--publish', 'draft', default=None,
              help='Convert release to a draft/published')
@click.option('--prerelease/--full-release', '--pre/--full', 'prerelease',
              default=None, help='Convert release to a prerelease/full release')
@click.option('-b', '--body', type=click.File(),
              help='File containing new release body')
@click.option('-n', '--name', help='Rename release')
@click.option('--tag-name', help='Change Git tag name')
@Release.argument('release')
def cli(release, **opts):
    """
    Edit release details.

    If one or more options are given on the command line, the release is
    modified accordingly.  Otherwise, an editor is started, allowing you to
    modify the release's details as a text file.
    """
    edited = {k:v for k,v in opts.items() if v is not None}
    if not edited:
        edited = edit_as_mail(
            release.data,
            'tag_name name draft prerelease',
            'body',
        )
        if not edited:
            click.echo('No modifications made; exiting')
            return
    elif 'body' in edited:
        edited['body'] = edited['body'].read()
    release.endpoint().patch(json=edited)
