import click
from   ghutil.showing import print_json
from   ghutil.types   import Repository

@click.command()
@Repository.option('-R', '--repo', '--repository', 'repo',
                   help='Repository to list the milestones of')
@click.option('-s', '--state', type=click.Choice(['open', 'closed', 'all']),
              help='Only show milestones in the given state')
@click.option('-A', '--asc', '--ascending', 'direction', flag_value='asc',
              help='Sort in ascending order')
@click.option('-D', '--desc', '--descending', 'direction', flag_value='desc',
              help='Sort in descending order')
@click.option('-S', '--sort', help='What to sort results by',
              type=click.Choice(['completeness', 'due_on']))
@click.option('-v', '--verbose', is_flag=True, help='Show full response body')
@click.pass_obj
def cli(gh, repo, verbose, **params):
    """ List milestones for a repository """
    milestones = repo.milestones.get(params=params)
    if verbose:
        print_json(milestones)
    else:
        for m in milestones:
            click.echo(m["title"])
