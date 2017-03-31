import click
from   ..api     import paginate
from   ..showing import print_json, gist_info

@click.command('gists')
def cli():
    """ List your gists """
    print_json(map(gist_info, paginate('https://api.github.com/gists')))
