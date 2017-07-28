READ_ISSUE = '''\
Issue:     click plugins / cache / local datastore
State:     open
Author:    roscopecoltran
Date:      2017-06-29T09:39:32Z  (last updated 2017-06-29T16:33:16Z)
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
Date:   2017-06-29T16:31:32Z

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

# issue search
