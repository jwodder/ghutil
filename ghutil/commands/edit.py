import click
from   ..edit  import edit_as_mail
from   ..local import get_remote_url
from   ..types import GHRepo

@click.command('edit')
@click.argument('repo', type=GHRepo(), default=get_remote_url)
@click.pass_obj
def cli(gh, repo):
    """ Edit repository details """
    about = repo.get()
    edited = edit_as_mail(about, 'name private description homepage'
                                 ' default_branch has_wiki has_issues'.split())
    if not edited:
        click.echo('No modifications made; exiting')
    else:
        edited.setdefault("name", about["name"])
        repo.patch(json=edited)
