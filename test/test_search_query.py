from shlex import split
import pytest
from ghutil.util import search_query


@pytest.mark.parametrize(
    "terms,query",
    [
        (split("label:Nice to Have"), "label:Nice to Have"),
        (split('label:"Nice to Have"'), 'label:"Nice to Have"'),
        (split("label:'Nice to Have'"), 'label:"Nice to Have"'),
        (split('"label:Nice to Have"'), 'label:"Nice to Have"'),
        (split("'label:Nice to Have'"), 'label:"Nice to Have"'),
        (split("'label:\"Nice to Have\"'"), 'label:"Nice to Have"'),
        (split("\"label:'Nice to Have'\""), "label:\"'Nice to Have'\""),
        (split("'\"label:Nice to Have\"'"), '"label:Nice to Have"'),
        (split("\"'label:Nice to Have'\""), "\"'label:Nice to Have'\""),
        (split("Nice to Have"), "Nice to Have"),
        (split('"Nice to Have"'), '"Nice to Have"'),
        (split("'Nice to Have'"), '"Nice to Have"'),
        (split("'\"Nice to Have\"'"), '"Nice to Have"'),
        (split("\"'Nice to Have'\""), "\"'Nice to Have'\""),
    ],
)
def test_search_query(terms, query):
    assert search_query(*terms) == query
