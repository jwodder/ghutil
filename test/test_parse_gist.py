import pytest
from ghutil.types import Gist

GIST_URLS = [
    (
        "https://gist.github.com/4bf350e2d72b547b22dc9de52148ccbe",
        {"id": "4bf350e2d72b547b22dc9de52148ccbe"},
    ),
    (
        "https://gist.github.com/4bf350e2d72b547b22dc9de52148ccbe.git",
        {"id": "4bf350e2d72b547b22dc9de52148ccbe"},
    ),
    ("https://gist.github.com/42", {"id": "42"}),
    (
        "gist.github.com/4bf350e2d72b547b22dc9de52148ccbe",
        {"id": "4bf350e2d72b547b22dc9de52148ccbe"},
    ),
    (
        "http://gist.github.com/4bf350e2d72b547b22dc9de52148ccbe",
        {"id": "4bf350e2d72b547b22dc9de52148ccbe"},
    ),
    (
        "https://api.github.com/gists/4bf350e2d72b547b22dc9de52148ccbe",
        {"id": "4bf350e2d72b547b22dc9de52148ccbe"},
    ),
    (
        "git@gist.github.com:4bf350e2d72b547b22dc9de52148ccbe.git",
        {"id": "4bf350e2d72b547b22dc9de52148ccbe"},
    ),
    (
        "git@github.com:4bf350e2d72b547b22dc9de52148ccbe.git",
        {"id": "4bf350e2d72b547b22dc9de52148ccbe"},
    ),
    (
        "https://gist.github.com/jwodder/4bf350e2d72b547b22dc9de52148ccbe",
        {"id": "4bf350e2d72b547b22dc9de52148ccbe"},
    ),
    (
        "https://gist.github.com/42/4bf350e2d72b547b22dc9de52148ccbe",
        {"id": "4bf350e2d72b547b22dc9de52148ccbe"},
    ),
]

BAD_GISTS = [
    "https://gist.github.com/",
    "https://github.com/4bf350e2d72b547b22dc9de52148ccbe",
    "https://github.com/jwodder/4bf350e2d72b547b22dc9de52148ccbe",
    "git@gist.github.com:jwodder/4bf350e2d72b547b22dc9de52148ccbe.git",
    "git@github.com:jwodder/4bf350e2d72b547b22dc9de52148ccbe.git",
]


@pytest.mark.parametrize("arg,result", GIST_URLS + [])
def test_parse_gist_arg(arg, result):
    assert Gist.parse_arg(arg) == result


@pytest.mark.parametrize("arg", BAD_GISTS)
def test_parse_bad_gist_arg(arg):
    with pytest.raises(ValueError):
        Gist.parse_arg(arg)


@pytest.mark.parametrize("url,result", GIST_URLS)
def test_parse_gist_url(url, result):
    assert Gist.parse_url(url) == result


@pytest.mark.parametrize("url", BAD_GISTS)
def test_parse_bad_gist_url(url):
    with pytest.raises(ValueError):
        Gist.parse_url(url)
