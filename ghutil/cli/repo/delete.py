import click
from   ghutil.types import Repository

@click.command()
@click.option('-f', '--force', is_flag=True, help='Delete without prompting')
@Repository.argument('repo')
@click.pass_obj
def cli(gh, repo, force):
    """ Delete a repository """
    name = repo.data["full_name"]
    if force or click.confirm('Delete repository {}?'.format(name)):
        repo.delete()
        click.echo('Repository {} deleted'.format(name))
    else:
        click.echo('Repository not deleted')
