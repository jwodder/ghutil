import webbrowser
import click
from   ghutil.types import Repository

@click.command()
@Repository.option('-R', '--repo', '--repository', 'repo',
                   help='Repository to which the milestone belongs')
@click.argument('milestone')
def cli(repo, milestone):
    """ Open a milestone in a web browser """
    webbrowser.open_new(repo.milestone(milestone).data["html_url"])
