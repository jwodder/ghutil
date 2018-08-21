from   io      import BytesIO
from   pathlib import Path
import webbrowser
from   ghutil  import git

FILEDIR = Path(__file__).with_name('data') / 'files'

GIST_LIST = '''\
8b229cd59365b98ab5172b9d1e0904f6
4bf350e2d72b547b22dc9de52148ccbe
7b00ad691ecbfe9fa3ff40388bae6e23
19317d3e4b9a58f2355e7643040d483a
f1091e01d3fbe9c02e7f
3b83cd3dd3a0409f076a
0e669fc431c00eac8c39
61bebc3ca55bf04ea4cc
33d7017e6255d13c5037
10acad4754f292723cd7
384dfc4ea9af656f2943
4008289fe808afd76284
65591f22496dc042b469
00550a8cbfec22126bf5
d9ee213119fff3f46aa2
b5ad97a344999ccbf0a2
961599
'''

def test_gist_list(cmd):
    r = cmd('gist', 'list')
    assert r.exit_code == 0
    assert r.output == GIST_LIST

def test_gist(cmd):
    r = cmd('gist')
    assert r.exit_code == 0
    assert r.output == GIST_LIST

def test_gist_show_fork(cmd):
    r = cmd('gist', 'show', '4bf350e2d72b547b22dc9de52148ccbe')
    assert r.exit_code == 0
    assert r.output == '''\
[
    {
        "comments": 0,
        "created_at": "2017-05-07T20:43:43Z",
        "description": "Print a 256-colour test pattern in the terminal",
        "files": {
            "print256colours.py": {
                "filename": "print256colours.py",
                "language": "Python",
                "raw_url": "https://gist.githubusercontent.com/jwodder/4bf350e2d72b547b22dc9de52148ccbe/raw/ab4b60d4637f1a587ff9239f1b20cc45de1e93ab/print256colours.py",
                "size": 2851,
                "truncated": false,
                "type": "application/x-python"
            }
        },
        "fork_of": "89ffe32783f89f403bba96bd7bcd1263",
        "forks": [],
        "git_pull_url": "https://gist.github.com/4bf350e2d72b547b22dc9de52148ccbe.git",
        "html_url": "https://gist.github.com/4bf350e2d72b547b22dc9de52148ccbe",
        "id": "4bf350e2d72b547b22dc9de52148ccbe",
        "owner": "jwodder",
        "public": true,
        "updated_at": "2017-05-07T21:20:15Z",
        "url": "https://api.github.com/gists/4bf350e2d72b547b22dc9de52148ccbe"
    }
]
'''

def test_gist_show_forked(cmd):
    r = cmd('gist', 'show', '89ffe32783f89f403bba96bd7bcd1263')
    assert r.exit_code == 0
    assert r.output == '''\
[
    {
        "comments": 6,
        "created_at": "2016-09-05T09:38:18Z",
        "description": "Print a 256-colour test pattern in the terminal",
        "files": {
            "print256colours.sh": {
                "filename": "print256colours.sh",
                "language": "Shell",
                "raw_url": "https://gist.githubusercontent.com/HaleTom/89ffe32783f89f403bba96bd7bcd1263/raw/99e3d8c9f9d3ae7d37e006fe9af328f0c7ea849c/print256colours.sh",
                "size": 3264,
                "truncated": false,
                "type": "application/x-sh"
            }
        },
        "forks": [
            "568540521e8350d42330e259c9494219",
            "97adbdfdd9222977a5ec58bb64d0c988",
            "cab0ca84a643d8a894b423eb589ca9da",
            "d5ce854fb03a10ab0cadbdc23852484d",
            "0c4f2ccc2dd21d2f60dd61569ecb9c5f",
            "b7cf18cee6d5efe77ff56e1e24a10ba4",
            "4bf350e2d72b547b22dc9de52148ccbe",
            "12722945037263555a2fe96112c459a7",
            "9a0038e50115c628d37e1259f27b1652",
            "f9e451d90e75c9102a86bb787587ad16"
        ],
        "git_pull_url": "https://gist.github.com/89ffe32783f89f403bba96bd7bcd1263.git",
        "html_url": "https://gist.github.com/89ffe32783f89f403bba96bd7bcd1263",
        "id": "89ffe32783f89f403bba96bd7bcd1263",
        "owner": "HaleTom",
        "public": true,
        "updated_at": "2017-07-15T20:38:13Z",
        "url": "https://api.github.com/gists/89ffe32783f89f403bba96bd7bcd1263"
    }
]
'''

