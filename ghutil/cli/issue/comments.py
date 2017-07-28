import click
from   ghutil.showing import print_json, comment_info
from   ghutil.types   import Issue

@click.command()
@click.option('--since', metavar='TIMESTAMP',
              help='Only show comments newer than the given timestamp')
@click.option('-v', '--verbose', is_flag=True, help='Show full response body')
@Issue.argument('issue')
def cli(issue, since, verbose):
    """ Show comments on an issue/PR as JSON"""
    print_json(
        comment_info(c, verbose)
        for c in issue.comments.get(params={"since": since})
    )
