import webbrowser
import click
from   ghutil.types import Repository

@click.command()
@Repository.argument('repo')
def cli(repo):
    """ Open a repository in a web browser """
    webbrowser.open_new(repo.data["html_url"])
