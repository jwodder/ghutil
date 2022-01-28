import click
from ghutil.types import Repository


@click.command()
@click.option("-f", "--force", is_flag=True, help="Delete without prompting")
@Repository.argument("repo")
def cli(repo, force):
    """Delete a repository"""
    repo.data  # Force fetching repo data before deletion
    if force or click.confirm(f"Delete repository {repo}?"):
        repo.delete()
        click.echo(f"Repository {repo} deleted")
    else:
        click.echo("Repository not deleted")
