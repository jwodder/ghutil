import click
from   ghutil.edit  import edit_as_mail
from   ghutil.types import PullRequest
from   ghutil.util  import optional

@click.command()
@optional('--base', metavar='BRANCH', help='Change branch to pull into')
@optional('-b', '--body', type=click.File(), help='File containing new PR body')
@optional('-M', '--maintainer-can-modify/--maintainer-no-modify',
          '--can-modify/--no-modify', 'maintainer_can_modify',
          help='Allow maintainers on the base repository to modify the PR?')
@optional('--open/--closed', ' /--close', help='Open/close the PR')
@optional('-T', '--title', help='New PR title')
@PullRequest.argument('pull_request')
def cli(pull_request, **edited):
    """
    Edit a pull request.

    If one or more options are given on the command line, the pull request is
    modified accordingly.  Otherwise, an editor is started, allowing you to
    modify the pull request's details as a text file.
    """
    if not edited:
        data = pull_request.data.copy()
        data['base'] = data['base']['ref']
        data['open'] = data['state'] == 'open'
        edited = edit_as_mail(
            data,
            'title open base maintainer_can_modify',
            'body',
        )
        if not edited:
            click.echo('No modifications made; exiting')
            return
    elif 'body' in edited:
        edited['body'] = edited['body'].read()
    if 'open' in edited:
        edited['state'] = 'open' if edited.pop('open') else 'closed'
    pull_request.patch(json=edited)
