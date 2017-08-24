import click
from   ghutil.showing import print_json
from   ghutil.types   import PullRequest
from   ghutil.util    import optional

@click.command()
@optional('-m', '--message', '--commit-message', 'commit_message',
          help='Extra detail for automatic commit message')
@optional('-M', '--method', '--merge-method',
          help='Merge method to use  [default: merge]',
          type=click.Choice(['merge', 'squash', 'rebase']))
@optional('--sha', metavar='HASH', help='SHA hash that PR head must match')
@optional('-T', '--title', '--commit-title', 'commit_title',
          help='Title for automatic commit message')
@PullRequest.argument('pull_request')
def cli(pull_request, **kwargs):
    """ Merge a pull request """
    print_json(pull_request.merge.put(json=kwargs))
