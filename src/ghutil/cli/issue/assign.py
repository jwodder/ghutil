import click
from ghutil.types import Issue


@click.command()
@click.option("-d", "--delete", is_flag=True, help="Remove the given assignees")
@click.option("--set", is_flag=True, help="Replace the current assignees")
@Issue.argument("issue")
@click.argument("user", nargs=-1)
@click.pass_context
def cli(ctx, issue, user, delete, set):  # noqa: B002
    """
    Assign an issue/PR.

    By default, any users listed on the command line are added to the issue's
    current assignees.  To instead replace the current assignees, specify the
    `--set` option.  To remove the given users from the issue's assignees,
    specify the `--delete` option.

    Note that specifying `--set` without any users will remove all assignees
    from the issue.
    """
    if delete and set:
        ctx.fail("--delete and --set are mutually exclusive")
    elif set:
        issue.patch(json={"assignees": user})
    elif delete:
        issue.assignees.delete(json={"assignees": user})
    else:
        issue.assignees.post(json={"assignees": user})
