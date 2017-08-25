import click
from   ghutil.types import Issue

@click.command()
@Issue.argument_list('issues')
def cli(issues):
    """ Unlock issues/PRs """
    for i in issues:
        i.lock.delete()
