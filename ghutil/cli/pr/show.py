import click
from   ghutil.showing import print_json, pr_info
from   ghutil.issues  import GHPull

@click.command()
@click.option('-v', '--verbose', is_flag=True)
@click.argument('pull_requests', type=GHPull(), nargs=-1)
def cli(pull_requests, verbose):
    """ Show pull request details """
    print_json([pr_info(p.get(), verbose) for p in pull_requests])
