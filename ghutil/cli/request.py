import click
from   ghutil.showing import print_json

@click.command()
@click.option(
    '-X', '--method',
    type=click.Choice(['GET', 'POST', 'PUT', 'PATCH', 'DELETE']),
    default='GET',
)
@click.option('-d', '--data')
@click.argument('path')
@click.pass_obj
def cli(gh, path, method, data):
    """ Make an arbitrary API request """
    ret = gh[path][method](data=data)
    if ret is not None:
        print_json(ret)
