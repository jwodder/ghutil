import click
from   ghutil.gists import gist_arg

@click.command()
@click.confirmation_option(prompt='Delete this gist?')
@gist_arg
@click.pass_obj
def cli(gh, gist):
    """ Delete a gist """
    gist.delete()
