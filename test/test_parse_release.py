import pytest
from ghutil.types import Release

RELEASE_URLS = [
    (
        "https://api.github.com/repos/jwodder/headerparser/releases/1",
        {"owner": "jwodder", "repo": "headerparser", "id": 1, "tag_name": None},
    ),
    (
        "https://api.github.com/repos/jwodder/headerparser/releases/latest",
        {"owner": "jwodder", "repo": "headerparser", "id": None, "tag_name": None},
    ),
    (
        "https://api.github.com/repos/jwodder/headerparser/releases/tags/v0.1.0",
        {"owner": "jwodder", "repo": "headerparser", "id": None, "tag_name": "v0.1.0"},
    ),
    (
        "https://api.github.com/repos/jwodder/headerparser/releases/tags/latest",
        {"owner": "jwodder", "repo": "headerparser", "id": None, "tag_name": "latest"},
    ),
    (
        "https://api.github.com/repos/jwodder/headerparser/releases/tags/1",
        {"owner": "jwodder", "repo": "headerparser", "id": None, "tag_name": "1"},
    ),
    (
        "https://github.com/jwodder/headerparser/releases/v0.1.0",
        {"owner": "jwodder", "repo": "headerparser", "tag_name": "v0.1.0"},
    ),
    (
        "https://github.com/jwodder/headerparser/releases/1",
        {"owner": "jwodder", "repo": "headerparser", "tag_name": "1"},
    ),
    (
        "https://github.com/jwodder/headerparser/releases/latest",
        {"owner": "jwodder", "repo": "headerparser", "tag_name": None},
    ),
    (
        "https://github.com/jwodder/headerparser/releases/tag/v0.1.0",
        {"owner": "jwodder", "repo": "headerparser", "tag_name": "v0.1.0"},
    ),
    (
        "https://github.com/jwodder/headerparser/releases/tag/1",
        {"owner": "jwodder", "repo": "headerparser", "tag_name": "1"},
    ),
    (
        "https://github.com/jwodder/headerparser/releases/tag/latest",
        {"owner": "jwodder", "repo": "headerparser", "tag_name": "latest"},
    ),
]

BAD_RELEASES = [
    "https://api.github.com/repos/jwodder/headerparser/releases/v0.1.0",
    "https://api.github.com/repos/jwodder/headerparser/releases/tags/@",
    "https://github.com/jwodder/headerparser/releases/@",
    "https://github.com/jwodder/headerparser/releases/@/",
    ":jwodder/headerparser:v0.1.0",
]


@pytest.mark.parametrize(
    "arg,result",
    RELEASE_URLS
    + [
        (
            "jwodder/headerparser:1",
            {"owner": "jwodder", "repo": "headerparser", "tag_name": "1"},
        ),
        (
            "jwodder/headerparser:v0.1.0",
            {"owner": "jwodder", "repo": "headerparser", "tag_name": "v0.1.0"},
        ),
        (
            "headerparser:v0.1.0",
            {"owner": None, "repo": "headerparser", "tag_name": "v0.1.0"},
        ),
        (
            "jwodder/headerparser:",
            {"owner": "jwodder", "repo": "headerparser"},
        ),
        (
            "headerparser:",
            {"owner": None, "repo": "headerparser"},
        ),
        ("v0.1.0", {"owner": None, "repo": None, "tag_name": "v0.1.0"}),
        (":v0.1.0", {"owner": None, "repo": None, "tag_name": "v0.1.0"}),
        (
            "jwodder/headerparser",
            {"owner": None, "repo": None, "tag_name": "jwodder/headerparser"},
        ),
        (
            ":jwodder/headerparser",
            {"owner": None, "repo": None, "tag_name": "jwodder/headerparser"},
        ),
        ("latest", {"owner": None, "repo": None, "tag_name": None}),
        (":latest", {"owner": None, "repo": None, "tag_name": "latest"}),
    ],
)
def test_parse_release_arg(arg, result):
    assert Release.parse_arg(arg) == result


@pytest.mark.parametrize("arg", BAD_RELEASES)
def test_parse_bad_release_arg(arg):
    with pytest.raises(ValueError):
        Release.parse_arg(arg)


@pytest.mark.parametrize("url,result", RELEASE_URLS)
def test_parse_release_url(url, result):
    assert Release.parse_url(url) == result


@pytest.mark.parametrize("url", BAD_RELEASES)
def test_parse_bad_release_url(url):
    with pytest.raises(ValueError):
        Release.parse_url(url)


# TODO: Test parsing more bad release args/URLs
