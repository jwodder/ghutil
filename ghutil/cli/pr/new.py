import click
from   ghutil         import git  # Import module to keep mocking easy
from   ghutil.edit    import edit_as_mail
from   ghutil.showing import print_json

@click.command()
@click.option('-b', '--body', type=click.File(), help='File containing PR body')
@click.option('-M', '--maintainer-can-modify/--maintainer-no-modify',
              '--can-modify/--no-modify', 'maintainer_can_modify',
              help='Allow maintainers on the base repository to modify the PR')
@click.option('-T', '--title', help='Pull request title')
@click.option('-v', '--verbose', is_flag=True, help='Show full response body')
@click.argument('base')
@click.argument('head', required=False)
@click.pass_obj
def cli(gh, head, base, title, body, maintainer_can_modify, verbose):
    """
    Create a new pull request.

    `gh pr new alice/repo:master bob/repo:patch` creates a pull request in
    alice/repo asking for bob/repo:patch to be merged into master.

    The `:branch` portion of the base or head can be omitted to merge (to) the
    repository's default branch.

    If omitted, the PR head defaults to the current branch of the current
    repository.

    The PR head can be given as just `:branch` to merge the given branch of the
    current repository.

    The PR base can be given as just `:branch` to merge to the given branch of
    the head repository.

    Unless both a pull request title and a file containing a PR body are
    specified on the command line, an editor will be opened for you to provide
    the missing details.
    """
    base_repo, base_branch, head = parse_pr_args(gh, base, head)
    data = {
        "title": title,
        "body": body.read() if body is not None else None,
        "maintainer_can_modify": maintainer_can_modify,
        "base": base_branch,
        "head": head,
    }
    if title is None or body is None:
        ### TODO: Also let the user edit the head & base?
        edited = edit_as_mail(data, 'title maintainer_can_modify', 'body')
        if edited is None:
            click.echo('No changes saved; exiting')
            return
        data.update(edited)
        if data["title"] is None:  # or body is None?
            click.echo('Aborting pull request due to empty title')
            return
    print_json(gh.pull_request(base_repo.pulls.post(json=data)), verbose)

def parse_pr_args(gh, base_arg, head_arg):
    if head_arg is None:
        head_repo = gh.repository()
        head_branch = git.get_current_branch()
        if head_branch is None:
            raise click.UsageError('Cannot determine default PR head from'
                                   ' detached HEAD')
    elif head_arg == '':
        raise click.UsageError('PR head cannot be an empty string')
    else:
        head_repo, colon, head_branch = head_arg.partition(':')
        head_repo = gh.repository(head_repo or None)
        if not colon:
            head_branch = head_repo.data["default_branch"]
        elif not head_branch:
            raise click.UsageError('Empty branch name: ' + head_arg)
    base_repo, colon, base_branch = base_arg.partition(':')
    base_repo = gh.repository(base_repo) if base_repo else head_repo
    if not colon:
        base_branch = base_repo.data["default_branch"]
    elif not base_branch:
        raise click.UsageError('Empty branch name: ' + base_arg)
    if base_repo == head_repo:
        head = head_branch
    elif not base_repo.same_network(head_repo):
        raise click.UsageError('Repositories must be in the same network')
    else:
        head = head_repo.data["owner"]["login"] + ':' + head_branch
    return base_repo, base_branch, head
