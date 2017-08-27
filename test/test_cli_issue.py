import json
import os
from   pathlib import Path
import click

FILEDIR = Path(__file__).with_name('data') / 'files'

READ_ISSUE = '''\
Issue:     click plugins / cache / local datastore
State:     open
Author:    roscopecoltran
Date:      2017-06-29 05:39:32 -0400  (last updated 2017-06-29 12:33:16 -0400)
Labels:    Nice to Have
Assignees: 

    Hi,

    Hope u are all well !

    Was wondering if adding click's plugins or pluggy as a feature for ghutil was on your roadmap. It would allow to be non-intrusive for some external plugins if we could define a plugin registry via a yaml file.

    From my perspective, I just wanted to extend the use of some ghutil "repos" related command (eg. repos starred) and to append some meta-data (mainly in Json/YAML format) from different sources:

    Additional info from github api:
    - Add topics for any repo related queries
    - Add readme for starred repo for indexation
    - Add files list per branch for making faster any source code sifting, pattern matching

    examples of plugins for a cached registry of enhanced meta data:
    - https://github.com/thombashi/ghscard (mainly to build a chrome extension and some hover cards"
    - https://github.com/asciimoo/searx
    - https://github.com/nexB/scancode-toolkit
    - https://github.com/GitMarkTeam/gitmark
    - https://github.com/douban/linguist
    - https://github.com/porter-io/tagg-python

    Ideally, I wanted to complete a **ghutil** with a local datastore, sqlite or mysql, and, later on, I will had some classifiers on gh topics attributes with gensim/elastic search but that's another milestone ^^.

    Any feedback or inputs are welcomed, have a great day !

    Cheers,
    Richard

comment 312021247
Author: jwodder
Date:   2017-06-29 12:31:32 -0400

    I do not currently have any plans for supporting plugins, and any such plans would be very far down on my to-do list for this project.
'''

def test_issue_read_issue(cmd):
    r = cmd('issue', 'read', 'ghutil/1')
    assert r.exit_code == 0
    assert r.output == READ_ISSUE

def test_pr_read_issue(cmd):
    r = cmd('pr', 'read', 'ghutil/1')
    assert r.exit_code == 0
    assert r.output == READ_ISSUE

READ_CLOSED_ISSUE = '''\
Issue:     support git refs in @ syntax
State:     closed
Author:    zzzeek
Date:      2016-07-26 19:27:19 -0400  (last updated 2017-04-08 06:21:30 -0400)
Labels:    
Assignees: 
Milestone: 10.0
Closed:    2017-04-08 06:21:04 -0400 by xavfernandez
Reactions: 👍 5

    We'd like to be able to put paths to gerrit reviews in requirements files.

    Given a gerrit like https://review.openstack.org/#/c/345601/6, the path given for a git pull looks like:

       git pull https://git.openstack.org/openstack/oslo.db refs/changes/01/345601/6

    pip syntax we'd expect would be:

    ```
    .venv/bin/pip install -e git+https://git.openstack.org/openstack/oslo.db@refs/changes/01/345601/6#egg=oslo.db
    ```

    current output:

    ```

    Obtaining oslo.db from git+https://git.openstack.org/openstack/oslo.db@refs/changes/01/345601/6#egg=oslo.db
      Cloning https://git.openstack.org/openstack/oslo.db (to refs/changes/01/345601/6) to ./.venv/src/oslo.db
      Could not find a tag or branch 'refs/changes/01/345601/6', assuming commit.
    error: pathspec 'refs/changes/01/345601/6' did not match any file(s) known to git.
    Command "git checkout -q refs/changes/01/345601/6" failed with error code 1 in /home/classic/.venv/src/oslo.db
    ```

comment 268571420
Author: pradyunsg
Date:   2016-12-21 11:44:43 -0500  (last updated 2016-12-21 11:44:54 -0500)

    @sshnaidm Please use Github reactions. They're meant for exactly this.
'''

def test_issue_read_closed_issue(cmd):
    r = cmd('issue', 'read', 'pypa/pip/3876')
    assert r.exit_code == 0
    assert r.output == READ_CLOSED_ISSUE

def test_pr_read_closed_issue(cmd):
    r = cmd('pr', 'read', 'pypa/pip/3876')
    assert r.exit_code == 0
    assert r.output == READ_CLOSED_ISSUE

