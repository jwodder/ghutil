import click
from   ghutil.showing import print_json

@click.command()
@click.option('-a', '--accept', multiple=True)
@click.option('-d', '--data')
@click.option(
    '-X', '--method',
    type=click.Choice(['GET', 'POST', 'PUT', 'PATCH', 'DELETE']),
    default='GET',
)
@click.argument('path')
@click.pass_obj
def cli(gh, path, method, accept, data):
    """ Make an arbitrary API request """
    headers = {}
    if accept:
        headers["Accept"] = '; '.join(accept)
    ret = gh[path][method](data=data, headers=headers)
    if ret is not None:
        print_json(ret)
