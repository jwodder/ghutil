import click
from   ghutil.showing import print_json

# Note: Options with multiple names need to have their desired name given
# explicitly due to <https://github.com/pallets/click/issues/793>
@click.command()
@click.option('--allow-merge-commit/--no-merge-commit', default=True)
@click.option('--allow-rebase-merge/--no-rebase-merge', default=True)
@click.option('--allow-squash-merge/--no-squash-merge', default=True)
@click.option('--auto-init/--no-init', '--init', 'auto_init', default=False)
@click.option('-d', '--description')
@click.option('--gitignore-template', '--gitignore', 'gitignore_template')
@click.option('--has-issues/--no-issues', default=True)
### TODO: Handle `has_projects` defaulting to false in organizations without
### projects; will setting the default value to `None` do the right thing?
@click.option('--has-projects/--no-projects', default=True)
@click.option('--has-wiki/--no-wiki', default=True)
@click.option('-H', '--homepage')
@click.option('--license-template', '--license', 'license_template')
@click.option('-O', '--organization')
@click.option('-P', '--private', is_flag=True)
@click.option('-v', '--verbose', is_flag=True)
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
