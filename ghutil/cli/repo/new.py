import click
from   ghutil.showing import print_json

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
@click.option('-d', '--description', help='Set repository description')
@click.option('--gitignore-template', '--gitignore', 'gitignore_template',
              help='Create an initial commit with the given .gitignore')
@click.option('--has-issues/--no-issues', default=True, show_default=True,
              help='Enable/disable issues for the repository')
### TODO: Handle `has_projects` defaulting to false in organizations without
### projects; will setting the default value to `None` do the right thing?
@click.option('--has-projects/--no-projects', default=True, show_default=True,
              help='Enable/disable projects in the repository')
@click.option('--has-wiki/--no-wiki', default=True, show_default=True,
              help="Enable/disable the repository's wiki")
@click.option('-H', '--homepage', metavar='URL', help='Set repository homepage')
@click.option('--license-template', '--license', 'license_template',
              help='Create an initial commit with the given license')
@click.option('-O', '--organization',
              help='Create the repository in the given organization')
@click.option('-P', '--private', is_flag=True, help='Make repository private')
@click.option('-v', '--verbose', is_flag=True, help='Show full response body')
### TODO: team_id
@click.argument('name')
@click.pass_obj
def cli(gh, organization, verbose, **kwargs):
    """ Create a new repository """
    if organization is None:
        ep = gh.user.repos
    else:
        ep = gh.orgs[organization].repos
    print_json(gh.repository(ep.post(json=kwargs)), verbose)
