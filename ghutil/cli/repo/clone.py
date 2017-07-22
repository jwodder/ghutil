import subprocess
import click
from   ghutil.types import Repository

@click.command()
@click.option('--git', 'url', flag_value='git_url')
@click.option('--https', 'url', flag_value='clone_url')
@click.option('--ssh', 'url', flag_value='ssh_url', default=True)
@Repository.argument('repo', implicit=False)
@click.argument('dir', required=False)
@click.pass_context
def cli(ctx, repo, dir, url):  # noqa: B002
    """ Clone a GitHub repository """
    args = ['git', 'clone', repo.data[url]]
    if dir is not None:
        args.append(dir)
    ctx.exit(subprocess.call(args))
