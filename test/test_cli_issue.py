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

# issue search
