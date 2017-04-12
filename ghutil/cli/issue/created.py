# https://developer.github.com/v3/search/#search-issues
import click
from   ghutil.repos import parse_repo_spec

@click.command()
@click.pass_obj
def cli(gh):
    me = gh.user.get()["login"]
    for issue in gh.search('issues', "author:" + me):
        #click.echo(issue["html_url"])
        click.echo(
            '{:40}  #{:<5}  [{}]'.format(
                #gh.repository(issue["repository_url"]).get()["full_name"],
                '{}/{}'.format(*parse_repo_spec(issue["repository_url"])),
                issue["number"],
                issue["state"].upper(),
            )
        )
