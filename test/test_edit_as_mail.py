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
])
def test_edit_as_mail(mocker, obj, fields, bodyfield, edit_in, edit_out, ret):
    mocker.patch('click.edit', return_value=edit_out)
    assert edit_as_mail(obj, fields, bodyfield) == ret
    assert click.edit.called_once_with(edit_in)

# boolean field
# deleting a field
# deleting the body
# leaving the body empty
# adding a body
# non-empty input field
# leaving a non-empty input field as-is
# non-empty input body
# deleting header-body interstitial blank line
# `fields` is None
# no body
# `obj` contains extra fields
# some fields are changed, others aren't
# list field filled in with whitespace
# list field filled with a single item (no commas)
# list field with trailing comma?
# leaving a boolean field blank
