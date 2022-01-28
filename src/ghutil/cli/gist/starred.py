import click


@click.command()
@click.option(
    "--since",
    metavar="TIMESTAMP",
    help="Only show gists updated on or after the given timestamp",
)
@click.pass_obj
def cli(gh, since):
    """List starred gists"""
    for gist in gh.gists.starred.get(params={"since": since}):
        click.echo(str(gh.gist(gist)))