def test_issue_list_pypa_packaging(cmd):
    r = cmd('issue', 'list', 'pypa/packaging')
    assert r.exit_code == 0
    assert r.output == '''\
pypa/packaging/111
pypa/packaging/109
pypa/packaging/108
pypa/packaging/107
pypa/packaging/106
pypa/packaging/101
pypa/packaging/100
pypa/packaging/99
pypa/packaging/95
pypa/packaging/92
pypa/packaging/90
pypa/packaging/88
pypa/packaging/87
pypa/packaging/86
pypa/packaging/84
pypa/packaging/83
pypa/packaging/82
pypa/packaging/81
pypa/packaging/74
pypa/packaging/34
'''

def test_issue_show_issue(cmd):
    r = cmd('issue', 'show', 'ghutil/1')
    assert r.exit_code == 0
    assert r.output == '''\
[
    {
        "assignees": [],
        "body": "Hi,\\r\\n\\r\\nHope u are all well !\\r\\n\\r\\nWas wondering if adding click's plugins or pluggy as a feature for ghutil was on your roadmap. It would allow to be non-intrusive for some external plugins if we could define a plugin registry via a yaml file.\\r\\n\\r\\nFrom my perspective, I just wanted to extend the use of some ghutil \\"repos\\" related command (eg. repos starred) and to append some meta-data (mainly in Json/YAML format) from different sources:\\r\\n\\r\\nAdditional info from github api:\\r\\n- Add topics for any repo related queries\\r\\n- Add readme for starred repo for indexation\\r\\n- Add files list per branch for making faster any source code sifting, pattern matching\\r\\n\\r\\nexamples of plugins for a cached registry of enhanced meta data:\\r\\n- https://github.com/thombashi/ghscard (mainly to build a chrome extension and some hover cards\\"\\r\\n- https://github.com/asciimoo/searx\\r\\n- https://github.com/nexB/scancode-toolkit\\r\\n- https://github.com/GitMarkTeam/gitmark\\r\\n- https://github.com/douban/linguist\\r\\n- https://github.com/porter-io/tagg-python\\r\\n\\r\\nIdeally, I wanted to complete a **ghutil** with a local datastore, sqlite or mysql, and, later on, I will had some classifiers on gh topics attributes with gensim/elastic search but that's another milestone ^^.\\r\\n\\r\\nAny feedback or inputs are welcomed, have a great day !\\r\\n\\r\\nCheers,\\r\\nRichard",
        "closed_at": null,
        "closed_by": null,
        "comments": 1,
        "created_at": "2017-06-29T09:39:32Z",
        "html_url": "https://github.com/jwodder/ghutil/issues/1",
        "id": 239420922,
        "labels": [
            "Nice to Have"
        ],
        "locked": false,
        "milestone": null,
        "number": 1,
        "reactions": {},
        "state": "open",
        "title": "click plugins / cache / local datastore",
        "updated_at": "2017-06-29T16:33:16Z",
        "url": "https://api.github.com/repos/jwodder/ghutil/issues/1",
        "user": "roscopecoltran"
    }
]
'''

