# <https://developer.github.com/v3/repos/releases/>
### TODO: Try to somehow guard against trying to create a release for a tag
### that hasn't been pushed yet
import subprocess
import attr
import click
from   headerparser import HeaderParser, BOOL
from   ..api        import github_root
from   ..local      import get_github_repo

@attr.s
class ReleaseData:
    tag_name   = attr.ib()
    name       = attr.ib()
    body       = attr.ib(default='')
    draft      = attr.ib(default=True)
    prerelease = attr.ib(default=False)

    def to_payload(self):
        return vars(self)

    def to822(self):
        return 'Tag: ' + self.tag_name + '\n' \
             + 'Name: ' + self.name + '\n' \
             + 'Draft: ' + ('yes' if self.draft else 'no') + '\n' \
             + 'Prerelease: ' + ('yes' if self.prerelease else 'no') + '\n' \
             + '\n' \
             + self.body.strip() + '\n'

    @classmethod
    def from822(cls, txt):
        parser = HeaderParser()
        parser.add_field('tag', required=True, dest='tag_name')
        parser.add_field('name', required=True)
        parser.add_field('draft', type=BOOL, default=True)
        parser.add_field('prerelease', type=BOOL, default=False)
        msg = parser.parse_string(txt)
        # When communicating with GitHub, "body" cannot be None.
        return cls(body=msg.body or '', **msg)


@click.command('release')
#@click.option('--delete', ### flag )
# -C, --chdir
# --owner
# --repo
# --remote-name / --remote-url ?
@click.argument('tag', required=False)
@click.pass_context
def cli(ctx, tag):
    """ Create or edit a GitHub release """
    owner, repo = get_github_repo()
    if tag is None:
        ### TODO: Fetch just the name of the latest tag when HEAD isn't tagged
        tag = subprocess.check_output(
            ['git', 'describe'], universal_newlines=True,
        ).strip()

    endpoint = github_root().repos[owner][repo].releases
    data = endpoint.tags[tag].get(maybe=True)
    if data is not None:
        relid = data["id"]
        release = ReleaseData(**{
            f.name: data[f.name]
            for f in attr.fields(ReleaseData)
            if f.name in data
        })
    else:
        relid = None
        release = ReleaseData(
            tag_name=tag,
            name='Version {} — INSERT SHORT DESCRIPTION HERE'
                .format(tag.lstrip('v')),
            body='INSERT LONG DESCRIPTION HERE (optional)',
        )
    edited = click.edit(release.to822())
    if edited is not None:
        newrelease = ReleaseData.from822(edited)
    if edited is None or newrelease == release:
        click.echo('No modifications made; exiting')
        ctx.exit()
    if relid is None:
        endpoint.post(json=newrelease.to_payload())
    else:
        endpoint[relid].patch(json=newrelease.to_payload())
