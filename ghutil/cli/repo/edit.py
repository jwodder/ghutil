import click
from   ghutil.edit  import edit_as_mail
from   ghutil.types import Repository

@click.command()
@click.option('-n', '--name')
@click.option('-b', '--default-branch')
@click.option('-d', '--description')
@click.option('-H', '--homepage')
@click.option('-P/-p', '--private/--public', default=None)
@click.option('--has-wiki/--no-wiki', default=None)
@click.option('--has-issues/--no-issues', default=None)
@Repository.argument('repo')
def cli(repo, **opts):
    """ Edit repository details """
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
