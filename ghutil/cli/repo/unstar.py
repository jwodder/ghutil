import click
from   ghutil.repos import parse_repo_spec

@click.command()
@click.argument('repos', nargs=-1)
@click.pass_obj
def cli(gh, repos):
    """ Unstar repositories """
    if not repos:
        repos = ['.']
    for r in repos:
        ### Show a human-friendly error message if parse_repo_spec fails?
        owner, repo = parse_repo_spec(r)
        if owner is None:
            owner = gh.me
        gh.user.starred[owner][repo].delete()
