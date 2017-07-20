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
