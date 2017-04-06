# https://developer.github.com/v3/search/#search-issues
import click

@click.command()
@click.pass_obj
def cli(gh):
    me = gh.user.get()["login"]
    for issue in gh.search('issues', "author:" + me):
        click.echo(issue["html_url"])
