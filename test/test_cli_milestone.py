import click
import pytest

def test_milestone_empty(cmd):
    r = cmd('milestone', 'list', '-R', 'jwodder/ghutil')
    assert r.exit_code == 0
    assert r.output == ''

@pytest.mark.usefixtures('test_repo')
def test_milestone(cmd):
    r = cmd('milestone')
    assert r.exit_code == 0
    assert r.output == 'v1.0\n'

@pytest.mark.usefixtures('test_repo')
def test_milestone_list(cmd):
    r = cmd('milestone', 'list')
    assert r.exit_code == 0
    assert r.output == 'v1.0\n'

def test_milestone_list_repo(cmd):
    r = cmd('milestone', 'list', '-R', 'jwodder/test')
    assert r.exit_code == 0
    assert r.output == 'v1.0\n'

def test_milestone_new(cmd):
    r = cmd(
        'milestone', 'new',
        '-R', 'jwodder/test',
        '-d', 'Test all the milestones',
        'Test milestone',
        '--due', '2038-01-19T03:14:08Z',
        '--open',
    )
    assert r.exit_code == 0
    assert r.output == '''\
{
    "closed_at": null,
    "closed_issues": 0,
    "created_at": "2017-08-27T18:49:18Z",
    "creator": "jwodder",
    "description": "Test all the milestones",
    "due_on": "2038-01-18T08:00:00Z",
    "html_url": "https://github.com/jwodder/test/milestone/2",
    "id": 2725405,
    "number": 2,
    "open_issues": 0,
    "state": "open",
    "title": "Test milestone",
    "updated_at": "2017-08-27T18:49:18Z",
    "url": "https://api.github.com/repos/jwodder/test/milestones/2"
}
'''

def test_milestone_edit_title(cmd):
    r = cmd('--debug', 'milestone', 'edit', '-R', 'jwodder/test',
            'Test milestone', '--title=Test')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/milestones?state=all
PATCH https://api.github.com/repos/jwodder/test/milestones/2
{
    "title": "Test"
}
'''

def test_milestone_edit_title_by_number(cmd):
    r = cmd('--debug', 'milestone', 'edit', '-R', 'jwodder/test',
            'https://github.com/jwodder/test/milestone/2',
            '--title=Test Milestone')
    assert r.exit_code == 0
    assert r.output == '''\
PATCH https://api.github.com/repos/jwodder/test/milestones/2
{
    "title": "Test Milestone"
}
'''

def test_milestone_edit_title_editor(cmd, mocker):
    mocker.patch('click.edit', return_value='Title: Test')
    r = cmd('--debug', 'milestone', 'edit', '-R', 'jwodder/test',
            'Test milestone')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/milestones?state=all
PATCH https://api.github.com/repos/jwodder/test/milestones/2
{
    "title": "Test"
}
'''
    click.edit.assert_called_once_with(
        'Title: Test milestone\n'
        'Description: Test all the milestones\n'
        'Open: yes\n'
        'Due-On: 2038-01-18T08:00:00Z\n',
        require_save=True,
    )

def test_milestone_edit_nop_editor(cmd, mocker):
    mocker.patch('click.edit', return_value='')
    r = cmd('--debug', 'milestone', 'edit', '-R', 'jwodder/test',
            'Test Milestone')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/milestones?state=all
No modifications made; exiting
'''
    click.edit.assert_called_once_with(
        'Title: Test Milestone\n'
        'Description: Test all the milestones\n'
        'Open: yes\n'
        'Due-On: 2038-01-18T08:00:00Z\n',
        require_save=True,
    )

def test_milestone_edit_unset_due_date(cmd):
    r = cmd('--debug', 'milestone', 'edit', '-R', 'jwodder/test',
            'Test Milestone', '--due=')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/milestones?state=all
PATCH https://api.github.com/repos/jwodder/test/milestones/2
{
    "due_on": null
}
'''

def test_milestone_edit_unset_due_date_editor(cmd, mocker):
    mocker.patch('click.edit', return_value='Due-On:')
    r = cmd('--debug', 'milestone', 'edit', '-R', 'jwodder/test',
            'Test Milestone')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/milestones?state=all
PATCH https://api.github.com/repos/jwodder/test/milestones/2
{
    "due_on": null
}
'''
    click.edit.assert_called_once_with(
        'Title: Test Milestone\n'
        'Description: Test all the milestones\n'
        'Open: yes\n'
        'Due-On: 2038-01-18T08:00:00Z\n',
        require_save=True,
    )

def test_milestone_edit_open(cmd):
    r = cmd('--debug', 'milestone', 'edit', '--open', '-R', 'jwodder/test',
            'Test Milestone')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/milestones?state=all
PATCH https://api.github.com/repos/jwodder/test/milestones/2
{
    "state": "open"
}
'''

def test_milestone_open(cmd):
    r = cmd('--debug', 'milestone', 'open', '-R', 'jwodder/test',
            'Test Milestone')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/milestones?state=all
PATCH https://api.github.com/repos/jwodder/test/milestones/2
{
    "state": "open"
}
'''

def test_milestone_edit_close(cmd):
    r = cmd('--debug', 'milestone', 'edit', '--closed', '-R', 'jwodder/test',
            'Test Milestone')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/milestones?state=all
PATCH https://api.github.com/repos/jwodder/test/milestones/2
{
    "state": "closed"
}
'''

def test_milestone_close(cmd):
    r = cmd('--debug', 'milestone', 'close', '-R', 'jwodder/test',
            'Test Milestone')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/milestones?state=all
PATCH https://api.github.com/repos/jwodder/test/milestones/2
{
    "state": "closed"
}
'''

def test_milestone_delete(cmd):
    r = cmd('--debug', 'milestone', 'delete', '-R', 'jwodder/test', '-f',
            'Test Milestone')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/milestones?state=all
DELETE https://api.github.com/repos/jwodder/test/milestones/2
Milestone 'Test Milestone' deleted
'''

def test_milestone_show(cmd):
    r = cmd('milestone', 'show', '-R', 'jwodder/test', 'v1.0')
    assert r.exit_code == 0
    assert r.output == '''\
[
    {
        "closed_at": null,
        "closed_issues": 0,
        "created_at": "2017-10-20T19:16:13Z",
        "creator": "jwodder",
        "description": null,
        "due_on": null,
        "html_url": "https://github.com/jwodder/test/milestone/2",
        "id": 2855064,
        "number": 2,
        "open_issues": 0,
        "state": "open",
        "title": "v1.0",
        "updated_at": "2017-10-20T19:16:13Z",
        "url": "https://api.github.com/repos/jwodder/test/milestones/2"
    }
]
'''
