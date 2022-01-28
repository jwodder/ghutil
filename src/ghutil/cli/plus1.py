import re
import click


@click.command()
@click.argument("url", nargs=-1)
@click.pass_context
def cli(ctx, url):
    """Thumb-up issues, PRs, or comments thereon"""
    for u in url:
        m = re.fullmatch(
            r"(?:https?://)?(?:www\.)?github\.com"
            r"/(?P<owner>[^/]+)"
            r"/(?P<repo>[^/]+)"
            r"/(?:issues|pull)"
            r"/(?P<issue>\d+)"
            r"(?:#issuecomment-(?P<comment>\d+))?",
            u,
        )
        if not m:
            click.echo(f"{ctx.command_path}: could not parse {u!r}", err=True)
            continue
        endpoint = ctx.obj.repos[m.group("owner")][m.group("repo")].issues
        if m.group("comment") is None:
            endpoint = endpoint[m.group("issue")].reactions
        else:
            endpoint = endpoint.comments[m.group("comment")].reactions
        endpoint.post(json={"content": "+1"})
