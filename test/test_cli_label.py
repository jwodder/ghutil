import click

def test_label(cmd):
    r = cmd('label')
    assert r.exit_code == 0
    assert r.output == '''\
bug
duplicate
enhancement
help wanted
invalid
Nice to Have
question
wontfix
'''

def test_label_list(cmd):
    r = cmd('label', 'list')
    assert r.exit_code == 0
    assert r.output == '''\
bug
duplicate
enhancement
help wanted
invalid
Nice to Have
question
wontfix
'''

def test_label_list_repo(cmd):
    r = cmd('label', 'list', '-R', 'jwodder/test')
    assert r.exit_code == 0
    assert r.output == '''\
bug
duplicate
enhancement
help wanted
invalid
question
wontfix
'''

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

def test_label_edit_name_editor(cmd, mocker):
    mocker.patch('click.edit', return_value="Name: Won't Fix\nColor: ffffff\n")
    r = cmd('--debug', 'label', 'edit', '-R', 'jwodder/test', 'wontfix')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/labels/wontfix
PATCH https://api.github.com/repos/jwodder/test/labels/wontfix
{
    "name": "Won't Fix"
}
'''
    click.edit.assert_called_once_with(
        "Name: wontfix\nColor: ffffff\n",
        require_save=True,
    )

def test_label_edit_color_editor(cmd, mocker):
    mocker.patch('click.edit', return_value="Name: invalid\nColor: #000000\n")
    r = cmd('--debug', 'label', 'edit', '-R', 'jwodder/test', 'invalid')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/labels/invalid
PATCH https://api.github.com/repos/jwodder/test/labels/invalid
{
    "color": "000000"
}
'''
    click.edit.assert_called_once_with(
        "Name: invalid\nColor: e6e6e6\n",
        require_save=True,
    )

def test_label_edit_nop_editor(cmd, mocker):
    mocker.patch('click.edit', return_value="Color: cccccc\nName: duplicate\n")
    r = cmd('--debug', 'label', 'edit', '-R', 'jwodder/test', 'duplicate')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/labels/duplicate
No modifications made; exiting
'''
    click.edit.assert_called_once_with(
        "Name: duplicate\nColor: cccccc\n",
        require_save=True,
    )

#gh label edit -R test ???
#  - change name in CLI
#  - change color in CLI
#  - change name in editor
#  - change color in editor
#  - change both in CLI
#  - change both in editor
