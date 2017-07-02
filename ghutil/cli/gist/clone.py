import subprocess
import click
from   ghutil.gists import gist_arg

@click.command()
@click.option('--https', 'url', flag_value='https')
@click.option('--ssh', 'url', flag_value='ssh', default=True)
@gist_arg(implicit=False)
@click.argument('dir', required=False)
@click.pass_context
def cli(ctx, gist, dir, url):  # noqa: B002
    """ Clone a gist """
    if url == 'https':
        clone_url = gist.get()["git_pull_url"]
    elif url == 'ssh':
        # Why isn't this URL returned by the API?
        clone_url = 'git@gist.github.com:{}.git'.format(gist.get()["id"])
    args = ['git', 'clone', clone_url]
    if dir is not None:
        args.append(dir)
    ctx.exit(subprocess.call(args))
