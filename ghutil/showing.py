from   collections.abc import Iterator
import json
import click

def print_json(obj):
    if isinstance(obj, Iterator):
        obj = list(obj)
    click.echo(json.dumps(obj, sort_keys=True, indent=4, ensure_ascii=False))

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
    }

def gist_info(gist):
    return {
        "id": gist["id"],
        "url": gist["url"],
        "git_push_url": gist["git_push_url"],
        "files": gist["files"],
        "public": gist["public"],
    }
