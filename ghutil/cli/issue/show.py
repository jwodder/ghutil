import click
from   ghutil.showing import print_json, issue_info
from   ghutil.issues  import GHIssue

@click.command()
@click.option('-v', '--verbose', is_flag=True)
@click.argument('issues', type=GHIssue(), nargs=-1)
def cli(issues, verbose):
    """ Show issue details """
    print_json([issue_info(i.get(), verbose) for i in issues])
