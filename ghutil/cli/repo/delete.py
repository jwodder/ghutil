import click
from   ghutil.types import Repository

@click.command()
@click.option('-f', '--force', is_flag=True, help='Delete without prompting')
@Repository.argument('repo')
def cli(repo, force):
    """ Delete a repository """
    if force or click.confirm('Delete repository {}?'.format(repo)):
        repo.delete()
        click.echo('Repository {} deleted'.format(repo))
    else:
        click.echo('Repository not deleted')
