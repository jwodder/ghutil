import click
from   ..api     import github_root
from   ..showing import print_json, gist_info

@click.command('gists')
def cli():
    """ List your gists """
    print_json(map(gist_info, github_root().gists.get()))
