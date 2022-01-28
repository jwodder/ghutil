import webbrowser
import click
from ghutil.types import Issue


@click.command()
@Issue.argument("issue")
def cli(issue):
    """Open an issue/PR in a web browser"""
    webbrowser.open_new(issue.data["html_url"])
