import click

@click.command()
@click.option('-f', '--filter', type=click.Choice([
    'assigned', 'created', 'mentioned', 'subscribed', 'all',
]), default='assigned')
@click.option('-s', '--state', type=click.Choice(['open', 'closed', 'all']),
              default='open')
@click.pass_obj
def cli(gh, filter, state):
    for issue in gh.issues.get(params={"filter": filter, "state": state}):
        click.echo(issue["html_url"])
