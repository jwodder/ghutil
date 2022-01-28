import itertools
import click


@click.command()
@click.option("--limit", type=int, help="Maximum number of results to return")
@click.option(
    "-A",
    "--asc",
    "--ascending",
    "order",
    flag_value="asc",
    help="Sort in ascending order",
)
@click.option(
    "-D",
    "--desc",
    "--descending",
    "order",
    flag_value="desc",
    help="Sort in descending order",
)
@click.option(
    "-S",
    "--sort",
    help="What to sort results by",
    type=click.Choice(["comments", "created", "updated"]),
)
@click.argument("terms", nargs=-1, required=True)
@click.pass_obj
def cli(gh, terms, limit, **params):
    """Search issues"""
    hits = gh.search("issues", *terms, **params)
    if limit is not None:
        hits = itertools.islice(hits, limit)
    for issue in hits:
        click.echo(str(gh.issue(issue)))
