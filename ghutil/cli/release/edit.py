import click
from   ghutil.edit  import edit_as_mail
from   ghutil.types import Release

@click.command()
@Release.argument('release')
@click.pass_obj
def cli(gh, release):
    """ Edit a GitHub release """
    edited = edit_as_mail(
        release.data,
        'tag_name name draft prerelease'.split(),
        'body',
    )
    if not edited:
        click.echo('No modifications made; exiting')
    else:
        release.endpoint.patch(json=edited)
