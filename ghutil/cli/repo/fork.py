import click
from   ghutil.showing import print_json
from   ghutil.types   import Repository

@click.command()
@click.option('-v', '--verbose', is_flag=True)
@Repository.argument('repo', implicit=False)
@click.pass_obj
def cli(gh, repo, verbose):
    """ Fork a repository """
    print_json(gh.repository(repo.forks.post()), verbose)