def test_gist_starred(cmd):
    r = cmd('gist', 'starred')
    assert r.exit_code == 0
    assert r.output == '''\
89ffe32783f89f403bba96bd7bcd1263
19317d3e4b9a58f2355e7643040d483a
4f100a9592b05e9b4d63
5823693
3331384
674099
'''

def test_gist_new_noargs(nullcmd):
    r = nullcmd('gist', 'new')
    assert r.exit_code != 0
    assert r.output == '''\
Usage: gh gist new [OPTIONS] [FILES]...

Error: No files specified
'''

def test_gist_new_unnamed(cmd):
    r = cmd('gist', 'new', '-d', 'A file', str(FILEDIR/'lorem.txt'))
    assert r.exit_code == 0
    assert r.output == '''\
{
    "comments": 0,
    "created_at": "2017-08-02T18:23:41Z",
    "description": "A file",
    "files": {
        "lorem.txt": {
            "filename": "lorem.txt",
            "language": "Text",
            "raw_url": "https://gist.githubusercontent.com/jwodder/db3b6873d3c9f7c7cab76cc3f2d1cd93/raw/ebe3d387302051a9d40f5cd9e09b9b2af7a8db40/lorem.txt",
            "size": 450,
            "truncated": false,
            "type": "text/plain"
        }
    },
    "forks": [],
    "git_pull_url": "https://gist.github.com/db3b6873d3c9f7c7cab76cc3f2d1cd93.git",
    "html_url": "https://gist.github.com/db3b6873d3c9f7c7cab76cc3f2d1cd93",
    "id": "db3b6873d3c9f7c7cab76cc3f2d1cd93",
    "owner": "jwodder",
    "public": true,
    "updated_at": "2017-08-02T18:23:41Z",
    "url": "https://api.github.com/gists/db3b6873d3c9f7c7cab76cc3f2d1cd93"
}
'''

def test_gist_new_two_unnamed(cmd):
    r = cmd(
        'gist', 'new', '-d', 'Two files',
        str(FILEDIR/'lorem.txt'),
        str(FILEDIR/'life.py'),
    )
    assert r.exit_code == 0
    assert r.output == '''\
{
    "comments": 0,
    "created_at": "2017-08-02T18:23:42Z",
    "description": "Two files",
    "files": {
        "life.py": {
            "filename": "life.py",
            "language": "Python",
            "raw_url": "https://gist.githubusercontent.com/jwodder/46b547788a193f706ca66b9519780e58/raw/f3e251d5db162c0fb419bd3179b120f522c6ee83/life.py",
            "size": 600,
            "truncated": false,
            "type": "application/x-python"
        },
        "lorem.txt": {
            "filename": "lorem.txt",
            "language": "Text",
            "raw_url": "https://gist.githubusercontent.com/jwodder/46b547788a193f706ca66b9519780e58/raw/ebe3d387302051a9d40f5cd9e09b9b2af7a8db40/lorem.txt",
            "size": 450,
            "truncated": false,
            "type": "text/plain"
        }
    },
    "forks": [],
    "git_pull_url": "https://gist.github.com/46b547788a193f706ca66b9519780e58.git",
    "html_url": "https://gist.github.com/46b547788a193f706ca66b9519780e58",
    "id": "46b547788a193f706ca66b9519780e58",
    "owner": "jwodder",
    "public": true,
    "updated_at": "2017-08-02T18:23:42Z",
    "url": "https://api.github.com/gists/46b547788a193f706ca66b9519780e58"
}
'''

