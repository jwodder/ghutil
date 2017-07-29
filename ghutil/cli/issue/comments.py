import click
from   ghutil.showing import print_json
from   ghutil.types   import Issue

@click.command()
@click.option('--since', metavar='TIMESTAMP',
              help='Only show comments newer than the given timestamp')
@click.option('-v', '--verbose', is_flag=True, help='Show full response body')
@Issue.argument('issue')
@click.pass_obj
def cli(gh, issue, since, verbose):
    """ Show comments on an issue/PR as JSON"""
    print_json(
        map(gh.comment, issue.comments.get(params={"since": since})),
        verbose,
    )
