import click
from   ghutil.repos import repo_arg

@click.command()
@repo_arg
def cli(repo):
    """ List releases for a repository """
    for rel in repo.releases.get():
        #click.echo('/'.join(map(str, parse_release_url(rel["url"]))))
        click.echo(rel["tag_name"])