def test_issue_show_pr(cmd):
    r = cmd('issue', 'show', 'vinta/awesome-python/875')
    assert r.exit_code == 0
    assert r.output == '''\
[
    {
        "assignees": [],
        "body": "## What is this Python project?\\r\\n\\r\\n`attrs` allows you to declare your class's instance attributes once, and it then takes care of generating the boilerplate `__init__`, `__eq__`, `__repr__`, etc. methods for you, turning this:\\r\\n\\r\\n```\\r\\nfrom functools import total_ordering\\r\\n@total_ordering\\r\\nclass Point3D(object):\\r\\n    def __init__(self, x, y, z):\\r\\n        self.x = x\\r\\n        self.y = y\\r\\n        self.z = z\\r\\n\\r\\n    def __repr__(self):\\r\\n        return (self.__class__.__name__ +\\r\\n                (\\"(x={}, y={}, z={})\\".format(self.x, self.y, self.z)))\\r\\n\\r\\n    def __eq__(self, other):\\r\\n        if not isinstance(other, self.__class__):\\r\\n            return NotImplemented\\r\\n        return (self.x, self.y, self.z) == (other.x, other.y, other.z)\\r\\n\\r\\n    def __lt__(self, other):\\r\\n        if not isinstance(other, self.__class__):\\r\\n            return NotImplemented\\r\\n        return (self.x, self.y, self.z) < (other.x, other.y, other.z)\\r\\n```\\r\\n\\r\\ninto this:\\r\\n\\r\\n```\\r\\nimport attr\\r\\n@attr.s\\r\\nclass Point3D(object):\\r\\n    x = attr.ib()\\r\\n    y = attr.ib()\\r\\n    z = attr.ib()\\r\\n```\\r\\n\\r\\nExample taken from [this blog post extolling the virtues of `attrs`](https://glyph.twistedmatrix.com/2016/08/attrs.html) written by the author of [Twisted](https://twistedmatrix.com/trac/).\\r\\n\\r\\n## What's the difference between this Python project and similar ones?\\r\\n\\r\\nThe only other project like this that I'm aware of is [`characteristic`](https://github.com/hynek/characteristic), which the author abandoned to create `attrs` instead.\\r\\n\\r\\n--\\r\\n\\r\\nAnyone who agrees with this pull request could vote for it by adding a :+1: to it, and usually, the maintainer will merge it when votes reach **20**.",
        "closed_at": null,
        "closed_by": null,
        "comments": 2,
        "created_at": "2017-04-15T23:59:11Z",
        "html_url": "https://github.com/vinta/awesome-python/pull/875",
        "id": 221980315,
        "labels": [],
        "locked": false,
        "milestone": null,
        "number": 875,
        "reactions": {
            "+1": 10
        },
        "state": "open",
        "title": "Add attrs",
        "updated_at": "2017-05-20T23:16:50Z",
        "url": "https://api.github.com/repos/vinta/awesome-python/issues/875",
        "user": "jwodder"
    }
]
'''

ISSUE_COMMENTS = '''\
[
    {
        "body": "I do not currently have any plans for supporting plugins, and any such plans would be very far down on my to-do list for this project.\\n",
        "created_at": "2017-06-29T16:31:32Z",
        "html_url": "https://github.com/jwodder/ghutil/issues/1#issuecomment-312021247",
        "id": 312021247,
        "reactions": {},
        "updated_at": "2017-06-29T16:31:32Z",
        "url": "https://api.github.com/repos/jwodder/ghutil/issues/comments/312021247",
        "user": "jwodder"
    }
]
'''

def test_issue_comments_issue(cmd):
    r = cmd('issue', 'comments', 'ghutil/1')
    assert r.exit_code == 0
    assert r.output == ISSUE_COMMENTS

def test_pr_comments_issue(cmd):
    r = cmd('pr', 'comments', 'ghutil/1')
    assert r.exit_code == 0
    assert r.output == ISSUE_COMMENTS

def test_issue_open(cmd):
    issues = ['jwodder/test/1', 'test/2']
    r = cmd('issue', 'open', *issues)
    assert r.exit_code == 0
    assert r.output == ''
    for i in issues:
        r = cmd('issue', 'show', '-v', i)
        assert r.exit_code == 0
        assert json.loads(r.output)[0]["state"] == "open"

def test_issue_close(cmd):
    issues = ['jwodder/test/1', 'test/2']
    r = cmd('issue', 'close', *issues)
    assert r.exit_code == 0
    assert r.output == ''
    for i in issues:
        r = cmd('issue', 'show', '-v', i)
        assert r.exit_code == 0
        assert json.loads(r.output)[0]["state"] == "closed"

def test_issue_lock(cmd):
    issues = ['jwodder/test/1', 'test/2']
    r = cmd('issue', 'lock', *issues)
    assert r.exit_code == 0
    assert r.output == ''
    for i in issues:
        r = cmd('issue', 'show', '-v', i)
        assert r.exit_code == 0
        assert json.loads(r.output)[0]["locked"]

def test_issue_unlock(cmd):
    issues = ['jwodder/test/1', 'test/2']
    r = cmd('issue', 'unlock', *issues)
    assert r.exit_code == 0
    assert r.output == ''
    for i in issues:
        r = cmd('issue', 'show', '-v', i)
        assert r.exit_code == 0
        assert not json.loads(r.output)[0]["locked"]

def test_issue_edit_one_assignee(cmd):
    r = cmd('--debug', 'issue', 'edit', '--assignee', 'jwodder', 'jwodder/test/1')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/issues/1
