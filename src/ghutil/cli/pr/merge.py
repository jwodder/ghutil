import click
from   ghutil.showing import print_json
from   ghutil.types   import PullRequest
from   ghutil.util    import optional

@click.command()
@optional('-m', '--message', '--commit-message', 'commit_message',
          help='Extra detail for automatic commit message')
# The API seems to use "merge" as the default method even when merge commits
# are not allowed in the repository, so I'm going to do that, too.
@click.option('--merge', 'merge_method', flag_value='merge', default=True,
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
