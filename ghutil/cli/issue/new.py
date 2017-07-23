import click
from   ghutil.edit    import edit_as_mail
from   ghutil.showing import print_json
from   ghutil.types   import Repository

@click.command()
@click.option('-a', '--assignee', multiple=True, metavar='USER')
@click.option('-b', '--body', type=click.File())
@click.option('-l', '--label', multiple=True, metavar='LABEL')
@click.option('-m', '--milestone', metavar='ID|TITLE')
@click.option('-T', '--title')
@click.option('-v', '--verbose', is_flag=True)
@Repository.argument('repo')
@click.pass_context
def cli(ctx, repo, title, body, label, assignee, milestone, verbose):
    """ Create a new issue """
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
        data.update(edit_as_mail(data, fields, 'body'))
        if data["title"] is None:  # or body is None?
            click.echo('Aborting issue due to empty title')
            return
    if data["milestone"] is not None:
        try:
            data["milestone"] = int(data["milestone"])
        except ValueError:
            for ms in repo.milestones.get():
                if ms["title"] == data["milestone"]:
                    data["milestone"] = ms["id"]
                    break
            else:
                ctx.fail("Unknown milestone: " + data["milestone"])
    print_json(ctx.obj.issue(repo.issues.post(json=data)), verbose)
