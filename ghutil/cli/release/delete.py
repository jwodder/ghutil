import click
from   ghutil.types import Release

@click.command()
@click.option('-f', '--force', is_flag=True, help='Delete without prompting')
@Release.argument('release')
def cli(release, force):
    """ Delete a release """
    release.data  # Force fetching release data before deletion
    if force or click.confirm('Delete release {}?'.format(release)):
        release.endpoint().delete()
        click.echo('Release {} deleted'.format(release))
    else:
        click.echo('Release not deleted')
