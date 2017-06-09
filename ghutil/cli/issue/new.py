import click
from   ghutil.repos   import GHRepo, get_remote_url
from   ghutil.showing import print_json, issue_info

@click.command()
@click.option('-a', '--assignee', multiple=True, metavar='USER')
@click.option('-b', '--body', type=click.File())
@click.option('-l', '--label', multiple=True, metavar='LABEL')
@click.option('-m', '--milestone', metavar='ID|TITLE')
@click.option('-T', '--title')
@click.option('-v', '--verbose', is_flag=True)
@click.argument('repo', type=GHRepo(), default=get_remote_url)
@click.pass_context
def cli(ctx, repo, title, body, label, assignee, milestone, verbose):
    """ Create a new issue """
    ### TODO: Open editor if title isn't given
    data = {
        "title": title,
        "body": body.read() if body is not None else None,
        "labels": label,
        "assignees": assignee,
    }
    if milestone is not None:
        try:
            data["milestone"] = int(milestone)
        except ValueError:
            for ms in repo.milestones.get():
                if ms["title"] == milestone:
                    data["milestone"] = ms["id"]
                    break
            else:
                ctx.fail("Unknown milestone: " + milestone)
    print_json(issue_info(repo.issues.post(json=data), verbose))
