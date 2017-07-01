import click
from   ghutil.gists import GHGist

@click.command()
@click.confirmation_option(prompt='Delete this gist?')
@click.argument('gist', type=GHGist())
@click.pass_obj
def cli(gh, gist):
    """ Delete a gist """
    gist.delete()
