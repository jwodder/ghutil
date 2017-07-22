import click

@click.command()
@click.argument('terms', nargs=-1, required=True)
@click.pass_obj
def cli(gh, terms):
    """ Search issues """
    for issue in gh.search('issues', *terms):
        click.echo(str(gh.issue(issue)))
