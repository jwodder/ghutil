import click
from ghutil.showing import print_json
from ghutil.types import Repository
from ghutil.util import optional


@click.command()
@Repository.option(
    "-R",
    "--repo",
    "--repository",
    "repo",
    help="Repository in which to create the label",
)
@optional("-d", "--description", help="Set label description")
@click.argument("name")
@click.argument("color")
def cli(repo, **kwargs):
    """
    Create a label.

    The label color must be specified as a six-character hex code, e.g.,
    `ff00ff`.
    """
    kwargs["color"] = kwargs["color"].lstrip("#")
    print_json(repo.labels.post(json=kwargs))
