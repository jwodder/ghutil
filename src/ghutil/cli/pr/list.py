import click
from   ghutil.types import Repository

@click.command()
@click.option('--base', metavar='BRANCH',
              help='Only show PRs for the given base branch')
@click.option('--head', metavar='USER:BRANCH',
              help='Only show PRs from the given head')
@click.option('-s', '--state', type=click.Choice(['open', 'closed', 'all']),
              help='Only show PRs in the given state')
@click.option('-A', '--asc', '--ascending', 'direction', flag_value='asc',
              help='Sort in ascending order')
@click.option('-D', '--desc', '--descending', 'direction', flag_value='desc',
              help='Sort in descending order')
@click.option('-S', '--sort', help='What to sort results by',
              type=click.Choice(['created', 'updated', 'popularity', 'long-running']))
@Repository.argument('repo')
@click.pass_obj
def cli(gh, repo, **params):
    """ List pull requests for a repository """
    for pr in repo.pulls.get(params=params):
        click.echo(str(gh.pull_request(pr)))
