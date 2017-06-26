import pytest
import ghutil.issues
from   ghutil.issues import parse_issue_spec, parse_issue_url

ISSUE_URLS = [
    (
        'https://github.com/jwodder/headerparser/pull/1',
        ('jwodder', 'headerparser', 1),
    ),
    (
        'https://api.github.com/repos/jwodder/headerparser/pulls/1',
        ('jwodder', 'headerparser', 1),
    ),
    (
        'https://github.com/jwodder/headerparser/issues/1',
        ('jwodder', 'headerparser', 1),
    ),
    (
        'https://api.github.com/repos/jwodder/headerparser/issues/1',
        ('jwodder', 'headerparser', 1),
    ),
]

BAD_URLS = [
    'https://github.com/jwodder/headerparser/pulls/1',
    'https://api.github.com/repos/jwodder/headerparser/pull/1',
    'https://github.com/jwodder/headerparser/issue/1',
    'https://api.github.com/repos/jwodder/headerparser/issue/1',
    'jwodder/headerparser',
]

@pytest.mark.parametrize('spec,result', ISSUE_URLS + [
    ('jwodder/headerparser/1', ('jwodder', 'headerparser', 1)),
    ('jwodder/headerparser#1', ('jwodder', 'headerparser', 1)),
    ('headerparser/1',         (None, 'headerparser', 1)),
    ('headerparser#1',         (None, 'headerparser', 1)),
])
def test_parse_issue_spec(spec, result):
    assert parse_issue_spec(spec) == result

@pytest.mark.parametrize('spec', BAD_URLS)
def test_parse_bad_issue_spec(spec):
    with pytest.raises(ValueError):
        parse_issue_url(spec)

def test_parse_issue_num(mocker):
    mocker.patch(
        'ghutil.issues.get_remote_url',
        return_value='https://github.com/jwodder/headerparser',
    )
    assert parse_issue_spec('42') == ('jwodder', 'headerparser', 42)
    assert ghutil.issues.get_remote_url.called_once_with()

@pytest.mark.parametrize('url,result', ISSUE_URLS)
def test_parse_issue_url(url, result):
    assert parse_issue_url(url) == result

@pytest.mark.parametrize('url', BAD_URLS)
def test_parse_bad_issue_url(url):
    with pytest.raises(ValueError):
        parse_issue_url(url)
