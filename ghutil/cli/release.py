# <https://developer.github.com/v3/repos/releases/>
### TODO: Try to somehow guard against trying to create a release for a tag
### that hasn't been pushed yet
import subprocess
import click
from   ghutil.edit import edit_as_mail

@click.command()
@click.argument('tag', required=False)
@click.pass_obj
def cli(gh, tag):
    """ Create or edit a GitHub release """
    if tag is None:
        ### TODO: Fetch just the name of the latest tag when HEAD isn't tagged
        tag = subprocess.check_output(
            ['git', 'describe'], universal_newlines=True,
        ).strip()
    endpoint = gh.repository().releases
    data = endpoint.tags[tag].get(maybe=True)
    if data is None:
        data = {
            "tag_name": tag,
            "name": 'v{} — INSERT SHORT DESCRIPTION HERE'
                    .format(tag.lstrip('v')),
            "draft": True,
            "prerelease": False,
            "body": 'INSERT LONG DESCRIPTION HERE (optional)',
        }
    edited = edit_as_mail(data,'tag_name name draft prerelease'.split(),'body')
    if not edited:
        click.echo('No modifications made; exiting')
    elif 'id' in data:
        endpoint[data['id']].patch(json=edited)
    else:
        endpoint.post(json=edited)
