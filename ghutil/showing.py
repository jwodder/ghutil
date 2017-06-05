from   collections.abc import Iterator
import json
import click

def print_json(obj, err=False):
    if isinstance(obj, Iterator):
        obj = list(obj)
    click.echo(json.dumps(obj, sort_keys=True, indent=4, ensure_ascii=False),
               err=err)

def show_fields(*fields):
    def show(obj):
        about = {}
        for entry in fields:
            if isinstance(entry, str):
                entry = (entry,)
            name, *subpath = entry
            try:
                value = obj[name]
            except KeyError:
                continue
            for sp in subpath:
                if value is None:
                    break
                elif callable(sp):
                    value = sp(value)
                elif isinstance(value, list):
                    value = [v and v[sp] for v in value]
                else:
                    value = value[sp]
            about[name] = value
        return about
    return show

repo_info = show_fields(
    ("owner", "login"),
    "name",
    "url",
    "html_url",
    "clone_url",
    "git_url",
    "ssh_url",
    "full_name",
    "description",
    "homepage",
    "private",
    "default_branch",
    "created_at",
    "updated_at",
    "pushed_at",
    "fork",
    "forks_count",
    "watchers_count",
    "size",
    "subscribers_count",
    "stargazers_count",
    "id",
    "language",
    "network_count",
    "open_issues_count",
    ("parent", "full_name"),
    ("source", "full_name"),
)

gist_info = show_fields(
    "id",
    "url",
    "git_push_url",
    ("files", lambda files: {
        fname: {k:v for k,v in about.items() if k != 'content'}
        for fname, about in files.items()
    }),
    "public",
    "html_url",
    ("owner", "login"),
    "description",
    "created_at",
    "updated_at",
)

issue_info = show_fields(
    ("assignees", "login"),
    "closed_at",
    ("closed_by", "login"),
    "comments",
    "created_at",
    "html_url",
    "id",
    ("labels", "name"),
    "locked",
    ("milestone", "title"),
    "number",
    "state",
    "title",
    "updated_at",
    "url",
    ("user", "login"),
    "repository_url",
    ### pull_request
)
