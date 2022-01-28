import webbrowser
import click
from ghutil.types import Gist


@click.command()
@Gist.argument("repo")
def cli(repo):
    """Open a gist in a web browser"""
    webbrowser.open_new(repo.data["html_url"])
