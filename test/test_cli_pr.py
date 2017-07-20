READ_PR = '''\
PR:        Add attrs
State:     open
Author:    jwodder
Date:      2017-04-15T23:59:11Z  (last updated 2017-05-20T23:16:50Z)
Labels:    
Assignees: 
Reactions: 👍 10

    ## What is this Python project?

    `attrs` allows you to declare your class's instance attributes once, and it then takes care of generating the boilerplate `__init__`, `__eq__`, `__repr__`, etc. methods for you, turning this:

    ```
    from functools import total_ordering
    @total_ordering
    class Point3D(object):
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

        def __repr__(self):
            return (self.__class__.__name__ +
                    ("(x={}, y={}, z={})".format(self.x, self.y, self.z)))

        def __eq__(self, other):
            if not isinstance(other, self.__class__):
                return NotImplemented
            return (self.x, self.y, self.z) == (other.x, other.y, other.z)

        def __lt__(self, other):
            if not isinstance(other, self.__class__):
                return NotImplemented
            return (self.x, self.y, self.z) < (other.x, other.y, other.z)
    ```

    into this:

    ```
    import attr
    @attr.s
    class Point3D(object):
        x = attr.ib()
        y = attr.ib()
        z = attr.ib()
    ```

    Example taken from [this blog post extolling the virtues of `attrs`](https://glyph.twistedmatrix.com/2016/08/attrs.html) written by the author of [Twisted](https://twistedmatrix.com/trac/).

    ## What's the difference between this Python project and similar ones?

    The only other project like this that I'm aware of is [`characteristic`](https://github.com/hynek/characteristic), which the author abandoned to create `attrs` instead.

    --

    Anyone who agrees with this pull request could vote for it by adding a :+1: to it, and usually, the maintainer will merge it when votes reach **20**.

comment 296700521
Author: pitcons
Date:   2017-04-24T15:12:42Z

     :+1:

comment 302904633
Author: ibewatuwant
Date:   2017-05-20T23:16:50Z

    Awesoms
'''

def test_issue_read_pr(cmd):
    r = cmd('issue', 'read', 'vinta/awesome-python/875')
    assert r.exit_code == 0
    assert r.output == READ_PR

def test_pr_read_pr(cmd):
    r = cmd('pr', 'read', 'vinta/awesome-python/875')
    assert r.exit_code == 0
    assert r.output == READ_PR

def test_pr_list_pypa_packaging(cmd):
    r = cmd('pr', 'list', 'pypa/packaging')
    assert r.exit_code == 0
    assert r.output == '''\
pypa/packaging/109
pypa/packaging/108
pypa/packaging/101
pypa/packaging/99
pypa/packaging/92
pypa/packaging/88
pypa/packaging/87
pypa/packaging/82
'''

# pr show
