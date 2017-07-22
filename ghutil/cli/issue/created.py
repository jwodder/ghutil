# https://developer.github.com/v3/search/#search-issues
import click
from   ghutil.types import Repository

@click.command()
@click.pass_obj
def cli(gh):
    for issue in gh.search('issues', "author:" + gh.me):
        #click.echo(issue["html_url"])
        click.echo(
            '{!s:40}  #{:<5}  [{}]'.format(
                Repository.from_url(issue["repository_url"]),
                issue["number"],
                issue["state"].upper(),
            )
        )
