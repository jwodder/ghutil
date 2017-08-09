import re
import click
from   ghutil.showing import print_json

@click.command()
@click.option('-d', '--data', help='Set request body')
@click.option('-H', '--header', multiple=True,
              help='Add custom HTTP header to request.'
                   '  May be specified multiple times.')
@click.option(
    '-X', '--request',
    type=click.Choice(['GET', 'POST', 'PUT', 'PATCH', 'DELETE']),
    default='GET',
    help='Set HTTP request method',
)
@click.argument('path')
@click.pass_obj
def cli(gh, path, request, data, header):
    """ Make an arbitrary API request """
    extra_headers = {}
    for h in header:
        name, value = re.split(r'\s*:\s*', h, maxsplit=1)
        extra_headers[name] = value
    ret = gh[path][request](data=data, headers=extra_headers)
    if ret is not None:
        print_json(ret)
