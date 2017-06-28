import click
from   ghutil.repos import repo_arg

@click.command()
@click.option('-a', '--assignee', metavar='USER')
@click.option('-c', '--creator', metavar='USER')
@click.option('-l', '--label', multiple=True, metavar='LABEL')
@click.option('--mentioned', metavar='USER')
@click.option('-m', '--milestone', metavar='ID|TITLE')
@click.option('--since', metavar='TIMESTAMP')
@click.option('-s', '--state', type=click.Choice(['open', 'closed', 'all']))
@click.option('-A', '--asc', '--ascending', 'direction', flag_value='asc')
@click.option('-D', '--desc', '--descending', 'direction', flag_value='desc')
@click.option('-S', '--sort',
              type=click.Choice(['created', 'updated', 'comments']))
@repo_arg
def cli(repo, **params):
    """ List issues for a repository """
    if params.get('label'):
        params['label'] = ','.join(params['label'])
    for issue in repo.issues.get(params=params):
        click.echo(issue["html_url"])
