import click
from   ghutil.types import Release

@click.command()
@click.option('-f', '--force', is_flag=True, help='Delete without prompting')
@Release.argument('release', implicit=False)
@click.argument('asset')
def cli(release, asset, force):
    """ Delete a release asset """
    s = release.asset(asset)
    if force or click.confirm(
        'Delete assert {} from release {}?'.format(s, release)
    ):
        s.delete()
        click.echo('Asset {} deleted'.format(s))
    else:
        click.echo('Asset not deleted')
