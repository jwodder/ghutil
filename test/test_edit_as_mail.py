from copy import deepcopy
import click

# from   headerparser import Error
import pytest
from ghutil.edit import edit_as_mail


@pytest.mark.parametrize(
    "obj,fields,bodyfield,edit_in,edit_out,ret",
    [
        (
            {"title": None, "labels": (), "body": None},
            "title labels",
            "body",
            "Title: \nLabels: \n\n",
            "Title: Testing\nLabels: test, editing\n\nThis is a message body.\n",
            {
                "title": "Testing",
                "labels": ["test", "editing"],
                "body": "This is a message body.\n",
            },
        ),
        (
            {"title": None, "labels": [], "body": None},
            "title labels",
            "body",
            "Title: \nLabels: \n\n",
            "Title: Testing\nLabels: test, editing\n\nThis is a message body.\n",
            {
                "title": "Testing",
                "labels": ["test", "editing"],
                "body": "This is a message body.\n",
            },
        ),
        (
            {"title": None, "labels": (), "body": None},
            "title labels",
            "body",
            "Title: \nLabels: \n\n",
            "Title: Testing\nLabels: one label\n\n",
            {"title": "Testing", "labels": ["one label"]},
        ),
        (
            {"title": None, "labels": (), "body": None},
            "title labels",
            "body",
            "Title: \nLabels: \n\n",
            "Title: Testing\nLabels: trailing comma, \n\n",
            {"title": "Testing", "labels": ["trailing comma"]},
        ),
        (
            {"title": None, "labels": (), "body": None},
            "title labels",
            "body",
            "Title: \nLabels: \n\n",
            "Title: Testing\nLabels:  \n  \n\n",
            {"title": "Testing"},
        ),
        (
            {"title": None, "labels": ("red", "green", "blue"), "body": None},
            "title labels",
            "body",
            "Title: \nLabels: red, green, blue\n\n",
            "Title: Testing\nLabels:  \n  \n\n",
            {"title": "Testing", "labels": []},
        ),
        (
            {"title": None, "labels": ["red", "green", "blue"], "body": None},
            "title labels",
            "body",
            "Title: \nLabels: red, green, blue\n\n",
            "Title: Testing\nLabels:  \n  \n\n",
            {"title": "Testing", "labels": []},
        ),
        (
            {"title": None, "labels": ("red", "green", "blue"), "body": None},
            "title labels",
            "body",
            "Title: \nLabels: red, green, blue\n\n",
            "Title: Testing\nLabels: blue, green, red\n\n",
            {"title": "Testing", "labels": ["blue", "green", "red"]},
        ),
        (
            {"title": None, "labels": (), "body": None},
            "title labels",
            "body",
            "Title: \nLabels: \n\n",
            None,
            None,
        ),
        (
            {"title": None, "labels": (), "body": None},
            "title labels",
            "body",
            "Title: \nLabels: \n\n",
            "Title: \nLabels: \n\n",
            {},
        ),
        (
            {"title": ""},
            "title",
            None,
            "Title: \n",
            "",
            {},
        ),
        pytest.param(
            {"title": ""},
            "title",
            None,
            "Title: \n",
            "\n",
            {},
            marks=pytest.mark.xfail(reason="TODO"),
        ),
        (
            {"title": "Title", "body": "Body"},
            "title",
            "body",
            "Title: Title\n\nBody",
            None,
            None,
        ),
        (
            {"title": "Title", "body": "Body"},
            "title",
            "body",
            "Title: Title\n\nBody",
            "Title: Title\n\nBody",
            {},
        ),
        (
            {"title": "Title", "body": "Body"},
            "title",
            "body",
            "Title: Title\n\nBody",
            "Title: New Title\n\nNew Body\n",
            {"title": "New Title", "body": "New Body\n"},
        ),
        (
            {"title": "Title", "body": "Body"},
            "title",
            "body",
            "Title: Title\n\nBody",
            "Title: Title\n\n",
            {"body": ""},
        ),
        (
            {"title": "Title", "body": "Body"},
            "title",
            "body",
            "Title: Title\n\nBody",
            "Title: Title\n",
            {},
        ),
        pytest.param(
            {"title": "Title", "body": "Body"},
            "title",
            "body",
            "Title: Title\n\nBody",
            "\n",
            {},
            marks=pytest.mark.xfail(reason="TODO"),
        ),
        (
            {"title": "Title", "body": "Body"},
            "title",
            "body",
            "Title: Title\n\nBody",
            "",
            {},
        ),
        (
            {"title": "Title", "body": "Body"},
            "title",
            "body",
            "Title: Title\n\nBody",
            "Title: Title\n\nBody\n",
            {"body": "Body\n"},
        ),
        (
            {"publish": False},
            "publish",
            None,
            "Publish: no\n",
            "Publish: yes\n",
            {"publish": True},
        ),
        (
            {"publish": False},
            "publish",
            None,
            "Publish: no\n",
            "Publish: false\n",
            {},
        ),
        (
            {"publish": None},
            "publish",
            None,
            "Publish: \n",
            "Publish: false\n",
            {"publish": "false"},
        ),
        (
            {"publish": False},
            "publish",
            None,
            "Publish: no\n",
            "",
            {},
        ),
        pytest.param(
            {"publish": False},
            "publish",
            None,
            "Publish: no\n",
            "\n",
            {},
            marks=pytest.mark.xfail(reason="TODO"),
        ),
        (
            {"publish": True},
            "publish",
            None,
            "Publish: yes\n",
            "",
            {},
        ),
        (
            {"title": "Title", "labels": ["red", "green"], "body": "Body"},
            None,
            None,
            "Body: Body\nLabels: red, green\nTitle: Title\n",
            None,
            None,
        ),
        (
            {"title": "Title", "labels": ["red", "green"], "body": "Body"},
            None,
            "body",
            "Labels: red, green\nTitle: Title\n\nBody",
            None,
            None,
        ),
    ],
)
def test_edit_as_mail(mocker, obj, fields, bodyfield, edit_in, edit_out, ret):
    mocker.patch("click.edit", return_value=edit_out)
    original_obj = deepcopy(obj)
    assert edit_as_mail(obj, fields, bodyfield) == ret
    assert obj == original_obj
    click.edit.assert_called_once_with(edit_in, require_save=True)
    if ret is not None:
        for k, v in ret.items():
            assert obj[k] != v


# `obj` contains extra fields
# some fields are changed, others aren't
# empty body vs. body that's just a newline
# header values that contain newlines

# Errors:
# - adding a body
# - adding a header
# - deleting header-body interstitial blank line
