import click
from   ghutil.edit import edit_as_mail
from   ghutil.git  import get_last_tag

@click.command()
@click.argument('tag', default=get_last_tag)
@click.pass_obj
def cli(gh, tag):
    """ Edit a GitHub release """
    endpoint = gh.repository().releases
    data = endpoint.tags[tag].get()
    edited = edit_as_mail(data,'tag_name name draft prerelease'.split(),'body')
    if not edited:
        click.echo('No modifications made; exiting')
    else:
        ### TODO: Error on empty tag_name?
        endpoint[data['id']].patch(json=edited)
