### TODO: Try to somehow guard against trying to create a release for a tag
### that hasn't been pushed yet or that already has a release
import click
from   ghutil.edit    import edit_as_mail
from   ghutil.showing import print_json
from   ghutil.util    import get_last_tag

@click.command()
@click.argument('tag', default=get_last_tag)
@click.pass_obj
def cli(gh, tag):
    """ Create a GitHub release """
    data = {
        "tag_name": tag,
        "name": '',
        "draft": True,
        "prerelease": False,
        "body": '',
    }
    data.update(
        edit_as_mail(data, 'tag_name name draft prerelease'.split(), 'body')
    )
    if not data["tag_name"]:
        click.echo('Aborting release due to empty tag name')
    else:
        ### TODO: Add custom showing and verbosity
        print_json(gh.repository().releases.post(json=data))
