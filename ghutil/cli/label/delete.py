import click
from   ghutil.types import Repository

@click.command()
@Repository.option('-R', '--repo', '--repository', 'repo',
                   help='Repository to which the label belongs')
@click.option('-f', '--force', is_flag=True, help='Delete without prompting')
@click.argument('label')
def cli(repo, label, force):
    """ Delete a label """
    ### TODO: Check that the label actually exists first?
    if force or click.confirm(
        'Delete label {!r} from {}?'.format(label, repo.data["full_name"])
    ):
        repo.labels[label].delete()
        click.echo('Label {!r} deleted'.format(label))
    else:
        click.echo('Label not deleted')
