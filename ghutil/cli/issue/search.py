import click
from   ghutil.issues import parse_issue_url

@click.command()
@click.argument('terms', nargs=-1, required=True)
@click.pass_obj
def cli(gh, terms):
    """ Search issues """
    for issue in gh.search('issues', *terms):
        click.echo('/'.join(map(str, parse_issue_url(issue["url"]))))
