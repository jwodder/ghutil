import click
from   ghutil.repos   import GHRepo
from   ghutil.showing import print_json, repo_info

@click.command()
@click.argument('repos', type=GHRepo(), nargs=-1)
@click.pass_obj
def cli(gh, repos):
    """ Show repository details """
    if not repos:
        repos = [gh.repository()]
    print_json([repo_info(r.get()) for r in repos])
