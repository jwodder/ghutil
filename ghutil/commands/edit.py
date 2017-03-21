import click
import requests
from   ..api   import show_response
from   ..edit  import edit_as_mail
from   ..local import get_github_repo

@click.command('edit')
def cli():
    """ Edit repository details """
    owner, repo = get_github_repo()
    url = 'https://api.github.com/repos/{}/{}'.format(owner, repo)
    s = requests.Session()
    r = s.get(url)
    if not r.ok:
        show_response(r)
    about = r.json()
    edited = edit_as_mail(about, 'name private description homepage'
                                 ' default_branch has_wiki has_issues'.split())
    if not edited:
        click.echo('No modifications made; exiting')
    else:
        r = s.patch(url, json=edited)
        if not r.ok:
            show_response(r)
