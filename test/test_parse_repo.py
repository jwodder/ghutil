import pytest
from ghutil.types import Repository

REPO_URLS = [
    (
        "git://github.com/jwodder/headerparser",
        {"owner": "jwodder", "repo": "headerparser"},
    ),
    (
        "git://github.com/jwodder/headerparser.git",
        {"owner": "jwodder", "repo": "headerparser"},
    ),
    (
        "git@github.com:jwodder/headerparser",
        {"owner": "jwodder", "repo": "headerparser"},
    ),
    (
        "git@github.com:jwodder/headerparser.git",
        {"owner": "jwodder", "repo": "headerparser"},
    ),
    (
        "https://api.github.com/repos/jwodder/headerparser",
        {"owner": "jwodder", "repo": "headerparser"},
    ),
    (
        "https://github.com/jwodder/headerparser",
        {"owner": "jwodder", "repo": "headerparser"},
    ),
    (
        "https://github.com/jwodder/headerparser.git",
        {"owner": "jwodder", "repo": "headerparser"},
    ),
    (
        "https://www.github.com/jwodder/headerparser",
        {"owner": "jwodder", "repo": "headerparser"},
    ),
    (
        "http://github.com/jwodder/headerparser",
        {"owner": "jwodder", "repo": "headerparser"},
    ),
    (
        "http://www.github.com/jwodder/headerparser",
        {"owner": "jwodder", "repo": "headerparser"},
    ),
    (
        "github.com/jwodder/headerparser",
        {"owner": "jwodder", "repo": "headerparser"},
    ),
    (
        "www.github.com/jwodder/headerparser",
        {"owner": "jwodder", "repo": "headerparser"},
    ),
    (
        "https://github.com/jwodder/none.git",
        {"owner": "jwodder", "repo": "none"},
    ),
]

BAD_REPOS = [
    "https://github.com/none/headerparser.git",
    "none/repo",
    "jwodder/headerparser.git",
    "jwodder/",
]


@pytest.mark.parametrize(
    "arg,params",
    REPO_URLS
    + [
        ("jwodder/headerparser", {"owner": "jwodder", "repo": "headerparser"}),
        ("headerparser", {"owner": None, "repo": "headerparser"}),
        ("jwodder/none", {"owner": "jwodder", "repo": "none"}),
        ("none", {"owner": None, "repo": "none"}),
        ("nonely/headerparser", {"owner": "nonely", "repo": "headerparser"}),
        ("none-none/headerparser", {"owner": "none-none", "repo": "headerparser"}),
        ("nonenone/headerparser", {"owner": "nonenone", "repo": "headerparser"}),
    ],
)
def test_parse_arg(arg, params):
    assert Repository.parse_arg(arg) == params


@pytest.mark.parametrize("arg", BAD_REPOS)
def test_parse_bad_repo_arg(arg):
    with pytest.raises(ValueError):
        Repository.parse_arg(arg)


@pytest.mark.parametrize("url,params", REPO_URLS)
def test_parse_url(url, params):
    assert Repository.parse_url(url) == params


@pytest.mark.parametrize("url", BAD_REPOS)
def test_parse_bad_repo_url(url):
    with pytest.raises(ValueError):
        Repository.parse_url(url)


# TODO: Test parsing more bad repository args/URLs
