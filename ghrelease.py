#!/usr/bin/python3
# <https://developer.github.com/v3/repos/releases/>
### TODO: Try to somehow guard against trying to create a release for a tag
### that hasn't been pushed yet
import subprocess
import attr
import click
from   headerparser import HeaderParser, BOOL
import requests
import ghutil

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
        parser.add_header('tag', required=True, dest='tag_name')
        parser.add_header('name', required=True)
        parser.add_header('draft', type=BOOL, default=True)
        parser.add_header('prerelease', type=BOOL, default=False)
        msg = parser.parse_string(txt)
        return cls(body=msg.body or '', **msg)
        ### Should/can an empty body be None?


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
#@click.option('--delete', ### flag )
# -C, --chdir
# --owner
# --repo
# --remote-name / --remote-url ?
@click.argument('tag', required=False)
@click.pass_context
def ghrelease(ctx, tag):
    """ Create or edit a GitHub release """
    owner, repo = ghutil.get_github_repo()
    relurl = 'https://api.github.com/repos/{}/{}/releases'.format(owner, repo)
    if tag is None:
        ### TODO: Fetch just the name of the latest tag when HEAD isn't tagged
        tag = subprocess.check_output(
            ['git', 'describe'], universal_newlines=True,
        ).strip()
    s = requests.Session()
    r = s.get('{}/tags/{}'.format(relurl, tag))
    if r.ok:
        data = r.json()
        relid = data["id"]
        release = ReleaseData(**{
            f.name: data[f.name]
            for f in attr.fields(ReleaseData)
            if f.name in data
        })
    elif r.status_code == 404:
        relid = None
        release = ReleaseData(
            tag_name=tag,
            name='Version {} — INSERT SHORT DESCRIPTION HERE'
                .format(tag.lstrip('v')),
            body='INSERT LONG DESCRIPTION HERE (optional)',
        )
    else:
        ghutil.show_response(r)
    edited = click.edit(release.to822())
    if edited is not None:
        newrelease = ReleaseData.from822(edited)
    if edited is None or newrelease == release:
        click.echo('No modifications made; exiting')
        ctx.exit()
    if relid is None:
        r = s.post(relurl, json=newrelease.to_payload())
    else:
        r = s.patch('{}/{}'.format(relurl, relid), json=newrelease.to_payload())
    if not r.ok:
        ghutil.show_response(r)

if __name__ == '__main__':
    ghrelease()
