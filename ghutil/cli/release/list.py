import click
from   ghutil.types import Repository

@click.command()
@Repository.argument('repo')
def cli(repo):
    """ List releases for a repository """
    for rel in repo.releases.get():
        #click.echo('/'.join(map(str, parse_release_url(rel["url"]))))
        click.echo(rel["tag_name"])
