import click

@click.command()
@click.pass_obj
def cli(gh):
    """ List starred repositories """
    for repo in gh.user.starred.get():
        click.echo(str(gh.repository(repo)))
