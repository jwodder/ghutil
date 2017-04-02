import click
from   ..edit import edit_as_mail

@click.command('edit')
@click.pass_obj
def cli(gh):
    """ Edit repository details """
    repo = gh.repository()
    about = repo.get()
    edited = edit_as_mail(about, 'name private description homepage'
                                 ' default_branch has_wiki has_issues'.split())
    if not edited:
        click.echo('No modifications made; exiting')
    else:
        edited.setdefault("name", about["name"])
        repo.patch(json=edited)
