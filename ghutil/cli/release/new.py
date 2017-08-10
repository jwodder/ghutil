### TODO: Try to somehow guard against trying to create a release for a tag
### that hasn't been pushed yet or that already has a release
import click
from   ghutil.edit    import edit_as_mail
from   ghutil.git     import get_last_tag
from   ghutil.showing import print_json

@click.command()
@click.option('--draft/--published', ' /--publish', 'draft', default=False,
              help='Whether to create a draft (unpublished) release'
                   ' [default: --published]')
@click.option('--prerelease/--full-release', '--pre/--full', 'prerelease',
              default=False,
              help='Whether this is a prerelease [default: --full-release]')
@click.option('-b', '--body', type=click.File(),
              help='File containing release body')
@click.option('-n', '--name', help='Release name')
@click.option('-v', '--verbose', is_flag=True, help='Show full response body')
@click.argument('tag', default=get_last_tag)
@click.pass_obj
def cli(gh, tag, name, body, draft, prerelease, verbose):
    """
    Convert a tag into a GitHub release.

    The tag must belong to the current repository and must have already been
    pushed to GitHub.  If no tag is specified, a release is created for the
    most recent tag reachable from the current repository's HEAD.

    Unless both a release name and a file containing a release body are
    specified on the command line, an editor will be opened for you to provide
    the missing details.
    """
    data = {
        "tag_name": tag,
        "name": name if name is not None else '',
        "draft": draft,
        "prerelease": prerelease,
        "body": body.read() if body is not None else '',
    }
    # Note: GitHub allows a release's name and body to both be the empty string
    # (in which case the web API displays the tag name and commit message,
    # respectively, in their stead), but it does not allow them to be null.
    if name is None or body is None:
        edited = edit_as_mail(data, 'tag_name name draft prerelease', 'body')
        if edited is None:
            click.echo('No changes saved; exiting')
            return
        data.update(edited)
        if not data["tag_name"]:
            click.echo('Aborting release due to empty tag name')
            return
    print_json(gh.release(gh.repository().releases.post(json=data)), verbose)
