import re
import click

@click.command()
@click.argument('url', nargs=-1)
@click.pass_context
def cli(ctx, url):
    """ Thumb-up issues, PRs, or comments thereon """
    for u in url:
        m = re.match(r'^(?:https?://)?(?:www\.)?github\.com'
                     r'/(?P<owner>[^/]+)'
                     r'/(?P<repo>[^/]+)'
                     r'/(?:issues|pull)'
                     r'/(?P<issue>\d+)'
                     r'(?:#issuecomment-(?P<comment>\d+))?$', u)
        if not m:
            click.echo('{}: could not parse {!r}'.format(ctx.command_path, u),
                       err=True)
            continue
        endpoint = ctx.obj.repos[m.group('owner')][m.group('repo')].issues
        if m.group('comment') is None:
            endpoint = endpoint[m.group('issue')].reactions
        else:
            endpoint = endpoint.comments[m.group('comment')].reactions
        # Due to what appears to be a bug in the GitHub API, requests to
        # reaction URLs need to list squirrel-girl-preview as the first (or
        # only) media type in the Accept header
        endpoint.post(
            headers={"Accept": "application/vnd.github.squirrel-girl-preview"},
            json={"content": "+1"},
        )
