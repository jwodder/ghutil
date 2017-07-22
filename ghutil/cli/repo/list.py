import click

@click.command()
@click.option('-A', '--asc', '--ascending', 'direction', flag_value='asc')
@click.option('-D', '--desc', '--descending', 'direction', flag_value='desc')
@click.option('-S', '--sort',
              type=click.Choice(['created', 'updated', 'pushed', 'full_name']))
@click.option('-t', '--type',
              type=click.Choice(['all','owner','public','private','member']))
@click.pass_obj
def cli(gh, **params):
    """ List your repositories """
    for repo in gh.user.repos.get(params=params):
        click.echo(str(gh.repository(repo)))
