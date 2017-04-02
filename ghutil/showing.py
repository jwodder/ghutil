from   collections.abc import Iterator
import json
import click

def print_json(obj, err=False):
    if isinstance(obj, Iterator):
        obj = list(obj)
    click.echo(json.dumps(obj, sort_keys=True, indent=4, ensure_ascii=False),
               err=err)

def repo_info(repo):
    return {
        "owner": repo["owner"]["login"],
        "name": repo["name"],
        "url": repo["url"],
        "html_url": repo["html_url"],
        "clone_url": repo["clone_url"],
        "git_url": repo["git_url"],
        "ssh_url": repo["ssh_url"],
        "full_name": repo["full_name"],
        "description": repo["description"],
        "homepage": repo["homepage"],
        "private": repo["private"],
        "default_branch": repo["default_branch"],
        "created_at": repo["created_at"],
        "updated_at": repo["updated_at"],
        "pushed_at": repo["pushed_at"],
    }

def gist_info(gist):
    return {
        "id": gist["id"],
        "url": gist["url"],
        "git_push_url": gist["git_push_url"],
        "files": {
            fname: {k:v for k,v in about.items() if k != 'content'}
            for fname, about in gist["files"].items()
        },
        "public": gist["public"],
        "html_url": gist["html_url"],
        "owner": gist["owner"]["login"],
        "description": gist["description"],
        "created_at": gist["created_at"],
        "updated_at": gist["updated_at"],
    }
