from   asciitree         import LeftAligned
from   asciitree.drawing import BoxStyle, BOX_LIGHT
import click
from   ghutil.repos      import GHRepo

class ForkTraversal:
    def __init__(self, gh, highlighted: [dict]):
        self.gh = gh
        self.highlighted = {h["full_name"] for h in highlighted}
        self.seen = set()

    def get_root(self, repo: dict) -> dict:
        return repo.get("source", repo)

    def get_children(self, repo: dict) -> [dict]:
        return list(self.gh[repo["forks_url"]].get())

    def get_text(self, repo: dict) -> str:
        txt = repo["full_name"]
        if txt in self.highlighted:
            self.seen.add(txt)
            txt = click.style(txt, bold=True)
        return txt


@click.command()
@click.argument('repos', type=GHRepo(), nargs=-1)
@click.pass_obj
def cli(gh, repos):
    """ Show a tree of forks """
    if not repos:
        repos = [gh.repository()]
    repos = [r.get() for r in repos]
    traverser = ForkTraversal(gh, repos)
    tree = LeftAligned(draw=BoxStyle(gfx=BOX_LIGHT), traverse=traverser)
    first = True
    for r in repos:
        if r["full_name"] not in traverser.seen:
            if first:
                first = False
            else:
                click.echo()
            click.echo(tree(r))
