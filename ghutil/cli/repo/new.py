import click
from   ghutil.showing import print_json
from   ghutil.util    import optional

# Note: Options with multiple names need to have their desired name given
# explicitly due to <https://github.com/pallets/click/issues/793>
@click.command()
@click.option('--allow-merge-commit/--no-merge-commit', default=True,
              help='Allow merging PRs with merge commits?', show_default=True)
@click.option('--allow-rebase-merge/--no-rebase-merge', default=True,
              help='Allow rebase-merging PRs?', show_default=True)
@click.option('--allow-squash-merge/--no-squash-merge', default=True,
              help='Allow squash-merging PRs?', show_default=True)
@click.option('--auto-init/--no-init', '--init', 'auto_init', default=False,
              help='Whether to create an initial commit with an empty README',
              show_default=True)
@optional('-d', '--description', help='Set repository description')
@optional('--gitignore-template', '--gitignore', 'gitignore_template',
          help='Create an initial commit with the given .gitignore')
@click.option('--has-issues/--no-issues', default=True, show_default=True,
              help='Enable/disable issues for the repository')
# Note that `has_projects`'s actual default value changes to false when
# creating a repo in an organization without projects, in which case trying to
# set it to true returns an error.  It's thus safer to not set this option at
# all if the user didn't specify it explicitly.
@optional('--has-projects/--no-projects',
          help='Enable/disable projects in the repository  [default: True]')
@click.option('--has-wiki/--no-wiki', default=True, show_default=True,
              help="Enable/disable the repository's wiki")
@optional('-H', '--homepage', metavar='URL', help='Set repository homepage')
@optional('--license-template', '--license', 'license_template',
          help='Create an initial commit with the given license')
@click.option('-O', '--organization',
              help='Create the repository in the given organization')
@click.option('-P/-p', '--private/--public', default=False,
              help='Make repository private/public  [default: public]')
@optional('--team', metavar='ID|NAME',
          help='Grant the given team access to the repository')
@click.option('-v', '--verbose', is_flag=True, help='Show full response body')
@click.argument('name')
@click.pass_context
def cli(ctx, organization, verbose, **kwargs):
    """ Create a new repository """
    if organization is None:
        if 'team' in kwargs:
            ctx.fail('--team cannot be used without --organization')
        ep = ctx.obj.user.repos
    else:
        if 'team' in kwargs:
            kwargs["team_id"] = ctx.obj.parse_team(
                organization,
                kwargs.pop("team"),
            )
        ep = ctx.obj.orgs[organization].repos
    print_json(ctx.obj.repository(ep.post(json=kwargs)), verbose)
