import click

@click.command()
@click.pass_obj
def cli(gh):
    """ List your repositories """
    for repo in gh.user.repos.get():
        click.echo(repo["full_name"])
