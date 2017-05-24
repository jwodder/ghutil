import subprocess
import click
from   ghutil.repos import GHRepo

@click.command()
@click.option('--git', 'url', flag_value='git_url')
@click.option('--https', 'url', flag_value='clone_url')
@click.option('--ssh', 'url', flag_value='ssh_url', default=True)
@click.argument('repo', type=GHRepo())
@click.argument('dir', required=False)
def cli(repo, dir, url):  # noqa: B002
    """ Clone a GitHub repository """
    args = ['git', 'clone', repo.get()[url]]
    if dir is not None:
        args.append(dir)
    subprocess.check_call(args)
