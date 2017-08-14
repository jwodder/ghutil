import click

@click.command()
@click.option('-A', '--asc', '--ascending', 'order', flag_value='asc',
              help='Sort in ascending order')
@click.option('-D', '--desc', '--descending', 'order', flag_value='desc',
              help='Sort in descending order')
@click.option('-S', '--sort', help='What to sort results by',
              type=click.Choice(['comments', 'created', 'updated']))
@click.argument('terms', nargs=-1, required=True)
@click.pass_obj
def cli(gh, terms, **params):
    """ Search issues """
    for issue in gh.search('issues', *terms, **params):
        click.echo(str(gh.issue(issue)))
