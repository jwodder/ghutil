import pytest
from   ghutil.types import Repository

REPO_URLS = [
    (
        'git://github.com/jwodder/headerparser',
        {"owner": "jwodder", "repo": "headerparser"},
    ),
    (
        'git://github.com/jwodder/headerparser.git',
        {"owner": "jwodder", "repo": "headerparser"},
    ),
    (
        'git@github.com:jwodder/headerparser',
        {"owner": "jwodder", "repo": "headerparser"},
    ),
    (
        'git@github.com:jwodder/headerparser.git',
        {"owner": "jwodder", "repo": "headerparser"},
    ),
    (
        'https://api.github.com/repos/jwodder/headerparser',
        {"owner": "jwodder", "repo": "headerparser"},
    ),
    (
        'https://github.com/jwodder/headerparser',
        {"owner": "jwodder", "repo": "headerparser"},
    ),
    (
        'https://github.com/jwodder/headerparser.git',
        {"owner": "jwodder", "repo": "headerparser"},
    ),
]

@pytest.mark.parametrize('arg,params', REPO_URLS + [
    ('jwodder/headerparser', {"owner": "jwodder", "repo": "headerparser"}),
    ('headerparser', {"owner": None, "repo": "headerparser"}),
])
def test_parse_arg(arg, params):
    assert Repository.parse_arg(arg) == params

@pytest.mark.parametrize('url,params', REPO_URLS)
def test_parse_url(url, params):
    assert Repository.parse_url(url) == params

# TODO: Test parsing bad repository args/URLs
