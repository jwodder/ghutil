import click
from   ghutil.showing import print_json
from   ghutil.types   import Repository

@click.command()
@click.option('-v', '--verbose', is_flag=True, help='Show full response body')
@Repository.argument_list('repos')
def cli(repos, verbose):
    """ Show repository details """
    print_json(repos, verbose)
