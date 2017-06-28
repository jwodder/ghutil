import click
from   ghutil.issues import parse_issue_url
from   ghutil.repos  import repo_arg

@click.command()
@click.option('--base', metavar='BRANCH')
@click.option('--head', metavar='USER:BRANCH')
@click.option('-s', '--state', type=click.Choice(['open', 'closed', 'all']))
@click.option('-A', '--asc', '--ascending', 'direction', flag_value='asc')
@click.option('-D', '--desc', '--descending', 'direction', flag_value='desc')
@click.option('-S', '--sort',
              type=click.Choice(['created', 'updated', 'popularity', 'long-running']))
@repo_arg
def cli(repo, **params):
    """ List pull requests for a repository """
    for pr in repo.pulls.get(params=params):
        click.echo('/'.join(map(str, parse_issue_url(pr["url"]))))
