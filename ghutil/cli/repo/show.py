import click
from   ghutil.types   import Repository
from   ghutil.showing import print_json

@click.command()
@click.option('-v', '--verbose', is_flag=True)
@Repository.argument_list('repos')
def cli(repos, verbose):
    """ Show repository details """
    print_json(repos, verbose)
