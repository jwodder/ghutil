import click
from   ghutil.edit    import edit_as_mail
from   ghutil.showing import print_json

@click.command()
@click.option('-b', '--body', type=click.File())
@click.option('-M', '--maintainer-can-modify', is_flag=True)
@click.option('-T', '--title')
@click.option('-v', '--verbose', is_flag=True)
@click.argument('base')
@click.argument('head')
@click.pass_context
def cli(ctx, head, base, title, body, maintainer_can_modify, verbose):
    """
    Create a new pull request.

    `gh pr new alice/repo:master bob/repo:patch` creates a pull request in
    alice/repo asking bob/repo:patch to be merged into master.
    """

    head_repo, sep, head_branch = head.rpartition(':')
    if not sep:
        ctx.fail('Invalid repo:branch identifier: ' + head)
    head_repo = ctx.obj.repository(head_repo)

    base_repo, sep, base_branch = base.rpartition(':')
    if not sep:
        ctx.fail('Invalid repo:branch identifier: ' + base)
    base_repo = ctx.obj.repository(base_repo)

    data = {
        "title": title,
        "body": body.read() if body is not None else None,
        "maintainer_can_modify": maintainer_can_modify,
        "base": base_branch,
    }
    if title is None or body is None:
        ### TODO: Also let the user edit the head & base?
        data.update(edit_as_mail(data, 'title maintainer_can_modify', 'body'))
        if data["title"] is None:  # or body is None?
            click.echo('Aborting pull request due to empty title')
            return

    if head_repo.data["full_name"] == base_repo.data["full_name"]:
        data["head"] = head_branch
    else:
        ### TODO: Check that the repositories are in the same network?
        data["head"] = head_repo.data["owner"]["login"] + ':' + head_branch

    print_json(ctx.obj.pull_request(base_repo.pulls.post(json=data)), verbose)