def test_gist_new_named(cmd):
    r = cmd(
        'gist', 'new', '-d', 'A named file',
        '-f', 'not-lorem.txt', str(FILEDIR/'lorem.txt'),
    )
    assert r.exit_code == 0
    assert r.output == '''\
{
    "comments": 0,
    "created_at": "2017-08-02T18:23:43Z",
    "description": "A named file",
    "files": {
        "not-lorem.txt": {
            "filename": "not-lorem.txt",
            "language": "Text",
            "raw_url": "https://gist.githubusercontent.com/jwodder/51d9d530c04470c6edc18a80418a8cae/raw/ebe3d387302051a9d40f5cd9e09b9b2af7a8db40/not-lorem.txt",
            "size": 450,
            "truncated": false,
            "type": "text/plain"
        }
    },
    "forks": [],
    "git_pull_url": "https://gist.github.com/51d9d530c04470c6edc18a80418a8cae.git",
    "html_url": "https://gist.github.com/51d9d530c04470c6edc18a80418a8cae",
    "id": "51d9d530c04470c6edc18a80418a8cae",
    "owner": "jwodder",
    "public": true,
    "updated_at": "2017-08-02T18:23:43Z",
    "url": "https://api.github.com/gists/51d9d530c04470c6edc18a80418a8cae"
}
'''

def test_gist_new_named_unnamed(cmd):
    r = cmd(
        'gist', 'new',
        '-f', 'lorem2.txt', str(FILEDIR/'subdir'/'lorem.txt'),
        str(FILEDIR/'lorem.txt'),
    )
    assert r.exit_code == 0
    assert r.output == '''\
{
    "comments": 0,
    "created_at": "2017-08-02T18:23:44Z",
    "description": null,
    "files": {
        "lorem.txt": {
            "filename": "lorem.txt",
            "language": "Text",
            "raw_url": "https://gist.githubusercontent.com/jwodder/4729d6a1d2ea65be4e471d8683620e2d/raw/ebe3d387302051a9d40f5cd9e09b9b2af7a8db40/lorem.txt",
            "size": 450,
            "truncated": false,
            "type": "text/plain"
        },
        "lorem2.txt": {
            "filename": "lorem2.txt",
            "language": "Text",
            "raw_url": "https://gist.githubusercontent.com/jwodder/4729d6a1d2ea65be4e471d8683620e2d/raw/8102356d848536c9ff5ed0ea189d565f165fe662/lorem2.txt",
            "size": 1171,
            "truncated": false,
            "type": "text/plain"
        }
    },
    "forks": [],
    "git_pull_url": "https://gist.github.com/4729d6a1d2ea65be4e471d8683620e2d.git",
    "html_url": "https://gist.github.com/4729d6a1d2ea65be4e471d8683620e2d",
    "id": "4729d6a1d2ea65be4e471d8683620e2d",
    "owner": "jwodder",
    "public": true,
    "updated_at": "2017-08-02T18:23:44Z",
    "url": "https://api.github.com/gists/4729d6a1d2ea65be4e471d8683620e2d"
}
'''

def test_gist_new_unnamed_named(cmd):
    r = cmd(
        'gist', 'new',
        str(FILEDIR/'lorem.txt'),
        '-f', 'lorem2.txt', str(FILEDIR/'subdir'/'lorem.txt'),
    )
    assert r.exit_code == 0
    assert r.output == '''\
{
    "comments": 0,
    "created_at": "2017-08-02T18:23:44Z",
    "description": null,
    "files": {
        "lorem.txt": {
            "filename": "lorem.txt",
            "language": "Text",
            "raw_url": "https://gist.githubusercontent.com/jwodder/4729d6a1d2ea65be4e471d8683620e2d/raw/ebe3d387302051a9d40f5cd9e09b9b2af7a8db40/lorem.txt",
            "size": 450,
            "truncated": false,
            "type": "text/plain"
        },
        "lorem2.txt": {
            "filename": "lorem2.txt",
            "language": "Text",
            "raw_url": "https://gist.githubusercontent.com/jwodder/4729d6a1d2ea65be4e471d8683620e2d/raw/8102356d848536c9ff5ed0ea189d565f165fe662/lorem2.txt",
            "size": 1171,
            "truncated": false,
            "type": "text/plain"
        }
    },
    "forks": [],
    "git_pull_url": "https://gist.github.com/4729d6a1d2ea65be4e471d8683620e2d.git",
    "html_url": "https://gist.github.com/4729d6a1d2ea65be4e471d8683620e2d",
    "id": "4729d6a1d2ea65be4e471d8683620e2d",
    "owner": "jwodder",
    "public": true,
    "updated_at": "2017-08-02T18:23:44Z",
    "url": "https://api.github.com/gists/4729d6a1d2ea65be4e471d8683620e2d"
}
'''

