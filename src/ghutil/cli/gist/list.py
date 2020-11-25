import click

@click.command()
@click.pass_obj
def cli(gh):
    """ List your gists """
    for gist in gh.gists.get():
        click.echo(str(gh.gist(gist)))
