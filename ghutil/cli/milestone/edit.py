import click
from   ghutil.edit  import edit_as_mail
from   ghutil.types import Repository
from   ghutil.util  import optional

@click.command()
@Repository.option('-R', '--repo', '--repository', 'repo',
                   help='Repository to which the milestone belongs')
@optional('-d', '--description', help='Set milestone description')
@optional('--due-on', '--due', 'due_on', metavar='TIMESTAMP', nilstr=True,
          help='Set milestone due date')
@optional('--open/--closed', ' /--close', help='Open/close the milestone')
@optional('-T', '--title', help='New milestone title')
@click.argument('milestone')
def cli(repo, milestone, **edited):
    """
    Edit a milestone.

    If one or more options are given on the command line, the milestone is
    modified accordingly.  Otherwise, an editor is started, allowing you to
    modify the milestone's details as a text file.

    A milestone's due date can be removed by setting it to the empty string,
    e.g., `--due-on ""`.
    """
    ms = repo.milestone(milestone)
    if not edited:
        data = ms.data.copy()
        data['open'] = data['state'] == 'open'
        edited = edit_as_mail(data, 'title description open due_on')
        if not edited:
            click.echo('No modifications made; exiting')
            return
        if edited.get('due_on') == '':
            edited['due_on'] = None
    if 'open' in edited:
        edited['state'] = 'open' if edited.pop('open') else 'closed'
    ms.patch(json=edited)
