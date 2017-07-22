import click

@click.command()
@click.pass_obj
def cli(gh):
    """ List starred gists """
    for gist in gh.gists.starred.get():
        click.echo(str(gh.gist(gist)))
