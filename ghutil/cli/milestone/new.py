import click
from   ghutil.showing import print_json
from   ghutil.types   import Milestone, Repository

@click.command()
@Repository.option('-R', '--repo', '--repository', 'repo',
                   help='Repository in which to create the milestone')
@click.option('-d', '--description', help='Set milestone description')
@click.option('--due-on', '--due', 'due_on', metavar='TIMESTAMP',
              help='Set milestone due date')
@click.option('--open', 'state', flag_value='open', default=True,
              help='Create milestone open  [default]')
@click.option('--closed', '--close', 'state', flag_value='closed',
              help='Create milestone closed')
@click.option('-v', '--verbose', is_flag=True, help='Show full response body')
@click.argument('title')
@click.pass_obj
def cli(gh, repo, verbose, **kwargs):
    """ Create a milestone """
    print_json(
        Milestone.from_data(gh, repo.milestones.post(json=kwargs)),
        verbose,
    )
