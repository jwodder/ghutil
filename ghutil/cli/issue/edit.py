from   operator     import itemgetter
import click
from   ghutil.edit  import edit_as_mail
from   ghutil.types import Issue, Repository
from   ghutil.util  import optional

@click.command()
@optional('-a', '--assignee', 'assignees', multiple=True, metavar='USER',
          help='Assign the issue to a user.  May be specified multiple times.',
          nilstr=True)
@optional('-b', '--body', type=click.File(),
          help='File containing new issue body')
@optional('-l', '--label', 'labels', multiple=True, metavar='LABEL',
          help='Set issue label.  May be specified multiple times.',
          nilstr=True)
@optional('-m', '--milestone', metavar='ID|TITLE', nilstr=True,
          help='Associate the issue with a milestone (by ID or name)')
@optional('--open/--closed', ' /--close', help='Open/close the issue')
@optional('-T', '--title', help='New issue title')
@Issue.argument('issue')
@click.pass_obj
def cli(gh, issue, **edited):
    """
    Edit an issue.

    If one or more options are given on the command line, the issue is modified
    accordingly.  Otherwise, an editor is started, allowing you to modify the
    issue's details as a text file.

    Assignees/labels given on the command line will replace the issue's current
    assignees/labels.  To remove all assignees/labels from an issue, supply an
    empty string as the sole assignee/label, e.g., `--assignee ""`.

    An issue's milestone can be removed by setting it to the empty string,
    e.g., `--milestone ""`.

    Note that an issue's assignees, labels, and milestone may only be set by
    users with push access to the repository.
    """
    repo = Repository.from_url(gh, issue.data["repository_url"])
    if not edited:
        if repo.data["permissions"]["push"]:
            fields = 'title labels assignees milestone open'
        else:
            fields = 'title open'
        data = issue.data.copy()
        data['open'] = data['state'] == 'open'
        if data['milestone'] is not None:
            data['milestone'] = data['milestone']['title']
        data["labels"] = list(map(itemgetter("name"), data["labels"]))
        data["assignees"] = list(map(itemgetter("login"), data["assignees"]))
        edited = edit_as_mail(data, fields, 'body')
        if not edited:
            click.echo('No modifications made; exiting')
            return
    elif 'body' in edited:
        edited['body'] = edited['body'].read()
    if 'milestone' in edited:
        if edited['milestone']:
            edited["milestone"] = repo.parse_milestone(edited["milestone"])
        else:
            edited['milestone'] = None
    if 'open' in edited:
        edited['state'] = 'open' if edited.pop('open') else 'closed'
    issue.patch(json=edited)
