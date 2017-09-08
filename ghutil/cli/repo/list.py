import click

@click.command()
@click.option(
    '--affiliation',
    help='Comma-separated list of "owner", "collaborator", and/or "organization_member"',
)
@click.option('-A', '--asc', '--ascending', 'direction', flag_value='asc',
              help='Sort in ascending order')
@click.option('-D', '--desc', '--descending', 'direction', flag_value='desc',
              help='Sort in descending order')
@click.option('-S', '--sort', help='What to sort results by',
              type=click.Choice(['created', 'updated', 'pushed', 'full_name']))
@click.option('-t', '--type', help='Filter by repository type/affiliation',
              type=click.Choice(['all','owner','public','private','member']))
@click.option('--visibility', help='Filter by repository visibility',
              type=click.Choice(['all', 'public', 'private']))
@click.argument('user', required=False)
@click.pass_obj
def cli(gh, user, **params):
    """
    List a user's repositories.

    If no user is specified, list all repositories for the current user.

    Note that the `--type` option cannot be used together with `--affiliation`
    or `--visibility`.

    Note that the `--affiliation` and `--visibility` options and certain values
    for `--type` cannot be used when fetching another user's repositories.
    """
    if user is None:
        repos = gh.user.repos.get(params=params)
    else:
        repos = gh.users[user].repos.get(params=params)
    for repo in repos:
        click.echo(str(gh.repository(repo)))
