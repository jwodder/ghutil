import click
from   ghutil.showing import print_json
from   ghutil.types   import Repository

@click.command()
@Repository.option('-R', '--repo', '--repository', 'repo',
                   help='Repository in which to create the label')
@click.argument('name')
@click.argument('color')
def cli(repo, name, color):
    """
    Create a label.

    The label color must be specified as a six-character hex code, e.g.,
    `ff00ff`.
    """
    print_json(repo.labels.post(json={
        "name": name,
        "color": color.lstrip('#'),
    }))
