import click
import pytest

LABELS='bug\nduplicate\nenhancement\nhelp wanted\ninvalid\nquestion\nwontfix\n'

@pytest.mark.usefixtures('test_repo')
def test_label(cmd):
    r = cmd('label')
    assert r.exit_code == 0
    assert r.output == LABELS

@pytest.mark.usefixtures('test_repo')
def test_label_list(cmd):
    r = cmd('label', 'list')
    assert r.exit_code == 0
    assert r.output == LABELS

def test_label_list_repo(cmd):
    r = cmd('label', 'list', '-R', 'jwodder/test')
    assert r.exit_code == 0
    assert r.output == LABELS

def test_label_list_repo_verbose(cmd):
    r = cmd('label', 'list', '-R', 'jwodder/test', '--verbose')
    assert r.exit_code == 0
    assert r.output == '''\
[
    {
        "color": "ee0701",
        "default": true,
        "id": 671704577,
        "name": "bug",
        "url": "https://api.github.com/repos/jwodder/test/labels/bug"
    },
    {
        "color": "cccccc",
        "default": true,
        "id": 671704578,
        "name": "duplicate",
        "url": "https://api.github.com/repos/jwodder/test/labels/duplicate"
    },
    {
        "color": "84b6eb",
        "default": true,
        "id": 671704579,
        "name": "enhancement",
        "url": "https://api.github.com/repos/jwodder/test/labels/enhancement"
    },
    {
        "color": "128A0C",
        "default": true,
        "id": 671704580,
        "name": "help wanted",
        "url": "https://api.github.com/repos/jwodder/test/labels/help%20wanted"
    },
    {
        "color": "e6e6e6",
        "default": true,
        "id": 671704581,
        "name": "invalid",
        "url": "https://api.github.com/repos/jwodder/test/labels/invalid"
    },
    {
        "color": "cc317c",
        "default": true,
        "id": 671704582,
        "name": "question",
        "url": "https://api.github.com/repos/jwodder/test/labels/question"
    },
    {
        "color": "ffffff",
        "default": true,
        "id": 671704583,
        "name": "wontfix",
        "url": "https://api.github.com/repos/jwodder/test/labels/wontfix"
    }
]
'''

def test_label_new(cmd):
    r = cmd('--debug', 'label', 'new', '-R', 'jwodder/test', 'Test Label', '#FF0000')
    assert r.exit_code == 0
    assert r.output == '''\
POST https://api.github.com/repos/jwodder/test/labels
{
    "color": "FF0000",
    "name": "Test Label"
}
{
    "color": "FF0000",
    "default": false,
    "id": 671710206,
    "name": "Test Label",
    "url": "https://api.github.com/repos/jwodder/test/labels/Test%20Label"
}
'''

def test_label_new_description(cmd):
    r = cmd(
        '--debug',
        'label', 'new', '-R', 'jwodder/test',
        'Test Label 2', '#FF0000',
        '-d', 'This label is a test.',
    )
    assert r.exit_code == 0
    assert r.output == '''\
POST https://api.github.com/repos/jwodder/test/labels
{
    "color": "FF0000",
    "description": "This label is a test.",
    "name": "Test Label 2"
}
{
    "color": "FF0000",
    "default": false,
    "description": "This label is a test.",
    "id": 1108950320,
    "name": "Test Label 2",
    "node_id": "MDU6TGFiZWwxMTA4OTUwMzIw",
    "url": "https://api.github.com/repos/jwodder/test/labels/Test%20Label%202"
}
'''

def test_label_delete(cmd):
    r = cmd('--debug', 'label', 'delete', '-R', 'jwodder/test', '-f', 'Test Label')
    assert r.exit_code == 0
    assert r.output == '''\
DELETE https://api.github.com/repos/jwodder/test/labels/Test%20Label
Label 'Test Label' deleted
'''

def test_label_edit_name(cmd):
    r = cmd('--debug', 'label', 'edit', '-R', 'jwodder/test', 'enhancement',
            '--name=Enhancement')
    assert r.exit_code == 0
    assert r.output == '''\
PATCH https://api.github.com/repos/jwodder/test/labels/enhancement
{
    "name": "Enhancement"
}
'''

def test_label_edit_description(cmd):
    r = cmd('--debug', 'label', 'edit', '-R', 'jwodder/test', 'enhancement',
            '--description=Not to be confused with "enchantment"')
    assert r.exit_code == 0
    assert r.output == '''\
PATCH https://api.github.com/repos/jwodder/test/labels/enhancement
{
    "description": "Not to be confused with \\"enchantment\\""
}
'''

def test_label_edit_name_editor(cmd, mocker):
    mocker.patch('click.edit', return_value="Name: Won't Fix\nColor: ffffff\n")
    r = cmd('--debug', 'label', 'edit', '-R', 'jwodder/test', 'wontfix')
    assert r.exit_code == 0, r.output
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/labels/wontfix
PATCH https://api.github.com/repos/jwodder/test/labels/wontfix
{
    "name": "Won't Fix"
}
'''
    click.edit.assert_called_once_with(
        "Name: wontfix\n"
        "Color: ffffff\n"
        "Description: This will not be worked on\n",
        require_save=True,
    )

def test_label_edit_color_editor(cmd, mocker):
    mocker.patch('click.edit', return_value="Name: invalid\nColor: #000000\n")
    r = cmd('--debug', 'label', 'edit', '-R', 'jwodder/test', 'invalid')
    assert r.exit_code == 0, r.output
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/labels/invalid
PATCH https://api.github.com/repos/jwodder/test/labels/invalid
{
    "color": "000000"
}
'''
    click.edit.assert_called_once_with(
        "Name: invalid\nColor: e4e669\nDescription: This doesn't seem right\n",
        require_save=True,
    )

def test_label_edit_nop_editor(cmd, mocker):
    mocker.patch('click.edit', return_value="Color: cfd3d7\nName: duplicate\n")
    r = cmd('--debug', 'label', 'edit', '-R', 'jwodder/test', 'duplicate')
    assert r.exit_code == 0, r.output
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/labels/duplicate
No modifications made; exiting
'''
    click.edit.assert_called_once_with(
        "Name: duplicate\n"
        "Color: cfd3d7\n"
        "Description: This issue or pull request already exists\n",
        require_save=True,
    )

# operating on labels with slashes in their names
# editing a label's color on the command line
# editing a label's description in the editor
