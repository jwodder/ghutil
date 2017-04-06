import click

@click.command()
@click.argument('terms', nargs=-1, required=True)
@click.pass_obj
def cli(gh, terms):
    """ Search repositories """
    for repo in gh.search('repositories', *terms):
        click.echo(repo["full_name"])
