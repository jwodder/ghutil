from   collections.abc import Iterator
from   inspect         import signature
import json
from   operator        import itemgetter
import click

def print_json(obj, verbose=False, err=False):
    def default(obj):
        if hasattr(obj, 'for_json'):
            if 'verbose' in signature(obj.for_json).parameters:
                return obj.for_json(verbose=verbose)
            else:
                return obj.for_json()
        elif isinstance(obj, Iterator):
            return list(obj)
        else:
            try:
                data = vars(obj).copy()
            except TypeError:
                data = {"__repr__": repr(obj)}
            data["__class__"] = type(obj).__name__
            return data
    click.echo(
        json.dumps(obj, sort_keys=True, indent=4, ensure_ascii=False,
                        default=default),
        err=err,
    )

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
    "body",
)

comment_info = show_fields(
    "body",
    "created_at",
    "html_url",
    "id",
    ("reactions", lambda react: {
        k:v for k,v in react.items()
            if k not in ('total_count', 'url') and v
    }),
    "url",
    ("user", "login"),
    "updated_at",
)
