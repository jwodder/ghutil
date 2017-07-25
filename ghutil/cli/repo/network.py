from   asciitree         import LeftAligned
from   asciitree.drawing import BOX_LIGHT, BoxStyle
import click
from   ghutil.types      import Repository

class ForkTraversal:
    def __init__(self, gh, highlighted: [dict]):
        self.gh = gh
        self.highlighted = {h["full_name"] for h in highlighted}
        self.seen = set()

    def get_root(self, repo: dict) -> dict:
        return repo.get("source", repo)

    def get_children(self, repo: dict) -> [dict]:
        if repo["forks_count"]:
            return list(self.gh[repo["forks_url"]].get())
        else:
            return []

    def get_text(self, repo: dict) -> str:
        txt = repo["full_name"]
        if txt in self.highlighted:
            self.seen.add(txt)
            txt = click.style(txt, bold=True)
        return txt


@click.command()
@Repository.argument_list('repos')
@click.pass_obj
def cli(gh, repos):
    """ Show a tree of forks """
    repos = [r.data for r in repos]
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
