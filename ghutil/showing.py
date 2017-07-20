from   collections.abc import Iterator
import json
from   operator        import itemgetter
import click

def print_json(obj, err=False):
    if isinstance(obj, Iterator):
        obj = list(obj)
    click.echo(json.dumps(obj, sort_keys=True, indent=4, ensure_ascii=False),
               err=err)

def show_fields(*fields):
    def show(obj, verbose=False):
        if verbose:
            return obj
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
                if not callable(sp):
                    sp = itemgetter(sp)
                if value is None:
                    break
                elif isinstance(value, list):
                    value = [v and sp(v) for v in value]
                else:
                    value = sp(value)
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
    "topics",
    ("license", "spdx_id"),
)

gist_info = show_fields(
    "id",
    "url",
    "git_pull_url",
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
    "comments",
    ("fork_of", "id"),
    ("forks", "id"),
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
    ("reactions", lambda react: {
        k:v for k,v in react.items() if k not in ('total_count', 'url') and v
    })
)

show_pr_repo = show_fields(
    "label",
    "ref",
    ("repo", "full_name"),
    "sha",
    ("user", "login"),
)

pr_info = show_fields(
    ("assignees", "login"),
    ("user", "login"),
    "title",
    "html_url",
    "id",
    "issue_url",
    "locked",
    "maintainer_can_modify",
    "changed_files",
    "closed_at",
    "comments",
    "commits",
    "additions",
    "deletions",
    "created_at",
    "diff_url",
    "milestone",
    "number",
    "updated_at",
    "url",
    "patch_url",
    "rebaseable",
    "review_comments",
    "state",
    ("base", show_pr_repo),
    ("head", show_pr_repo),
    "mergeable",
    "mergeable_state",
    "merged",
    "merged_at",
    "merge_commit_sha",
    ("merged_by", "login"),
    ("requested_reviewers", "login"),  ### Double-check this one
)

release_info = show_fields(
    "id",
    "name",
    "tag_name",
    ("author", "login"),
    "prerelease",
    "published_at",
    "created_at",
    "draft",
    "target_commitish",
    "html_url",
    "url",
    "tarball_url",
    "zipball_url",
    ("assets", show_fields(
        "browser_download_url",
        "content_type",
        "created_at",
        "download_count",
        "id",
        "label",
        "name",
        "size",
        "state",
        "updated_at",
        ("uploader", "login"),
        "url",
    )),
)
