import click
from   ghutil.edit  import edit_as_mail
from   ghutil.repos import repo_arg

@click.command()
@click.option('-n', '--name')
@click.option('-b', '--default-branch')
@click.option('-d', '--description')
@click.option('-H', '--homepage')
@click.option('-P/-p', '--private/--public', default=None)
@click.option('--has-wiki/--no-wiki', default=None)
@click.option('--has-issues/--no-issues', default=None)
@repo_arg
def cli(repo, **opts):
    """ Edit repository details """
    edited = {k:v for k,v in opts.items() if v is not None}
    if edited:
        if 'name' not in edited:
            edited['name'] = repo.get()["name"]
        repo.patch(json=edited)
    else:
        about = repo.get()
        edited = edit_as_mail(about, 'name private description homepage'
                                     ' default_branch has_wiki has_issues')
        if not edited:
            click.echo('No modifications made; exiting')
        else:
            edited.setdefault("name", about["name"])
            repo.patch(json=edited)
