import click
from   ghutil.git   import clone_repo
from   ghutil.types import Gist

@click.command()
@click.option('--https', 'url', flag_value='https', help='Clone over HTTPS')
@click.option('--ssh', 'url', flag_value='ssh', default=True,
              help='Clone over SSH [default]')
@Gist.argument('gist', implicit=False)
@click.argument('dir', required=False)
@click.pass_context
def cli(ctx, gist, dir, url):  # noqa: B002
    """ Clone a gist """
    if url == 'https':
        clone_url = gist.data["git_pull_url"]
    elif url == 'ssh':
        # Why isn't this URL returned by the API?
        clone_url = f'git@gist.github.com:{gist.id}.git'
    clone_repo(clone_url, dir)
