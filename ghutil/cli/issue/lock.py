import click
from   ghutil.types import Issue

@click.command()
@Issue.argument_list('issues')
def cli(issues):
    """ Lock issues """
    for i in issues:
        i.lock.put()
