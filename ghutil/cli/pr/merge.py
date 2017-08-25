import click
from   ghutil.showing import print_json
from   ghutil.types   import PullRequest
from   ghutil.util    import optional

@click.command()
@optional('-m', '--message', '--commit-message', 'commit_message',
          help='Extra detail for automatic commit message')
### TODO: Omit merge_method from kwargs when not set by user
@click.option('--merge', 'merge_method', flag_value='merge',
              help='Use the "merge" merge method [default]')
@click.option('--squash', 'merge_method', flag_value='squash',
              help='Use the "squash" merge method')
@click.option('--rebase', 'merge_method', flag_value='rebase',
              help='Use the "rebase" merge method')
@optional('--sha', metavar='HASH', help='SHA hash that PR head must match')
@optional('-T', '--title', '--commit-title', 'commit_title',
          help='Title for automatic commit message')
@PullRequest.argument('pull_request')
def cli(pull_request, **kwargs):
    """ Merge a pull request """
    print_json(pull_request.merge.put(json=kwargs))
