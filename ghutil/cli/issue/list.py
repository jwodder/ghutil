import click
from   ghutil.types import Repository

@click.command()
@click.option('-a', '--assignee', metavar='USER',
              help='Only show issues assigned to the given user')
@click.option('-c', '--creator', metavar='USER',
              help='Only show issues created by the given user')
@click.option('-l', '--label', multiple=True, metavar='LABEL',
              help='Only show issues with the given label.'
                   '  May be specified multiple times')
@click.option('--mentioned', metavar='USER',
              help='Only show issues mentioning the given user')
@click.option('-m', '--milestone', metavar='URL|TITLE',
              help='Only show issues belonging to the given milestone')
@click.option('--since', metavar='TIMESTAMP',
              help='Only show issues updated on or after the given timestamp')
@click.option('-s', '--state', type=click.Choice(['open', 'closed', 'all']),
              help='Only show issues in the given state')
@click.option('-A', '--asc', '--ascending', 'direction', flag_value='asc',
              help='Sort in ascending order')
@click.option('-D', '--desc', '--descending', 'direction', flag_value='desc',
              help='Sort in descending order')
@click.option('-S', '--sort', help='What to sort results by',
              type=click.Choice(['created', 'updated', 'comments']))
@Repository.argument('repo')
@click.pass_obj
def cli(gh, repo, **params):
    """ List issues for a repository """
    if params.get('label'):
        params['label'] = ','.join(params['label'])
    if params["milestone"] not in (None, 'none', '*'):
        params["milestone"] = int(repo.milestone(params["milestone"]))
    for issue in repo.issues.get(params=params):
        click.echo(str(gh.issue(issue)))
