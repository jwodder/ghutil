import click
from   ghutil.repos   import GHRepo
from   ghutil.showing import print_json, repo_info

@click.command()
@click.option('-v', '--verbose', is_flag=True)
@click.argument('repos', type=GHRepo(), nargs=-1)
@click.pass_obj
def cli(gh, repos, verbose):
    """ Show repository details """
    if not repos:
        repos = [gh.repository()]
    print_json([repo_info(r.get(), verbose) for r in repos])
