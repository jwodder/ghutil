import click
from   ghutil.showing import print_json
from   ghutil.types   import PullRequest

@click.command()
@click.option('-v', '--verbose', is_flag=True)
@PullRequest.argument_list('pull_requests')
def cli(pull_requests, verbose):
    """ Show pull request details """
    print_json(pull_requests, verbose)
