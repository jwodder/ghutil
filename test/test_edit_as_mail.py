import click
#from   headerparser import Error
import pytest
from   ghutil.edit import edit_as_mail

@pytest.mark.parametrize('obj,fields,bodyfield,edit_in,edit_out,ret', [
    (
        {"title": None, "labels": (), "body": None},
        "title labels",
        "body",
        "Title: \nLabels: \n\n",
        "Title: Testing\nLabels: test, editing\n\nThis is a message body.\n",
        {"title": "Testing", "labels": ["test", "editing"], "body": "This is a message body.\n"},
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
        {"title": None, "labels": ('red', 'green', 'blue'), "body": None},
        "title labels",
        "body",
        "Title: \nLabels: red, green, blue\n\n",
        "Title: Testing\nLabels:  \n  \n\n",
        {"title": "Testing", "labels": []},
    ),

    (
        {"title": None, "labels": ('red', 'green', 'blue'), "body": None},
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
        {},
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
        {"title": ''},
        "title",
        None,
        "Title: \n",
        "",
        {},
    ),

    pytest.param(
        {"title": ''},
        "title",
        None,
        "Title: \n",
        "\n",
        {},
        marks=pytest.mark.xfail(reason='TODO'),
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
        {'publish': 'false'},
    ),

    (
        {"publish": False},
        "publish",
        None,
        "Publish: no\n",
        "",
        {},
    ),

    (
        {"publish": True},
        "publish",
        None,
        "Publish: yes\n",
        "",
        {},
    ),

])
def test_edit_as_mail(mocker, obj, fields, bodyfield, edit_in, edit_out, ret):
    mocker.patch('click.edit', return_value=edit_out)
    assert edit_as_mail(obj, fields, bodyfield) == ret
    click.edit.assert_called_once_with(edit_in)

# deleting the body
# non-empty input field
# leaving a non-empty input field as-is
# non-empty input body
# `fields` is None
# no body
# `obj` contains extra fields
# some fields are changed, others aren't
# empty body vs. body that's just a newline
# assert that `obj` is never modified

# Errors:
# - adding a body
# - adding a header
# - deleting header-body interstitial blank line