PATCH https://api.github.com/repos/jwodder/test/issues/1
{
    "assignees": [
        "jwodder"
    ]
}
'''

def test_issue_edit_nil_assignee(cmd):
    r = cmd('--debug', 'issue', 'edit', '--assignee', '', 'jwodder/test/1')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/issues/1
PATCH https://api.github.com/repos/jwodder/test/issues/1
{
    "assignees": []
}
'''

def test_issue_edit_one_label(cmd):
    r = cmd('--debug', 'issue', 'edit', '--label', 'invalid', 'jwodder/test/1')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/issues/1
PATCH https://api.github.com/repos/jwodder/test/issues/1
{
    "labels": [
        "invalid"
    ]
}
'''

def test_issue_edit_nil_label(cmd):
    r = cmd('--debug', 'issue', 'edit', '--label', '', 'jwodder/test/1')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/issues/1
PATCH https://api.github.com/repos/jwodder/test/issues/1
{
    "labels": []
}
'''

def test_issue_edit_two_labels(cmd):
    r = cmd('--debug', 'issue', 'edit', '--label', 'invalid', '-lhelp wanted', 'jwodder/test/1')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/issues/1
PATCH https://api.github.com/repos/jwodder/test/issues/1
{
    "labels": [
        "invalid",
        "help wanted"
    ]
}
'''

def test_issue_edit_milestone(cmd):
    r = cmd('--debug', 'issue', 'edit', '--milestone', 'v1.0', 'jwodder/test/1')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/issues/1
GET https://api.github.com/repos/jwodder/test/milestones?state=all
PATCH https://api.github.com/repos/jwodder/test/issues/1
{
    "milestone": 1
}
'''

def test_issue_edit_int_milestone(cmd):
    r = cmd('--debug', 'issue', 'edit', '--milestone', '1', 'jwodder/test/1')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/issues/1
PATCH https://api.github.com/repos/jwodder/test/issues/1
{
    "milestone": 1
}
'''

def test_issue_edit_nil_milestone(cmd):
    r = cmd('--debug', 'issue', 'edit', '--milestone', '', 'jwodder/test/1')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/issues/1
PATCH https://api.github.com/repos/jwodder/test/issues/1
{
    "milestone": null
}
'''

def test_issue_edit_title(cmd):
    r = cmd('--debug', 'issue', 'edit', '--title', 'API test site', 'jwodder/test/1')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/issues/1
PATCH https://api.github.com/repos/jwodder/test/issues/1
{
    "title": "API test site"
}
'''

def test_issue_edit_nil_title(cmd):
    r = cmd('--debug', 'issue', 'edit', '--title', '', 'jwodder/test/1')
    assert r.exit_code != 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/issues/1
PATCH https://api.github.com/repos/jwodder/test/issues/1
{
    "title": ""
}
422 Client Error: Unprocessable Entity for url: https://api.github.com/repos/jwodder/test/issues/1
{
    "documentation_url": "https://developer.github.com/v3/issues/#edit-an-issue",
    "errors": [
        {
            "code": "missing_field",
            "field": "title",
            "resource": "Issue"
        }
    ],
    "message": "Validation Failed"
}
'''

def test_issue_edit_body(cmd):
    r = cmd('--debug', 'issue', 'edit', '--body', str(FILEDIR/'life.py'), 'jwodder/test/1')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/issues/1
PATCH https://api.github.com/repos/jwodder/test/issues/1
{
    "body": "from collections import Counter\\n\\ndef life(before):\\n    \\\"\\\"\\\"\\n    Takes as input a state of Conway's Game of Life, represented as an iterable\\n    of ``(int, int)`` pairs giving the coordinates of living cells, and returns\\n    a `set` of ``(int, int)`` pairs representing the next state\\n    \\\"\\\"\\\"\\n    before = set(before)\\n    neighbors = Counter(\\n        (x+i, y+j) for (x,y) in before\\n                   for i in [-1,0,1]\\n                   for j in [-1,0,1]\\n                   if (i,j) != (0,0)\\n    )\\n    return {xy for (xy, n) in neighbors.items()\\n               if n == 3 or (n == 2 and xy in before)}\\n"
}
'''

def test_issue_edit_body_devnull(cmd):
    r = cmd('--debug', 'issue', 'edit', '--body', os.devnull, 'jwodder/test/1')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/issues/1
PATCH https://api.github.com/repos/jwodder/test/issues/1
{
    "body": ""
}
'''

