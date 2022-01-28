import webbrowser
import click
from ghutil.types import Release


@click.command()
@Release.argument("release")
def cli(release):
    """Open a release in a web browser"""
    webbrowser.open_new(release.data["html_url"])