def test_gist_new_stdin(cmd):
    fp = BytesIO(b'This is stdin.')
    fp.name = '<stdin>'  # or else we get an AttributeError
    r = cmd('gist', 'new', '-', input=fp)
    assert r.exit_code == 0
    assert r.output == '''\
{
    "comments": 0,
    "created_at": "2017-08-02T18:44:30Z",
    "description": null,
    "files": {
        "<stdin>": {
            "filename": "<stdin>",
            "language": null,
            "raw_url": "https://gist.githubusercontent.com/jwodder/7577ef3391fd07516aa207eef5f626be/raw/4262ec90ea000a131b930ec60ddac44e3a76545e/%3Cstdin%3E",
            "size": 14,
            "truncated": false,
            "type": "text/plain"
        }
    },
    "forks": [],
    "git_pull_url": "https://gist.github.com/7577ef3391fd07516aa207eef5f626be.git",
    "html_url": "https://gist.github.com/7577ef3391fd07516aa207eef5f626be",
    "id": "7577ef3391fd07516aa207eef5f626be",
    "owner": "jwodder",
    "public": true,
    "updated_at": "2017-08-02T18:44:30Z",
    "url": "https://api.github.com/gists/7577ef3391fd07516aa207eef5f626be"
}
'''

def test_gist_new_named_stdin(cmd):
    r = cmd('gist', 'new', '-f', 'standard input', '-', input='This is stdin.')
    assert r.exit_code == 0
    assert r.output == '''\
{
    "comments": 0,
    "created_at": "2017-08-02T18:23:47Z",
    "description": null,
    "files": {
        "standard input": {
            "filename": "standard input",
            "language": null,
            "raw_url": "https://gist.githubusercontent.com/jwodder/5a302aefacbd11c7c7b1fc1684bea669/raw/4262ec90ea000a131b930ec60ddac44e3a76545e/standard%20input",
            "size": 14,
            "truncated": false,
            "type": "text/plain"
        }
    },
    "forks": [],
    "git_pull_url": "https://gist.github.com/5a302aefacbd11c7c7b1fc1684bea669.git",
    "html_url": "https://gist.github.com/5a302aefacbd11c7c7b1fc1684bea669",
    "id": "5a302aefacbd11c7c7b1fc1684bea669",
    "owner": "jwodder",
    "public": true,
    "updated_at": "2017-08-02T18:23:47Z",
    "url": "https://api.github.com/gists/5a302aefacbd11c7c7b1fc1684bea669"
}
'''

def test_gist_new_duped_names(cmd):
    r = cmd(
        'gist', 'new',
        str(FILEDIR/'lorem.txt'),
        str(FILEDIR/'subdir'/'lorem.txt'),
    )
    assert r.exit_code == 0
    assert r.output == '''\
{
    "comments": 0,
    "created_at": "2017-08-02T18:23:48Z",
    "description": null,
    "files": {
        "lorem.txt": {
            "filename": "lorem.txt",
            "language": "Text",
            "raw_url": "https://gist.githubusercontent.com/jwodder/0a577c9ccb01dadf1a3952ffaf3fc8f5/raw/8102356d848536c9ff5ed0ea189d565f165fe662/lorem.txt",
            "size": 1171,
            "truncated": false,
            "type": "text/plain"
        }
    },
    "forks": [],
    "git_pull_url": "https://gist.github.com/0a577c9ccb01dadf1a3952ffaf3fc8f5.git",
    "html_url": "https://gist.github.com/0a577c9ccb01dadf1a3952ffaf3fc8f5",
    "id": "0a577c9ccb01dadf1a3952ffaf3fc8f5",
    "owner": "jwodder",
    "public": true,
    "updated_at": "2017-08-02T18:23:48Z",
    "url": "https://api.github.com/gists/0a577c9ccb01dadf1a3952ffaf3fc8f5"
}
'''

