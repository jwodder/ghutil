import click
from   ghutil.showing import print_json, issue_info
from   ghutil.issues  import GHIssue

@click.command()
@click.argument('issues', type=GHIssue(), nargs=-1)
@click.pass_obj
def cli(gh, issues):
    """ Show issue details """
    print_json([issue_info(i.get()) for i in issues])
