import click
from   ghutil.edit  import edit_as_mail
from   ghutil.types import Repository
from   ghutil.util  import optional

@click.command()
@Repository.option('-R', '--repo', '--repository', 'repo',
                   help='Repository to which the label belongs')
@optional('-c', '--color', help='New label color (six-character hex code)')
@optional('-d', '--description', help='Set label description')
@optional('-n', '--name', help='Rename label')
@click.argument('label')
def cli(repo, label, **edited):
    """
    Edit a label.

    If one or more options are given on the command line, the label is modified
    accordingly.  Otherwise, an editor is started, allowing you to modify the
    label's details as a text file.
    """
    if not edited:
        edited = edit_as_mail(repo.labels[label].get(), 'name color description')
        if not edited:
            click.echo('No modifications made; exiting')
            return
    if 'color' in edited:
        edited['color'] = edited['color'].lstrip('#')
    repo.labels[label].patch(json=edited)