def test_gist_new_unduped_names(cmd):
    r = cmd(
        'gist', 'new',
        '-f', 'lorem1.txt', str(FILEDIR/'lorem.txt'),
        '-f', 'lorem2.txt', str(FILEDIR/'subdir'/'lorem.txt'),
    )
    assert r.exit_code == 0
    assert r.output == '''\
{
    "comments": 0,
    "created_at": "2017-08-02T18:23:50Z",
    "description": null,
    "files": {
        "lorem1.txt": {
            "filename": "lorem1.txt",
            "language": "Text",
            "raw_url": "https://gist.githubusercontent.com/jwodder/77eb2255b2fee9ee88ab331586596779/raw/ebe3d387302051a9d40f5cd9e09b9b2af7a8db40/lorem1.txt",
            "size": 450,
            "truncated": false,
            "type": "text/plain"
        },
        "lorem2.txt": {
            "filename": "lorem2.txt",
            "language": "Text",
            "raw_url": "https://gist.githubusercontent.com/jwodder/77eb2255b2fee9ee88ab331586596779/raw/8102356d848536c9ff5ed0ea189d565f165fe662/lorem2.txt",
            "size": 1171,
            "truncated": false,
            "type": "text/plain"
        }
    },
    "forks": [],
    "git_pull_url": "https://gist.github.com/77eb2255b2fee9ee88ab331586596779.git",
    "html_url": "https://gist.github.com/77eb2255b2fee9ee88ab331586596779",
    "id": "77eb2255b2fee9ee88ab331586596779",
    "owner": "jwodder",
    "public": true,
    "updated_at": "2017-08-02T18:23:50Z",
    "url": "https://api.github.com/gists/77eb2255b2fee9ee88ab331586596779"
}
'''

def test_gist_new_forced_dupe(cmd):
    r = cmd(
        'gist', 'new',
        '-f', 'duped.dat', str(FILEDIR/'lorem.txt'),
        '-f', 'duped.dat', str(FILEDIR/'life.py'),
    )
    assert r.exit_code == 0
    assert r.output == '''\
{
    "comments": 0,
    "created_at": "2017-08-02T18:23:51Z",
    "description": null,
    "files": {
        "duped.dat": {
            "filename": "duped.dat",
            "language": null,
            "raw_url": "https://gist.githubusercontent.com/jwodder/493ee12c1af8825cb706735f95b34bad/raw/f3e251d5db162c0fb419bd3179b120f522c6ee83/duped.dat",
            "size": 600,
            "truncated": false,
            "type": "text/plain"
        }
    },
    "forks": [],
    "git_pull_url": "https://gist.github.com/493ee12c1af8825cb706735f95b34bad.git",
    "html_url": "https://gist.github.com/493ee12c1af8825cb706735f95b34bad",
    "id": "493ee12c1af8825cb706735f95b34bad",
    "owner": "jwodder",
    "public": true,
    "updated_at": "2017-08-02T18:23:51Z",
    "url": "https://api.github.com/gists/493ee12c1af8825cb706735f95b34bad"
}
'''

def test_gist_show_bad_implicit_repo(nullcmd, mocker):
    mocker.patch(
        'ghutil.git.get_remote_url',
        return_value='git@github.com:jwodder/ghutil.git',
    )
    r = nullcmd('gist', 'show')
    assert r.exit_code != 0
    assert r.output == '''\
Usage: gh gist show [OPTIONS] [GISTS]...

Error: Not a gist remote: git@github.com:jwodder/ghutil.git
'''
    git.get_remote_url.assert_called_once_with()

def test_gist_show_bad_explicit_repo(nullcmd, mocker):
    mocker.patch(
        'ghutil.git.get_remote_url',
        return_value='git@github.com:jwodder/ghutil.git',
    )
    r = nullcmd('gist', 'show', '/some/path')
    assert r.exit_code != 0
    assert r.output == '''\
Usage: gh gist show [OPTIONS] [GISTS]...

Error: Not a gist remote: git@github.com:jwodder/ghutil.git
'''
    git.get_remote_url.assert_called_once_with(chdir='/some/path')

def test_gist_web_fork(cmd, mocker):
    mocker.patch('webbrowser.open_new')
    r = cmd('--debug', 'gist', 'web', '4bf350e2d72b547b22dc9de52148ccbe')
    assert r.exit_code == 0, r.output
    assert r.output == '''\
GET https://api.github.com/gists/4bf350e2d72b547b22dc9de52148ccbe
'''
    webbrowser.open_new.assert_called_once_with(
        'https://gist.github.com/4bf350e2d72b547b22dc9de52148ccbe'
    )

# `show` and `web` with no arguments
