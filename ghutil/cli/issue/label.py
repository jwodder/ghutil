import click
from   ghutil.types import Issue

@click.command()
@click.option('-d', '--delete', is_flag=True, help='Remove the given labels')
@click.option('--set', is_flag=True, help='Replace the current labels')
@Issue.argument('issue')
@click.argument('label', nargs=-1)
@click.pass_context
def cli(ctx, issue, label, delete, set):  # noqa: B002
    """
    Label an issue/PR.

    By default, any labels listed on the command line are added to the issue's
    current labels.  To instead replace the current labels, specify the `--set`
    option.  To remove the given labels from the issue, specify the `--delete`
    option.

    Note that specifying `--set` without any labels will remove all labels from
    the issue.
    """
    if delete and set:
        ctx.fail('--delete and --set are mutually exclusive')
    elif set:
        issue.labels.put(json=label)
    elif delete:
        for l in label:
            issue.labels[l].delete()
    else:
        issue.labels.post(json=label)
