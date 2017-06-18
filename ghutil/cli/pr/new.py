import click
from   ghutil.showing import print_json

@click.command()
@click.option('-b', '--body', type=click.File())
@click.option('-M', '--maintainer-can-modify', is_flag=True)
@click.option('-T', '--title')
#@click.option('-v', '--verbose', is_flag=True)
@click.argument('source')
@click.argument('dest')
@click.pass_obj
def cli(gh, source, dest, title, body, maintainer_can_modify):
    """ Create a new pull request """

    src_repo, sep, src_branch = source.rpartition(':')
    if not sep:
        raise ValueError(source)  #####
    src_repo = gh.repository(src_repo)

    dest_repo, sep, dest_branch = dest.rpartition(':')
    if not sep:
        raise ValueError(dest)  #####
    dest_repo = gh.repository(dest_repo)

    ### TODO: Open editor if either title or body is absent
    data = {
        "title": title,
        "body": body.read() if body is not None else None,
        "maintainer_can_modify": maintainer_can_modify,
        "base": dest_branch,
    }
    src_data = src_repo.get()

    if src_data["full_name"] == dest_repo.get()["full_name"]:
        data["head"] = src_branch
    else:
        ### Check that the repositories are in the same network?
        data["head"] = src_data["owner"]["login"] + ':' + src_branch

    print_json(dest_repo.pulls.post(json=data))  #### Show only selected fields