def test_issue_edit_open(cmd):
    r = cmd('--debug', 'issue', 'edit', '--open', 'jwodder/test/1')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/issues/1
PATCH https://api.github.com/repos/jwodder/test/issues/1
{
    "state": "open"
}
'''

def test_issue_edit_closed(cmd):
    r = cmd('--debug', 'issue', 'edit', '--closed', 'jwodder/test/1')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/issues/1
PATCH https://api.github.com/repos/jwodder/test/issues/1
{
    "state": "closed"
}
'''

def test_issue_edit_open_close(cmd):
    r = cmd('--debug', 'issue', 'edit', '--open', '--close', 'jwodder/test/1')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/issues/1
PATCH https://api.github.com/repos/jwodder/test/issues/1
{
    "state": "closed"
}
'''

ISSUE_EDIT_MSG = 'Title: Test issue\n' \
                 'Labels: \n' \
                 'Assignees: \n' \
                 'Milestone: \n' \
                 'Open: yes\n' \
                 '\n' \
                 'Here be testing.\n'

def test_issue_edit_nosave(cmd, mocker):
    mocker.patch('click.edit', return_value=None)
    r = cmd('--debug', 'issue', 'edit', 'jwodder/test/1')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/issues/1
GET https://api.github.com/repos/jwodder/test
No modifications made; exiting
'''
    click.edit.assert_called_once_with(ISSUE_EDIT_MSG, require_save=True)

def test_issue_edit_nochange(cmd, mocker):
    mocker.patch('click.edit', return_value=ISSUE_EDIT_MSG)
    r = cmd('--debug', 'issue', 'edit', 'jwodder/test/1')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/issues/1
GET https://api.github.com/repos/jwodder/test
No modifications made; exiting
'''
    click.edit.assert_called_once_with(ISSUE_EDIT_MSG, require_save=True)

def test_issue_edit_change_everything(cmd, mocker):
    mocker.patch(
        'click.edit',
        return_value='Title: Tests at work\n'
                     'Labels: help wanted, enhancement\n'
                     'Assignees: jwodder\n'
                     'Milestone: v1.0\n'
                     'Open: false\n'
                     '\n'
                     'Once upon a time, there was a little unit test.'
                     '  He failed, and the project was cancelled before anyone'
                     ' could figure out why.'
                     '  The end.\n'
    )
    r = cmd('--debug', 'issue', 'edit', 'jwodder/test/1')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/issues/1
GET https://api.github.com/repos/jwodder/test
GET https://api.github.com/repos/jwodder/test/milestones?state=all
PATCH https://api.github.com/repos/jwodder/test/issues/1
{
    "assignees": [
        "jwodder"
    ],
    "body": "Once upon a time, there was a little unit test.  He failed, and the project was cancelled before anyone could figure out why.  The end.\\n",
    "labels": [
        "help wanted",
        "enhancement"
    ],
    "milestone": 1,
    "state": "closed",
    "title": "Tests at work"
}
'''
    click.edit.assert_called_once_with(ISSUE_EDIT_MSG, require_save=True)

def test_issue_label_add(cmd):
    r = cmd('issue', 'show', 'jwodder/test/1')
    assert r.exit_code == 0
    assert json.loads(r.output)[0]["labels"] == ['enhancement']
    r = cmd('--debug', 'issue', 'label', 'jwodder/test/1', 'invalid','question')
    assert r.exit_code == 0
    assert r.output == '''\
POST https://api.github.com/repos/jwodder/test/issues/1/labels
[
    "invalid",
    "question"
]
'''
    r = cmd('issue', 'show', 'jwodder/test/1')
    assert r.exit_code == 0
    assert sorted(json.loads(r.output)[0]["labels"]) == \
        ['enhancement', 'invalid', 'question']

def test_issue_label_add_redundant(cmd):
    r = cmd('issue', 'show', 'jwodder/test/1')
    assert r.exit_code == 0
    assert sorted(json.loads(r.output)[0]["labels"]) == \
        ['enhancement', 'invalid', 'question']
    r = cmd('--debug', 'issue', 'label', 'jwodder/test/1', 'invalid', 'wontfix')
    assert r.exit_code == 0
    assert r.output == '''\
POST https://api.github.com/repos/jwodder/test/issues/1/labels
[
    "invalid",
    "wontfix"
]
'''
    r = cmd('issue', 'show', 'jwodder/test/1')
    assert r.exit_code == 0
    assert sorted(json.loads(r.output)[0]["labels"]) == \
        ['enhancement', 'invalid', 'question', 'wontfix']

