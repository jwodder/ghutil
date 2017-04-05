import click
from   ghutil.showing import print_json, gist_info

@click.command()
@click.pass_obj
def cli(gh):
    """ List your gists """
    print_json(map(gist_info, gh.gists.get()))
