import re
import click
from   ghutil.showing import print_json

@click.command()
@click.option('-a', '--accept', multiple=True, metavar='MIME_TYPE')
@click.option('-d', '--data')
@click.option('-H', '--header', multiple=True)
@click.option(
    '-X', '--method',
    type=click.Choice(['GET', 'POST', 'PUT', 'PATCH', 'DELETE']),
    default='GET',
)
@click.argument('path')
@click.pass_obj
def cli(gh, path, method, accept, data, header):
    """ Make an arbitrary API request """
    extra_headers = {}
    if accept:
        extra_headers["Accept"] = ','.join(accept)
    for h in header:
        name, value = re.split(r'\s*:\s*', h, maxsplit=1)
        extra_headers[name] = value
    ret = gh[path][method](data=data, headers=extra_headers)
    if ret is not None:
        print_json(ret)
