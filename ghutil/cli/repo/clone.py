import subprocess
import click
from   ghutil.repos import repo_arg

@click.command()
@click.option('--git', 'url', flag_value='git_url')
@click.option('--https', 'url', flag_value='clone_url')
@click.option('--ssh', 'url', flag_value='ssh_url', default=True)
@repo_arg(implicit=False)
@click.argument('dir', required=False)
def cli(repo, dir, url):  # noqa: B002
    """ Clone a GitHub repository """
    args = ['git', 'clone', repo.get()[url]]
    if dir is not None:
        args.append(dir)
    subprocess.check_call(args)
