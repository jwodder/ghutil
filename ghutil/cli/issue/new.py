import click
from   ghutil.edit    import edit_as_mail
from   ghutil.showing import print_json
from   ghutil.types   import Repository

@click.command()
@click.option('-a', '--assignee', multiple=True, metavar='USER',
              help='Assign the issue to a user.'
                   '  May be specified multiple times.')
@click.option('-b', '--body', type=click.File(),
              help='File containing issue body')
@click.option('-l', '--label', multiple=True, metavar='LABEL',
              help='Add a label to the issue.  May be specified multiple times.')
@click.option('-m', '--milestone', metavar='URL|TITLE',
              help='Associate the issue with a milestone')
@click.option('-T', '--title', help='Issue title')
@click.option('-v', '--verbose', is_flag=True, help='Show full response body')
@Repository.argument('repo')
@click.pass_context
def cli(ctx, repo, title, body, label, assignee, milestone, verbose):
    """
    Create a new issue.

    Unless both an issue title and a file containing an issue body are
    specified on the command line, an editor will be opened for you to provide
    the missing details.

    Note that an issue's assignees, labels, and milestone may only be set by
    users with push access to the repository.
    """
    data = {
        "title": title,
        "body": body.read() if body is not None else None,
        "labels": label,
        "assignees": assignee,
        "milestone": milestone,
    }
    if title is None or body is None:
        if repo.data["permissions"]["push"]:
            fields = 'title labels assignees milestone'
        else:
            fields = 'title'
        edited = edit_as_mail(data, fields, 'body')
        if edited is None:
            click.echo('No changes saved; exiting')
            return
        data.update(edited)
        if data["title"] is None:  # or body is None?
            click.echo('Aborting issue due to empty title')
            return
    if data["milestone"] is not None:
        data["milestone"] = int(repo.milestone(data["milestone"]))
    print_json(ctx.obj.issue(repo.issues.post(json=data)), verbose)
