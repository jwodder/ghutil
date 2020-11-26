import click
from   ghutil.types import Release

@click.command()
@click.option('-f', '--force', is_flag=True, help='Delete without prompting')
@Release.argument('release', implicit=False)
@click.argument('asset')
def cli(release, asset, force):
    """ Delete a release asset """
    s = release.asset(asset)
    if force or click.confirm(f'Delete assert {s} from release {release}?'):
        s.delete()
        click.echo(f'Asset {s} deleted')
    else:
        click.echo('Asset not deleted')
