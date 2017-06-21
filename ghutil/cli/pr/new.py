import click
from   ghutil.edit    import edit_as_mail
from   ghutil.showing import print_json, pr_info

@click.command()
@click.option('-b', '--body', type=click.File())
@click.option('-M', '--maintainer-can-modify', is_flag=True)
@click.option('-T', '--title')
@click.option('-v', '--verbose', is_flag=True)
@click.argument('source')
@click.argument('dest')
@click.pass_obj
def cli(gh, source, dest, title, body, maintainer_can_modify, verbose):
    """ Create a new pull request """

    src_repo, sep, src_branch = source.rpartition(':')
    if not sep:
        raise ValueError(source)  ##### TODO: Be more informative
    src_repo = gh.repository(src_repo)

    dest_repo, sep, dest_branch = dest.rpartition(':')
    if not sep:
        raise ValueError(dest)  ##### TODO: Be more informative
    dest_repo = gh.repository(dest_repo)

    data = {
        "title": title,
        "body": body.read() if body is not None else None,
        "maintainer_can_modify": maintainer_can_modify,
        "base": dest_branch,
    }
    if title is None or body is None:
        ### TODO: Also let the user edit the source & destination?
        data.update(edit_as_mail(data, 'title maintainer_can_modify', 'body'))
        if data["title"] is None:  # or body is None?
            click.echo('Aborting pull request due to empty title')
            return

    src_data = src_repo.get()
    if src_data["full_name"] == dest_repo.get()["full_name"]:
        data["head"] = src_branch
    else:
        ### TODO: Check that the repositories are in the same network?
        data["head"] = src_data["owner"]["login"] + ':' + src_branch

    print_json(pr_info(dest_repo.pulls.post(json=data), verbose))