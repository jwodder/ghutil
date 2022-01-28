import click


@click.command()
@click.option(
    "-A",
    "--asc",
    "--ascending",
    "direction",
    flag_value="asc",
    help="Sort in ascending order",
)
@click.option(
    "-D",
    "--desc",
    "--descending",
    "direction",
    flag_value="desc",
    help="Sort in descending order",
)
@click.option(
    "-S",
    "--sort",
    help="What to sort results by",
    type=click.Choice(["created", "updated"]),
)
@click.pass_obj
def cli(gh, **params):
    """List starred repositories"""
    for repo in gh.user.starred.get(params=params):
        click.echo(str(gh.repository(repo)))
