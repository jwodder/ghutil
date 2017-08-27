import click
from   ghutil.types import Repository

@click.command()
@Repository.option('-R', '--repo', '--repository', 'repo',
                   help='Repository to which the milestone belongs')
@click.option('-f', '--force', is_flag=True, help='Delete without prompting')
@click.argument('milestone')
def cli(repo, milestone, force):
    """ Delete a milestone """
    ms = repo.milestone(milestone)
    if force or click.confirm(
        'Delete milestone {!r} (#{}) from {}?'
            .format(str(ms), int(ms), repo.data["full_name"])
    ):
        ms.delete()
        click.echo('Milestone {!r} deleted'.format(str(ms)))
    else:
        click.echo('Milestone not deleted')
