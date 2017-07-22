import click
from   ghutil.types   import Repository
from   ghutil.showing import print_json

@click.command()
@click.option('-v', '--verbose', is_flag=True)
@Repository.argument('repo', implicit=False)
@click.pass_obj
def cli(gh, repo, verbose):
    """ Fork a repository """
    print_json(gh.repository(repo.forks.post()), verbose)
