import click
from   ghutil.edit  import edit_as_mail
from   ghutil.types import Release
from   ghutil.util  import optional

@click.command()
@optional('--draft/--published', ' /--publish', 'draft',
          help='Convert release to a draft/published')
@optional('--prerelease/--full-release', '--pre/--full', 'prerelease',
          help='Convert release to a prerelease/full release')
@optional('-b', '--body', type=click.File(),
          help='File containing new release body')
@optional('-n', '--name', help='Rename release')
@optional('--tag-name', help='Change Git tag name')
@Release.argument('release')
def cli(release, **edited):
    """
    Edit release details.

    If one or more options are given on the command line, the release is
    modified accordingly.  Otherwise, an editor is started, allowing you to
    modify the release's details as a text file.
    """
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
    release.patch(json=edited)
