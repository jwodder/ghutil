import click
from   ghutil.gists import gists_list_arg

@click.command()
@gists_list_arg
@click.pass_obj
def cli(gh, gists):
    """ Unstar gists """
    for g in gists:
        g.star.delete()
