import click
from   ghutil.edit  import edit_as_mail
from   ghutil.types import Repository

@click.command()
@click.option('-n', '--name', help='Rename repository')
@click.option('-b', '--default-branch',
              help="Change the repository's default branch")
@click.option('-d', '--description', help='Set repository description')
@click.option('--has-issues/--no-issues', default=None,
              help='Enable/disable issues for repository')
@click.option('--has-wiki/--no-wiki', default=None,
              help="Enable/disable the repository's wiki")
@click.option('-H', '--homepage', metavar='URL', help='Set repository homepage')
@click.option('-P/-p', '--private/--public', default=None,
              help='Make repository private/public')
@Repository.argument('repo')
def cli(repo, **opts):
    """
    Edit repository details.

    If one or more options are given on the command line, the repository is
    modified accordingly.  Otherwise, an editor is started, allowing you to
    modify the repository's details as a text file.
    """
    edited = {k:v for k,v in opts.items() if v is not None}
    # The repository may have been renamed, leaving a redirect at the old name,
    # and so the name supplied by the user might not equal the current one.
    # Thus, get the repository's name from the API via `repo.data["name"]`
    # instead of from the user via `repo.repo`.
    if edited:
        if 'name' not in edited:
            edited['name'] = repo.data["name"]
        repo.patch(json=edited)
    else:
        edited = edit_as_mail(repo.data, 'name private description homepage'
                                         ' default_branch has_wiki has_issues')
        if not edited:
            click.echo('No modifications made; exiting')
        else:
            edited.setdefault("name", repo.data["name"])
            repo.patch(json=edited)
