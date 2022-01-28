import click
from ghutil.types import Issue


@click.command()
@Issue.argument("issue")
@click.argument("file", type=click.File(), required=False)
def cli(issue, file):
    """
    Comment on an issue/PR.

    If a file is given on the command line, its contents will be used as the
    comment body.  Otherwise, an editor will be opened for you to type your
    comment.
    """
    if file is None:
        body = click.edit()
        if body is None:
            click.echo("No text entered; exiting")
    else:
        body = file.read()
    issue.comments.post(json={"body": body})
