import re
import click
from ghutil.api.util import die, echo_response
from ghutil.showing import print_json


@click.command()
@click.option("-d", "--data", metavar="TEXT|@FILE", help="Set request body")
@click.option(
    "-H",
    "--header",
    multiple=True,
    help="Add custom HTTP header to request." "  May be specified multiple times.",
)
@click.option(
    "--paginate", "do_paginate", is_flag=True, help='Follow all "next" Link headers'
)
@click.option(
    "-X",
    "--request",
    "method",
    type=click.Choice(["GET", "POST", "PUT", "PATCH", "DELETE"]),
    default="GET",
    help="Set HTTP request method",
)
@click.argument("path")
@click.pass_obj
def cli(gh, path, method, data, header, do_paginate):
    """Make an arbitrary API request"""
    extra_headers = {}
    for h in header:
        name, value = re.split(r"\s*:\s*", h, maxsplit=1)
        extra_headers[name] = value
    if data is not None and len(data) > 1 and data[0] == "@":
        with click.open_file(data[1:]) as fp:
            data = fp.read()
    r = gh[path][method](decode=False, data=data, headers=extra_headers)
    if not r.ok:
        die(r)
    elif do_paginate and method.lower() == "get" and "next" in r.links:
        for q in gh.paginate(r):
            print_json(q)
    else:
        echo_response(r)