def test_issue_label_add_nothing(cmd):
    r = cmd('issue', 'show', 'jwodder/test/1')
    assert r.exit_code == 0
    assert sorted(json.loads(r.output)[0]["labels"]) == \
        ['enhancement', 'question']
    r = cmd('--debug', 'issue', 'label', 'jwodder/test/1')
    assert r.exit_code == 0
    assert r.output == '''\
POST https://api.github.com/repos/jwodder/test/issues/1/labels
[]
'''
    r = cmd('issue', 'show', 'jwodder/test/1')
    assert r.exit_code == 0
    assert sorted(json.loads(r.output)[0]["labels"]) == \
        ['enhancement', 'question']

def test_issue_label_delete(cmd):
    r = cmd('issue', 'show', 'jwodder/test/1')
    assert r.exit_code == 0
    assert sorted(json.loads(r.output)[0]["labels"]) == \
        ['enhancement', 'invalid', 'question', 'wontfix']
    r = cmd('--debug', 'issue', 'label', '--delete', 'jwodder/test/1',
            'invalid', 'wontfix')
    assert r.exit_code == 0
    assert r.output == '''\
DELETE https://api.github.com/repos/jwodder/test/issues/1/labels/invalid
DELETE https://api.github.com/repos/jwodder/test/issues/1/labels/wontfix
'''
    r = cmd('issue', 'show', 'jwodder/test/1')
    assert r.exit_code == 0
    assert sorted(json.loads(r.output)[0]["labels"]) == \
        ['enhancement', 'question']

def test_issue_label_delete_nothing(cmd):
    r = cmd('issue', 'show', 'jwodder/test/1')
    assert r.exit_code == 0
    assert sorted(json.loads(r.output)[0]["labels"]) == \
        ['enhancement', 'question']
    r = cmd('--debug', 'issue', 'label', '--delete', 'jwodder/test/1')
    assert r.exit_code == 0
    assert r.output == ''
    r = cmd('issue', 'show', 'jwodder/test/1')
    assert r.exit_code == 0
    assert sorted(json.loads(r.output)[0]["labels"]) == \
        ['enhancement', 'question']

def test_issue_label_set(cmd):
    r = cmd('issue', 'show', 'jwodder/test/1')
    assert r.exit_code == 0
    assert sorted(json.loads(r.output)[0]["labels"]) == \
        ['enhancement', 'question']
    r = cmd('--debug', 'issue', 'label', '--set', 'jwodder/test/1',
            'invalid', 'enhancement')
    assert r.exit_code == 0
    assert r.output == '''\
PUT https://api.github.com/repos/jwodder/test/issues/1/labels
[
    "invalid",
    "enhancement"
]
'''
    r = cmd('issue', 'show', 'jwodder/test/1')
    assert r.exit_code == 0
    assert sorted(json.loads(r.output)[0]["labels"]) == \
        ['enhancement', 'invalid']

def test_issue_label_set_nothing(cmd):
    r = cmd('issue', 'show', 'jwodder/test/1')
    assert r.exit_code == 0
    assert sorted(json.loads(r.output)[0]["labels"]) == \
        ['enhancement', 'invalid']
    r = cmd('--debug', 'issue', 'label', '--set', 'jwodder/test/1')
    assert r.exit_code == 0
    assert r.output == '''\
PUT https://api.github.com/repos/jwodder/test/issues/1/labels
[]
'''
    r = cmd('issue', 'show', 'jwodder/test/1')
    assert r.exit_code == 0
    assert json.loads(r.output)[0]["labels"] == []

def test_issue_label_delete_set_nothing(nullcmd):
    r = nullcmd('issue', 'label', '--delete', '--set', 'jwodder/test/1', 'bug')
    assert r.exit_code != 0
    assert r.output == '''\
Usage: gh issue label [OPTIONS] ISSUE [LABEL]...

Error: --delete and --set are mutually exclusive
'''

# issue edit - two assignees
# editing an issue on a repository you don't have push access to
# issue search
