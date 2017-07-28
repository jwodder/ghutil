import click

@click.command()
@click.option('-A', '--asc', '--ascending', 'direction', flag_value='asc',
              help='Sort in ascending order')
@click.option('-D', '--desc', '--descending', 'direction', flag_value='desc',
              help='Sort in descending order')
@click.option('-S', '--sort', help='What to sort results by',
              type=click.Choice(['created', 'updated', 'pushed', 'full_name']))
@click.option('-t', '--type', help='Only show the given type of repositories',
              type=click.Choice(['all','owner','public','private','member']))
@click.pass_obj
def cli(gh, **params):
    """ List your repositories """
    for repo in gh.user.repos.get(params=params):
        click.echo(str(gh.repository(repo)))
