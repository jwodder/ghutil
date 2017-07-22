import pytest
from   ghutil.types import Issue

ISSUE_URLS = [
    (
        'https://github.com/jwodder/headerparser/pull/1',
        {"owner": "jwodder", "repo": "headerparser", "number": 1},
    ),
    (
        'https://api.github.com/repos/jwodder/headerparser/pulls/1',
        {"owner": "jwodder", "repo": "headerparser", "number": 1},
    ),
    (
        'https://github.com/jwodder/headerparser/issues/1',
        {"owner": "jwodder", "repo": "headerparser", "number": 1},
    ),
    (
        'https://api.github.com/repos/jwodder/headerparser/issues/1',
        {"owner": "jwodder", "repo": "headerparser", "number": 1},
    ),
]

BAD_ISSUES = [
    'https://github.com/jwodder/headerparser/pulls/1',
    'https://api.github.com/repos/jwodder/headerparser/pull/1',
    'https://github.com/jwodder/headerparser/issue/1',
    'https://api.github.com/repos/jwodder/headerparser/issue/1',
    'jwodder/headerparser',
    '#1',
    '/1',
]

@pytest.mark.parametrize('arg,result', ISSUE_URLS + [
    (
        'jwodder/headerparser/1',
        {"owner": "jwodder", "repo": "headerparser", "number": 1},
    ),
    (
        'jwodder/headerparser#1',
        {"owner": "jwodder", "repo": "headerparser", "number": 1},
    ),
    ('headerparser/1', {"owner": None, "repo": "headerparser", "number": 1}),
    ('headerparser#1', {"owner": None, "repo": "headerparser", "number": 1}),
    ('42', {"owner": None, "repo": None, "number": 42}),
])
def test_parse_issue_arg(arg, result):
    assert Issue.parse_arg(arg) == result

@pytest.mark.parametrize('arg', BAD_ISSUES)
def test_parse_bad_issue_arg(arg):
    with pytest.raises(ValueError):
        Issue.parse_arg(arg)

@pytest.mark.parametrize('url,result', ISSUE_URLS)
def test_parse_issue_url(url, result):
    assert Issue.parse_url(url) == result

@pytest.mark.parametrize('url', BAD_ISSUES)
def test_parse_bad_issue_url(url):
    with pytest.raises(ValueError):
        Issue.parse_url(url)
