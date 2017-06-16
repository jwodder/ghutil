import click
from   ghutil.repos   import repos_list_arg
from   ghutil.showing import print_json, repo_info

@click.command()
@click.option('-v', '--verbose', is_flag=True)
@repos_list_arg
def cli(repos, verbose):
    """ Show repository details """
    print_json([repo_info(r.get(), verbose) for r in repos])
