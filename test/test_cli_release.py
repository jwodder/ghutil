from   pathlib import Path
import webbrowser
import click
import pytest
from   ghutil  import git

FILEDIR = Path(__file__).with_name('data') / 'files'

LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.  Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.  Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"

def test_release_none(cmd, mocker):
    mocker.patch(
        'ghutil.git.get_remote_url',
        return_value='git@github.com:jwodder/ghutil.git',
    )
    r = cmd('release', 'list')
    assert r.exit_code == 0
    assert r.output == ''
    git.get_remote_url.assert_called_once_with()

def test_release_mockdir(cmd, mocker):
    mocker.patch(
        'ghutil.git.get_remote_url',
        return_value='https://github.com/stedolan/jq.git',
    )
    r = cmd('release', 'list')
    assert r.exit_code == 0
    assert r.output == '''\
stedolan/jq:jq-1.5
stedolan/jq:jq-1.1
stedolan/jq:jq-1.0
stedolan/jq:jq-1.2
stedolan/jq:jq-1.3
stedolan/jq:jq-1.4
stedolan/jq:jq-1.5rc2
stedolan/jq:jq-1.5rc1
'''
    git.get_remote_url.assert_called_once_with()

def test_release_list_qypi(cmd):
    r = cmd('release', 'list', 'qypi')
    assert r.exit_code == 0
    assert r.output == '''\
jwodder/qypi:v0.4.1
jwodder/qypi:v0.4.0
jwodder/qypi:v0.3.0
jwodder/qypi:v0.2.0
jwodder/qypi:v0.1.0.post1
jwodder/qypi:v0.1.0
'''

def test_release_show(cmd, mocker):
    mocker.patch(
        'ghutil.git.get_remote_url',
        return_value='https://github.com/stedolan/jq.git',
    )
    r = cmd('release', 'show')
    assert r.exit_code == 0
    assert r.output == '''\
[
    {
        "assets": [
            {
                "browser_download_url": "https://github.com/stedolan/jq/releases/download/jq-1.5/jq-1.5.tar.gz",
                "content_type": "application/gzip",
                "created_at": "2015-08-16T05:50:05Z",
                "download_count": 101277,
                "id": 792919,
                "label": null,
                "name": "jq-1.5.tar.gz",
                "size": 739309,
                "state": "uploaded",
                "updated_at": "2015-08-16T05:50:07Z",
                "uploader": "dtolnay",
                "url": "https://api.github.com/repos/stedolan/jq/releases/assets/792919"
            },
            {
                "browser_download_url": "https://github.com/stedolan/jq/releases/download/jq-1.5/jq-1.5.zip",
                "content_type": "application/zip",
                "created_at": "2015-08-16T05:52:16Z",
                "download_count": 757,
                "id": 792924,
                "label": null,
                "name": "jq-1.5.zip",
                "size": 747407,
                "state": "uploaded",
                "updated_at": "2015-08-16T05:52:18Z",
                "uploader": "dtolnay",
                "url": "https://api.github.com/repos/stedolan/jq/releases/assets/792924"
            },
            {
                "browser_download_url": "https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux32",
                "content_type": "application/octet-stream",
                "created_at": "2015-10-23T03:12:42Z",
                "download_count": 33733,
                "id": 967992,
                "label": null,
                "name": "jq-linux32",
                "size": 1600813,
                "state": "uploaded",
                "updated_at": "2015-10-23T03:12:55Z",
                "uploader": "nicowilliams",
                "url": "https://api.github.com/repos/stedolan/jq/releases/assets/967992"
            },
            {
                "browser_download_url": "https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux32-no-oniguruma",
                "content_type": "application/octet-stream",
                "created_at": "2015-10-23T03:12:26Z",
                "download_count": 702,
                "id": 967991,
                "label": null,
                "name": "jq-linux32-no-oniguruma",
                "size": 1307827,
                "state": "uploaded",
                "updated_at": "2015-10-23T03:12:38Z",
                "uploader": "nicowilliams",
                "url": "https://api.github.com/repos/stedolan/jq/releases/assets/967991"
            },
            {
                "browser_download_url": "https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64",
                "content_type": "application/octet-stream",
                "created_at": "2015-08-16T05:19:02Z",
                "download_count": 8572878,
                "id": 792891,
                "label": null,
                "name": "jq-linux64",
                "size": 3027945,
                "state": "uploaded",
                "updated_at": "2015-08-16T05:19:28Z",
                "uploader": "nicowilliams",
                "url": "https://api.github.com/repos/stedolan/jq/releases/assets/792891"
            },
            {
                "browser_download_url": "https://github.com/stedolan/jq/releases/download/jq-1.5/jq-osx-amd64",
                "content_type": "application/octet-stream",
                "created_at": "2015-08-16T06:39:46Z",
                "download_count": 113960,
                "id": 792972,
                "label": null,
                "name": "jq-osx-amd64",
                "size": 649996,
                "state": "uploaded",
                "updated_at": "2015-08-16T06:39:50Z",
                "uploader": "nicowilliams",
                "url": "https://api.github.com/repos/stedolan/jq/releases/assets/792972"
            },
            {
                "browser_download_url": "https://github.com/stedolan/jq/releases/download/jq-1.5/jq-win32.exe",
                "content_type": "application/octet-stream",
                "created_at": "2015-08-16T05:19:02Z",
                "download_count": 9816,
                "id": 792890,
                "label": null,
                "name": "jq-win32.exe",
                "size": 1220806,
                "state": "uploaded",
                "updated_at": "2015-08-16T05:19:14Z",
                "uploader": "nicowilliams",
                "url": "https://api.github.com/repos/stedolan/jq/releases/assets/792890"
            },
            {
                "browser_download_url": "https://github.com/stedolan/jq/releases/download/jq-1.5/jq-win64.exe",
                "content_type": "application/octet-stream",
                "created_at": "2015-08-16T05:19:02Z",
                "download_count": 110679,
                "id": 792892,
                "label": null,
                "name": "jq-win64.exe",
                "size": 2326953,
                "state": "uploaded",
                "updated_at": "2015-08-16T05:19:37Z",
                "uploader": "nicowilliams",
                "url": "https://api.github.com/repos/stedolan/jq/releases/assets/792892"
            }
        ],
        "author": "nicowilliams",
        "body": "Thanks to the 20+ developers who have sent us PRs since 1.4, and the many contributors to issues and the wiki.\\n\\nThe manual for jq 1.5 can be found at https://stedolan.github.io/jq/manual/v1.5/\\n\\nSalient new features since 1.4:\\n- regexp support (using Oniguruma)!\\n- a proper module system\\n  \\n  `import \\"foo/bar\\" as bar; # import foo/bar.jq's defs into a bar::* namespace`\\n  \\n  and\\n  \\n  `include \\"foo/bar\\"; # import foo/bar.jq's defs into the top-level`\\n- destructuring syntax (`. as [$first, $second, {$foo, $bar}] | ...`)\\n- math functions\\n- an online streaming parser\\n- minimal I/O builtions (`inputs`, `debug`)\\n  \\n  One can now write:\\n  \\n  `jq -n 'reduce inputs as $i ( ... )'`\\n  \\n  to reduce inputs in an online way without having to slurp them first!  This works with streaming too.\\n- try/catch, for catching and handling errors (this makes for a dynamic non-local exit system)\\n- a lexical non-local exit system\\n  \\n  One can now say\\n  \\n  `label $foo | ..... | break $foo`\\n  \\n  where the break causes control to return to the label $foo, which\\n  then produces `empty` (backtracks).  There's named and anonymous\\n  labels.\\n- tail call optimization (TCO), which allows efficient recursion in jq\\n- a variety of new control structure builtins (e.g., `while(cond; exp)`, `repeat(exp)`, `until(cond; next)`), many of which internally use TCO\\n- an enhanced form of `reduce`: `foreach exp as $name (init_exp; update_exp; extract_exp)`\\n- the ability to read module data files\\n  \\n  `import \\"foo/bar\\" as $bar; # read foo/bar.json, bind to $bar::bar`\\n- `--argjson var '<JSON text>'`\\n  \\n  Using --arg var <number> bit me too many times :)\\n- `--slurpfile var \\"filename\\"`\\n  \\n  Replaces the `--argfile` form (which is now deprecated but remains for backward compatibility).\\n- support for application/json-seq (RFC7464)\\n- a large variety of new utility functions, many being community contributions (e.g., `bsearch`, for binary searching arrays)\\n- datetime functions\\n- a variety of performance enhancements\\n- `def($a): ...;` is now allowed as an equivalent of `def(a): a as $a | ...;`\\n- test and build improvements, including gcov support\\n\\nLastly, don't forget the wiki!  The wiki has a lot of new content since 1.4, much of it contributed by the community.\\n",
        "created_at": "2015-08-18T04:25:04Z",
        "draft": false,
        "html_url": "https://github.com/stedolan/jq/releases/tag/jq-1.5",
        "id": 1678243,
        "name": "jq 1.5",
        "prerelease": false,
        "published_at": "2015-08-16T06:39:17Z",
        "tag_name": "jq-1.5",
        "tarball_url": "https://api.github.com/repos/stedolan/jq/tarball/jq-1.5",
        "target_commitish": "master",
        "url": "https://api.github.com/repos/stedolan/jq/releases/1678243",
        "zipball_url": "https://api.github.com/repos/stedolan/jq/zipball/jq-1.5"
    }
]
'''
    git.get_remote_url.assert_called_once_with()

def test_release_show_a_bunch(cmd, mocker):
    mocker.patch(
        'ghutil.git.get_remote_url',
        return_value='git@github.com:jwodder/daemail.git',
    )
    r = cmd(
        'release', 'show',
        ':v0.5.0',
        'qypi:',
        'stedolan/jq:',
        'TomasTomecek/sen:0.5.0',
        'https://github.com/nlohmann/json/releases/tag/v2.0.10',
    )
    assert r.exit_code == 0
    assert r.output == '''\
[
    {
        "assets": [],
        "author": "jwodder",
        "body": "- `--to-addr` can now be specified on the command line multiple times in order to send to multiple addresses\\n- Arguments to `--to-addr` and `--from-addr` can now be in the form \\"`Real Name <address@example.com>`\\".  `--to-name` and `--from-name` are now deprecated and will be removed in a future version.\\n- If an error occurs during daemonization (e.g., because the `--chdir` argument is not a directory), a normal error traceback will be printed to stderr instead of writing a report to the logfile.\\n",
        "created_at": "2017-02-05T22:01:37Z",
        "draft": false,
        "html_url": "https://github.com/jwodder/daemail/releases/tag/v0.5.0",
        "id": 5365453,
        "name": "Version 0.5.0 — Multiple recipients",
        "prerelease": false,
        "published_at": "2017-02-05T22:04:08Z",
        "tag_name": "v0.5.0",
        "tarball_url": "https://api.github.com/repos/jwodder/daemail/tarball/v0.5.0",
        "target_commitish": "master",
        "url": "https://api.github.com/repos/jwodder/daemail/releases/5365453",
        "zipball_url": "https://api.github.com/repos/jwodder/daemail/zipball/v0.5.0"
    },
    {
        "assets": [],
        "author": "jwodder",
        "body": "**Bugfix**: Better handling of package versions that aren't in PEP 440 normalized form (e.g., \\"`2001.01.01`\\")",
        "created_at": "2017-05-15T14:46:17Z",
        "draft": false,
        "html_url": "https://github.com/jwodder/qypi/releases/tag/v0.4.1",
        "id": 6388802,
        "name": "v0.4.1 — Handle non-normalized versions",
        "prerelease": false,
        "published_at": "2017-05-15T14:46:34Z",
        "tag_name": "v0.4.1",
        "tarball_url": "https://api.github.com/repos/jwodder/qypi/tarball/v0.4.1",
        "target_commitish": "master",
        "url": "https://api.github.com/repos/jwodder/qypi/releases/6388802",
        "zipball_url": "https://api.github.com/repos/jwodder/qypi/zipball/v0.4.1"
    },
    {
        "assets": [
            {
                "browser_download_url": "https://github.com/stedolan/jq/releases/download/jq-1.5/jq-1.5.tar.gz",
                "content_type": "application/gzip",
                "created_at": "2015-08-16T05:50:05Z",
                "download_count": 101277,
                "id": 792919,
                "label": null,
                "name": "jq-1.5.tar.gz",
                "size": 739309,
                "state": "uploaded",
                "updated_at": "2015-08-16T05:50:07Z",
                "uploader": "dtolnay",
                "url": "https://api.github.com/repos/stedolan/jq/releases/assets/792919"
            },
            {
                "browser_download_url": "https://github.com/stedolan/jq/releases/download/jq-1.5/jq-1.5.zip",
                "content_type": "application/zip",
                "created_at": "2015-08-16T05:52:16Z",
                "download_count": 757,
                "id": 792924,
                "label": null,
                "name": "jq-1.5.zip",
                "size": 747407,
                "state": "uploaded",
                "updated_at": "2015-08-16T05:52:18Z",
                "uploader": "dtolnay",
                "url": "https://api.github.com/repos/stedolan/jq/releases/assets/792924"
            },
            {
                "browser_download_url": "https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux32",
                "content_type": "application/octet-stream",
                "created_at": "2015-10-23T03:12:42Z",
                "download_count": 33733,
                "id": 967992,
                "label": null,
                "name": "jq-linux32",
                "size": 1600813,
                "state": "uploaded",
                "updated_at": "2015-10-23T03:12:55Z",
                "uploader": "nicowilliams",
                "url": "https://api.github.com/repos/stedolan/jq/releases/assets/967992"
            },
            {
                "browser_download_url": "https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux32-no-oniguruma",
                "content_type": "application/octet-stream",
                "created_at": "2015-10-23T03:12:26Z",
                "download_count": 702,
                "id": 967991,
                "label": null,
                "name": "jq-linux32-no-oniguruma",
                "size": 1307827,
                "state": "uploaded",
                "updated_at": "2015-10-23T03:12:38Z",
                "uploader": "nicowilliams",
                "url": "https://api.github.com/repos/stedolan/jq/releases/assets/967991"
            },
            {
                "browser_download_url": "https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64",
                "content_type": "application/octet-stream",
                "created_at": "2015-08-16T05:19:02Z",
                "download_count": 8572878,
                "id": 792891,
                "label": null,
                "name": "jq-linux64",
                "size": 3027945,
                "state": "uploaded",
                "updated_at": "2015-08-16T05:19:28Z",
                "uploader": "nicowilliams",
                "url": "https://api.github.com/repos/stedolan/jq/releases/assets/792891"
            },
            {
                "browser_download_url": "https://github.com/stedolan/jq/releases/download/jq-1.5/jq-osx-amd64",
                "content_type": "application/octet-stream",
                "created_at": "2015-08-16T06:39:46Z",
                "download_count": 113960,
                "id": 792972,
                "label": null,
                "name": "jq-osx-amd64",
                "size": 649996,
                "state": "uploaded",
                "updated_at": "2015-08-16T06:39:50Z",
                "uploader": "nicowilliams",
                "url": "https://api.github.com/repos/stedolan/jq/releases/assets/792972"
            },
            {
                "browser_download_url": "https://github.com/stedolan/jq/releases/download/jq-1.5/jq-win32.exe",
                "content_type": "application/octet-stream",
                "created_at": "2015-08-16T05:19:02Z",
                "download_count": 9816,
                "id": 792890,
                "label": null,
                "name": "jq-win32.exe",
                "size": 1220806,
                "state": "uploaded",
                "updated_at": "2015-08-16T05:19:14Z",
                "uploader": "nicowilliams",
                "url": "https://api.github.com/repos/stedolan/jq/releases/assets/792890"
            },
            {
                "browser_download_url": "https://github.com/stedolan/jq/releases/download/jq-1.5/jq-win64.exe",
                "content_type": "application/octet-stream",
                "created_at": "2015-08-16T05:19:02Z",
                "download_count": 110679,
                "id": 792892,
                "label": null,
                "name": "jq-win64.exe",
                "size": 2326953,
                "state": "uploaded",
                "updated_at": "2015-08-16T05:19:37Z",
                "uploader": "nicowilliams",
                "url": "https://api.github.com/repos/stedolan/jq/releases/assets/792892"
            }
        ],
        "author": "nicowilliams",
        "body": "Thanks to the 20+ developers who have sent us PRs since 1.4, and the many contributors to issues and the wiki.\\n\\nThe manual for jq 1.5 can be found at https://stedolan.github.io/jq/manual/v1.5/\\n\\nSalient new features since 1.4:\\n- regexp support (using Oniguruma)!\\n- a proper module system\\n  \\n  `import \\"foo/bar\\" as bar; # import foo/bar.jq's defs into a bar::* namespace`\\n  \\n  and\\n  \\n  `include \\"foo/bar\\"; # import foo/bar.jq's defs into the top-level`\\n- destructuring syntax (`. as [$first, $second, {$foo, $bar}] | ...`)\\n- math functions\\n- an online streaming parser\\n- minimal I/O builtions (`inputs`, `debug`)\\n  \\n  One can now write:\\n  \\n  `jq -n 'reduce inputs as $i ( ... )'`\\n  \\n  to reduce inputs in an online way without having to slurp them first!  This works with streaming too.\\n- try/catch, for catching and handling errors (this makes for a dynamic non-local exit system)\\n- a lexical non-local exit system\\n  \\n  One can now say\\n  \\n  `label $foo | ..... | break $foo`\\n  \\n  where the break causes control to return to the label $foo, which\\n  then produces `empty` (backtracks).  There's named and anonymous\\n  labels.\\n- tail call optimization (TCO), which allows efficient recursion in jq\\n- a variety of new control structure builtins (e.g., `while(cond; exp)`, `repeat(exp)`, `until(cond; next)`), many of which internally use TCO\\n- an enhanced form of `reduce`: `foreach exp as $name (init_exp; update_exp; extract_exp)`\\n- the ability to read module data files\\n  \\n  `import \\"foo/bar\\" as $bar; # read foo/bar.json, bind to $bar::bar`\\n- `--argjson var '<JSON text>'`\\n  \\n  Using --arg var <number> bit me too many times :)\\n- `--slurpfile var \\"filename\\"`\\n  \\n  Replaces the `--argfile` form (which is now deprecated but remains for backward compatibility).\\n- support for application/json-seq (RFC7464)\\n- a large variety of new utility functions, many being community contributions (e.g., `bsearch`, for binary searching arrays)\\n- datetime functions\\n- a variety of performance enhancements\\n- `def($a): ...;` is now allowed as an equivalent of `def(a): a as $a | ...;`\\n- test and build improvements, including gcov support\\n\\nLastly, don't forget the wiki!  The wiki has a lot of new content since 1.4, much of it contributed by the community.\\n",
        "created_at": "2015-08-18T04:25:04Z",
        "draft": false,
        "html_url": "https://github.com/stedolan/jq/releases/tag/jq-1.5",
        "id": 1678243,
        "name": "jq 1.5",
        "prerelease": false,
        "published_at": "2015-08-16T06:39:17Z",
        "tag_name": "jq-1.5",
        "tarball_url": "https://api.github.com/repos/stedolan/jq/tarball/jq-1.5",
        "target_commitish": "master",
        "url": "https://api.github.com/repos/stedolan/jq/releases/1678243",
        "zipball_url": "https://api.github.com/repos/stedolan/jq/zipball/jq-1.5"
    },
    {
        "assets": [],
        "author": "TomasTomecek",
        "body": "## 0.5.0\\n\\n### Features\\n- Realtime events from docker daemon refresh container info and image info buffers.\\n- Layer size is now displayed in layer tree view. [#115](https://github.com/TomasTomecek/sen/issues/115)\\n- ANSI escape sequences are now stripped from container logs. [#67](https://github.com/TomasTomecek/sen/issues/67)\\n\\n### Bug fixes\\n- Viewing container logs should no longer break sen's interface. [#112](https://github.com/TomasTomecek/sen/issues/112)\\n- Various issues, race conditions, code quality and performance was either fixed or improved.\\n",
        "created_at": "2017-01-04T10:35:54Z",
        "draft": false,
        "html_url": "https://github.com/TomasTomecek/sen/releases/tag/0.5.0",
        "id": 5065008,
        "name": "0.5.0",
        "prerelease": false,
        "published_at": "2017-01-04T10:37:04Z",
        "tag_name": "0.5.0",
        "tarball_url": "https://api.github.com/repos/TomasTomecek/sen/tarball/0.5.0",
        "target_commitish": "master",
        "url": "https://api.github.com/repos/TomasTomecek/sen/releases/5065008",
        "zipball_url": "https://api.github.com/repos/TomasTomecek/sen/zipball/0.5.0"
    },
    {
        "assets": [
            {
                "browser_download_url": "https://github.com/nlohmann/json/releases/download/v2.0.10/json.hpp",
                "content_type": "application/octet-stream",
                "created_at": "2017-01-02T15:43:21Z",
                "download_count": 891,
                "id": 2914608,
                "label": null,
                "name": "json.hpp",
                "size": 418409,
                "state": "uploaded",
                "updated_at": "2017-01-02T15:43:23Z",
                "uploader": "nlohmann",
                "url": "https://api.github.com/repos/nlohmann/json/releases/assets/2914608"
            },
            {
                "browser_download_url": "https://github.com/nlohmann/json/releases/download/v2.0.10/json.hpp.asc",
                "content_type": "text/plain",
                "created_at": "2017-02-25T16:31:50Z",
                "download_count": 3,
                "id": 3274645,
                "label": null,
                "name": "json.hpp.asc",
                "size": 801,
                "state": "uploaded",
                "updated_at": "2017-02-25T16:31:51Z",
                "uploader": "nlohmann",
                "url": "https://api.github.com/repos/nlohmann/json/releases/assets/3274645"
            }
        ],
        "author": "nlohmann",
        "body": "- Release date: 2017-01-02\\r\\n- SHA-256: ec27d4e74e9ce0f78066389a70724afd07f10761009322dc020656704ad5296d\\r\\n\\r\\n### Summary\\r\\n\\r\\nThis release fixes several security-relevant bugs in the MessagePack and CBOR parsers. The fixes are backwards compatible.\\r\\n\\r\\n### Changes\\r\\n- :bug: Fixed a lot of **bugs in the CBOR and MesssagePack parsers**. These bugs occurred if invalid input was parsed and then could lead in buffer overflows. These bugs were found with Google's [OSS-Fuzz](https://github.com/google/oss-fuzz), see #405, #407, #408, #409, #411, and #412 for more information.\\r\\n- :construction_worker: We now also use the **[Doozer](https://doozer.io) continuous integration platform**.\\r\\n- :construction_worker: The complete test suite is now also run with **Clang's address sanitizer and undefined-behavior sanitizer**.\\r\\n- :white_check_mark: Overworked **fuzz testing**; CBOR and MessagePack implementations are now fuzz-tested. Furthermore, all fuzz tests now include a round trip which ensures created output can again be properly parsed and yields the same JSON value.\\r\\n- :memo: Clarified documentation of `find()` function to always return `end()` when called on non-object value types.\\r\\n- :hammer: Moved thirdparty test code to `test/thirdparty` directory.",
        "created_at": "2017-01-02T15:38:23Z",
        "draft": false,
        "html_url": "https://github.com/nlohmann/json/releases/tag/v2.0.10",
        "id": 5048008,
        "name": "JSON for Modern C++ Version 2.0.10",
        "prerelease": false,
        "published_at": "2017-01-02T15:39:14Z",
        "tag_name": "v2.0.10",
        "tarball_url": "https://api.github.com/repos/nlohmann/json/tarball/v2.0.10",
        "target_commitish": "develop",
        "url": "https://api.github.com/repos/nlohmann/json/releases/5048008",
        "zipball_url": "https://api.github.com/repos/nlohmann/json/zipball/v2.0.10"
    }
]
'''
    git.get_remote_url.assert_called_once_with()

def test_release_show_bad_implicit_repo(nullcmd, mocker):
    mocker.patch(
        'ghutil.git.get_remote_url',
        return_value='/home/jwodder/git/private.git',
    )
    r = nullcmd('release', 'show')
    assert r.exit_code != 0
    assert r.output == '''\
Usage: gh release show [OPTIONS] [RELEASES]...

Error: Not a GitHub remote: /home/jwodder/git/private.git
'''
    git.get_remote_url.assert_called_once_with()

@pytest.mark.usefixtures('test_repo')
def test_release_show_latest(cmd):
    r = cmd('release', 'show', 'latest')
    assert r.exit_code == 0
    assert r.output == '''\
[
    {
        "assets": [],
        "author": "jwodder",
        "body": "This is the latest release.\\n",
        "created_at": "2017-08-12T18:49:37Z",
        "draft": false,
        "html_url": "https://github.com/jwodder/test/releases/tag/v100.1",
        "id": 7371148,
        "name": "Version 100.1",
        "prerelease": false,
        "published_at": "2017-08-12T18:52:16Z",
        "tag_name": "v100.1",
        "tarball_url": "https://api.github.com/repos/jwodder/test/tarball/v100.1",
        "target_commitish": "master",
        "url": "https://api.github.com/repos/jwodder/test/releases/7371148",
        "zipball_url": "https://api.github.com/repos/jwodder/test/zipball/v100.1"
    }
]
'''

@pytest.mark.usefixtures('test_repo')
def test_release_show_colon_latest(cmd):
    r = cmd('release', 'show', ':latest')
    assert r.exit_code == 0
    assert r.output == '''\
[
    {
        "assets": [],
        "author": "jwodder",
        "body": "This is a release tagged \\"latest\\".\\n",
        "created_at": "2017-08-12T18:49:04Z",
        "draft": false,
        "html_url": "https://github.com/jwodder/test/releases/tag/latest",
        "id": 7371143,
        "name": "Pseudo-latest",
        "prerelease": false,
        "published_at": "2017-08-12T18:51:01Z",
        "tag_name": "latest",
        "tarball_url": "https://api.github.com/repos/jwodder/test/tarball/latest",
        "target_commitish": "master",
        "url": "https://api.github.com/repos/jwodder/test/releases/7371143",
        "zipball_url": "https://api.github.com/repos/jwodder/test/zipball/latest"
    }
]
'''

@pytest.mark.usefixtures('test_repo')
def test_release_attach_text(cmd):
    r = cmd('--debug', 'release', 'attach', 'latest', str(FILEDIR/'lorem.txt'))
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/releases/latest
POST https://uploads.github.com/repos/jwodder/test/releases/7620310/assets?name=lorem.txt
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.  Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.  Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

{
    "browser_download_url": "https://github.com/jwodder/test/releases/download/v0.0.0/lorem.txt",
    "content_type": "text/plain",
    "created_at": "2017-09-04T00:30:14Z",
    "download_count": 0,
    "id": 4737049,
    "label": "",
    "name": "lorem.txt",
    "size": 450,
    "state": "uploaded",
    "updated_at": "2017-09-04T00:30:14Z",
    "uploader": "jwodder",
    "url": "https://api.github.com/repos/jwodder/test/releases/assets/4737049"
}
'''

@pytest.mark.usefixtures('test_repo')
def test_release_attach_named_text(cmd):
    r = cmd(
        'release', 'attach',
        '-n', 'lorem.html',
        'latest',
        str(FILEDIR/'lorem.txt'),
    )
    assert r.exit_code == 0
    assert r.output == '''\
{
    "browser_download_url": "https://github.com/jwodder/test/releases/download/v0.0.0/lorem.html",
    "content_type": "text/html",
    "created_at": "2017-09-04T00:39:07Z",
    "download_count": 0,
    "id": 4737064,
    "label": "",
    "name": "lorem.html",
    "size": 450,
    "state": "uploaded",
    "updated_at": "2017-09-04T00:39:07Z",
    "uploader": "jwodder",
    "url": "https://api.github.com/repos/jwodder/test/releases/assets/4737064"
}
'''

@pytest.mark.usefixtures('test_repo')
def test_release_attach_named_typed_text(cmd):
    r = cmd(
        'release', 'attach',
        '-n', 'lorem.html',
        '--content-type', 'text/plain',
        'latest',
        str(FILEDIR/'lorem.txt'),
    )
    assert r.exit_code == 0
    assert r.output == '''\
{
    "browser_download_url": "https://github.com/jwodder/test/releases/download/v0.0.0/lorem.html",
    "content_type": "text/plain",
    "created_at": "2017-09-04T01:09:27Z",
    "download_count": 0,
    "id": 4737162,
    "label": "",
    "name": "lorem.html",
    "size": 450,
    "state": "uploaded",
    "updated_at": "2017-09-04T01:09:27Z",
    "uploader": "jwodder",
    "url": "https://api.github.com/repos/jwodder/test/releases/assets/4737162"
}
'''

@pytest.mark.usefixtures('test_repo')
def test_release_attach_labelled_text(cmd):
    r = cmd(
        '--debug',
        'release', 'attach',
        '-lAbout',
        'latest',
        str(FILEDIR/'lorem.txt'),
    )
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/releases/latest
POST https://uploads.github.com/repos/jwodder/test/releases/7620310/assets?name=lorem.txt&label=About
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.  Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.  Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

{
    "browser_download_url": "https://github.com/jwodder/test/releases/download/v0.0.0/lorem.txt",
    "content_type": "text/plain",
    "created_at": "2017-09-04T01:13:55Z",
    "download_count": 0,
    "id": 4737174,
    "label": "About",
    "name": "lorem.txt",
    "size": 450,
    "state": "uploaded",
    "updated_at": "2017-09-04T01:13:55Z",
    "uploader": "jwodder",
    "url": "https://api.github.com/repos/jwodder/test/releases/assets/4737174"
}
'''

@pytest.mark.usefixtures('test_repo')
def test_release_attach_binary(cmd):
    r = cmd('release', 'attach', 'latest', str(FILEDIR/'blob.png'))
    assert r.exit_code == 0
    assert r.output == '''\
{
    "browser_download_url": "https://github.com/jwodder/test/releases/download/v0.0.0/blob.png",
    "content_type": "image/png",
    "created_at": "2017-09-04T00:44:01Z",
    "download_count": 0,
    "id": 4737084,
    "label": "",
    "name": "blob.png",
    "size": 208,
    "state": "uploaded",
    "updated_at": "2017-09-04T00:44:01Z",
    "uploader": "jwodder",
    "url": "https://api.github.com/repos/jwodder/test/releases/assets/4737084"
}
'''

@pytest.mark.usefixtures('test_repo')
def test_release_attach_unknown_type(cmd):
    r = cmd('release', 'attach', 'latest', str(FILEDIR/'lorem'))
    assert r.exit_code == 0
    assert r.output == '''\
{
    "browser_download_url": "https://github.com/jwodder/test/releases/download/v0.0.0/lorem",
    "content_type": "application/octet-stream",
    "created_at": "2017-09-04T01:18:48Z",
    "download_count": 0,
    "id": 4737189,
    "label": "",
    "name": "lorem",
    "size": 450,
    "state": "uploaded",
    "updated_at": "2017-09-04T01:18:48Z",
    "uploader": "jwodder",
    "url": "https://api.github.com/repos/jwodder/test/releases/assets/4737189"
}
'''

@pytest.mark.usefixtures('test_repo')
def test_release_unattach(cmd):
    r = cmd('--debug', 'release', 'unattach', '--force', 'latest', 'lorem.txt')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/releases/latest
DELETE https://api.github.com/repos/jwodder/test/releases/assets/4737049
Asset lorem.txt deleted
'''

@pytest.mark.usefixtures('test_repo')
def test_release_new(cmd):
    r = cmd(
        '--debug',
        'release', 'new',
        '-nInit',
        '--body', str(FILEDIR/'lorem.txt'),
        'v0.0.0',
    )
    assert r.exit_code == 0
    assert r.output == '''\
POST https://api.github.com/repos/jwodder/test/releases
{
    "body": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.  Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.  Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\\n",
    "draft": false,
    "name": "Init",
    "prerelease": false,
    "tag_name": "v0.0.0"
}
{
    "assets": [],
    "author": "jwodder",
    "body": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.  Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.  Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\\n",
    "created_at": "2017-09-24T23:46:48Z",
    "draft": false,
    "html_url": "https://github.com/jwodder/test/releases/tag/v0.0.0",
    "id": 7871180,
    "name": "Init",
    "prerelease": false,
    "published_at": "2017-09-25T00:05:35Z",
    "tag_name": "v0.0.0",
    "tarball_url": "https://api.github.com/repos/jwodder/test/tarball/v0.0.0",
    "target_commitish": "master",
    "url": "https://api.github.com/repos/jwodder/test/releases/7871180",
    "zipball_url": "https://api.github.com/repos/jwodder/test/zipball/v0.0.0"
}
'''

@pytest.mark.usefixtures('test_repo')
def test_release_new_edit_body(cmd, mocker):
    HEADERS = 'Tag-Name: v0.0.0\n' \
              'Name: Init\n' \
              'Draft: no\n' \
              'Prerelease: no\n'
    mocker.patch('click.edit', return_value=HEADERS + '\n' + LOREM)
    r = cmd(
        '--debug',
        'release', 'new',
        '-nInit',
        'v0.0.0',
    )
    assert r.exit_code == 0
    assert r.output == '''\
POST https://api.github.com/repos/jwodder/test/releases
{
    "body": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.  Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.  Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\\n",
    "draft": false,
    "name": "Init",
    "prerelease": false,
    "tag_name": "v0.0.0"
}
{
    "assets": [],
    "author": "jwodder",
    "body": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.  Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.  Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\\n",
    "created_at": "2017-09-24T23:46:48Z",
    "draft": false,
    "html_url": "https://github.com/jwodder/test/releases/tag/v0.0.0",
    "id": 7871180,
    "name": "Init",
    "prerelease": false,
    "published_at": "2017-09-25T00:05:35Z",
    "tag_name": "v0.0.0",
    "tarball_url": "https://api.github.com/repos/jwodder/test/tarball/v0.0.0",
    "target_commitish": "master",
    "url": "https://api.github.com/repos/jwodder/test/releases/7871180",
    "zipball_url": "https://api.github.com/repos/jwodder/test/zipball/v0.0.0"
}
'''
    click.edit.assert_called_once_with(HEADERS+'\n', require_save=True)

@pytest.mark.usefixtures('test_repo')
def test_release_new_edit_name(cmd, mocker):
    HEADERS = 'Tag-Name: v0.0.0\n' \
              'Name: Init\n' \
              'Draft: no\n' \
              'Prerelease: no\n'
    mocker.patch('click.edit', return_value=HEADERS + '\n' + LOREM)
    r = cmd(
        '--debug',
        'release', 'new',
        '--body', str(FILEDIR/'lorem.txt'),
        'v0.0.0',
    )
    assert r.exit_code == 0
    assert r.output == '''\
POST https://api.github.com/repos/jwodder/test/releases
{
    "body": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.  Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.  Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\\n",
    "draft": false,
    "name": "Init",
    "prerelease": false,
    "tag_name": "v0.0.0"
}
{
    "assets": [],
    "author": "jwodder",
    "body": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.  Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.  Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\\n",
    "created_at": "2017-09-24T23:46:48Z",
    "draft": false,
    "html_url": "https://github.com/jwodder/test/releases/tag/v0.0.0",
    "id": 7871180,
    "name": "Init",
    "prerelease": false,
    "published_at": "2017-09-25T00:05:35Z",
    "tag_name": "v0.0.0",
    "tarball_url": "https://api.github.com/repos/jwodder/test/tarball/v0.0.0",
    "target_commitish": "master",
    "url": "https://api.github.com/repos/jwodder/test/releases/7871180",
    "zipball_url": "https://api.github.com/repos/jwodder/test/zipball/v0.0.0"
}
'''
    click.edit.assert_called_once_with(
        'Tag-Name: v0.0.0\nName: \nDraft: no\nPrerelease: no\n\n' + LOREM,
        require_save=True,
    )

@pytest.mark.usefixtures('test_repo')
def test_release_new_no_name_no_body(cmd, mocker):
    EDIT = 'Tag-Name: v0.0.0\n' \
           'Name: \n' \
           'Draft: no\n' \
           'Prerelease: no\n\n'
    mocker.patch('click.edit', return_value=EDIT)
    r = cmd('--debug', 'release', 'new', 'v0.0.0')
    assert r.exit_code == 0
    assert r.output == '''\
POST https://api.github.com/repos/jwodder/test/releases
{
    "body": "",
    "draft": false,
    "name": "",
    "prerelease": false,
    "tag_name": "v0.0.0"
}
{
    "assets": [],
    "author": "jwodder",
    "body": "",
    "created_at": "2017-09-24T23:46:48Z",
    "draft": false,
    "html_url": "https://github.com/jwodder/test/releases/tag/v0.0.0",
    "id": 7895578,
    "name": "",
    "prerelease": false,
    "published_at": "2017-09-26T15:02:29Z",
    "tag_name": "v0.0.0",
    "tarball_url": "https://api.github.com/repos/jwodder/test/tarball/v0.0.0",
    "target_commitish": "master",
    "url": "https://api.github.com/repos/jwodder/test/releases/7895578",
    "zipball_url": "https://api.github.com/repos/jwodder/test/zipball/v0.0.0"
}
'''
    click.edit.assert_called_once_with(EDIT, require_save=True)

def test_release_new_no_name_no_body_no_save(nullcmd, mocker):
    EDIT = 'Tag-Name: v0.0.0\n' \
           'Name: \n' \
           'Draft: no\n' \
           'Prerelease: no\n\n'
    mocker.patch('click.edit', return_value=None)
    r = nullcmd('--debug', 'release', 'new', 'v0.0.0')
    assert r.exit_code == 0
    assert r.output == 'No changes saved; exiting\n'
    click.edit.assert_called_once_with(EDIT, require_save=True)

def test_release_new_delete_tag_name(nullcmd, mocker):
    EDIT = 'Tag-Name: v0.0.0\n' \
           'Name: \n' \
           'Draft: no\n' \
           'Prerelease: no\n\n'
    mocker.patch('click.edit', return_value='Tag-name: \n')
    r = nullcmd('--debug', 'release', 'new', 'v0.0.0')
    assert r.exit_code == 0
    assert r.output == 'Aborting release due to empty tag name\n'
    click.edit.assert_called_once_with(EDIT, require_save=True)

@pytest.mark.usefixtures('test_repo')
def test_release_edit_name(cmd):
    r = cmd('--debug', 'release', 'edit', '--name=Initial Release', 'v0.0.0')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/releases/tags/v0.0.0
PATCH https://api.github.com/repos/jwodder/test/releases/7871180
{
    "name": "Initial Release"
}
'''

@pytest.mark.usefixtures('test_repo')
def test_release_edit_name_editor(cmd, mocker):
    mocker.patch('click.edit', return_value="Name: Initial Release\n")
    r = cmd('--debug', 'release', 'edit', 'v0.0.0')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/releases/tags/v0.0.0
PATCH https://api.github.com/repos/jwodder/test/releases/7871180
{
    "name": "Initial Release"
}
'''
    click.edit.assert_called_once_with(
        'Tag-Name: v0.0.0\n'
        'Name: Init\n'
        'Draft: no\n'
        'Prerelease: no\n'
        '\n' + LOREM,
        require_save=True,
    )

@pytest.mark.usefixtures('test_repo')
def test_release_edit_body(cmd):
    r = cmd(
        '--debug',
        'release', 'edit',
        '--body=' + str(FILEDIR/'label.json'),
        'v0.0.0',
    )
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/releases/tags/v0.0.0
PATCH https://api.github.com/repos/jwodder/test/releases/7871180
{
    "body": "{\\"name\\": \\"Test Label\\", \\"color\\": \\"FF0000\\"}"
}
'''

@pytest.mark.usefixtures('test_repo')
def test_release_edit_body_editor(cmd, mocker):
    HEADERS = 'Tag-Name: v0.0.0\n' \
              'Name: Initial Release\n' \
              'Draft: no\n' \
              'Prerelease: no\n'
    mocker.patch(
        'click.edit',
        return_value=HEADERS + '\n{"name": "Test Label", "color": "FF0000"}'
    )
    r = cmd('--debug', 'release', 'edit', 'v0.0.0')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/releases/tags/v0.0.0
PATCH https://api.github.com/repos/jwodder/test/releases/7871180
{
    "body": "{\\"name\\": \\"Test Label\\", \\"color\\": \\"FF0000\\"}"
}
'''
    click.edit.assert_called_once_with(HEADERS+'\n'+LOREM, require_save=True)

@pytest.mark.usefixtures('test_repo')
def test_release_edit_nochange(cmd, mocker):
    RELEASE = 'Tag-Name: v0.0.0\n' \
              'Name: Init\n' \
              'Draft: no\n' \
              'Prerelease: no\n' \
              '\n' + LOREM
    mocker.patch('click.edit', return_value=RELEASE)
    r = cmd('--debug', 'release', 'edit', 'v0.0.0')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/releases/tags/v0.0.0
No modifications made; exiting
'''
    click.edit.assert_called_once_with(RELEASE, require_save=True)

@pytest.mark.usefixtures('test_repo')
def test_release_delete_noforce(cmd):
    r = cmd('--debug', 'release', 'delete', 'v0.0.0', input='y\n')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/releases/tags/v0.0.0
Delete release jwodder/test:v0.0.0? [y/N]: y
DELETE https://api.github.com/repos/jwodder/test/releases/7871180
Release jwodder/test:v0.0.0 deleted
'''

@pytest.mark.usefixtures('test_repo')
def test_release_delete_force(cmd):
    r = cmd('--debug', 'release', 'delete', '-f', 'v0.0.0')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/releases/tags/v0.0.0
DELETE https://api.github.com/repos/jwodder/test/releases/7871180
Release jwodder/test:v0.0.0 deleted
'''

@pytest.mark.usefixtures('test_repo')
def test_release_no_delete(cmd):
    r = cmd('--debug', 'release', 'delete', 'v0.0.0', input='n\n')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/releases/tags/v0.0.0
Delete release jwodder/test:v0.0.0? [y/N]: n
Release not deleted
'''

def test_release_web(cmd, mocker):
    mocker.patch(
        'ghutil.git.get_remote_url',
        return_value='https://github.com/stedolan/jq.git',
    )
    mocker.patch('webbrowser.open_new')
    r = cmd('--debug', 'release', 'web')
    assert r.exit_code == 0, r.output
    assert r.output == '''\
GET https://api.github.com/repos/stedolan/jq/releases/latest
'''
    git.get_remote_url.assert_called_once_with()
    webbrowser.open_new.assert_called_once_with(
        'https://github.com/stedolan/jq/releases/tag/jq-1.5'
    )

@pytest.mark.usefixtures('test_repo')
def test_release_web_colon_latest(cmd, mocker):
    mocker.patch('webbrowser.open_new')
    r = cmd('--debug', 'release', 'web', ':latest')
    assert r.exit_code == 0, r.output
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test/releases/tags/latest
'''
    webbrowser.open_new.assert_called_once_with(
        'https://github.com/jwodder/test/releases/tag/latest'
    )

# new: --draft, --published
# new: --prerelease, --full-release
# new: no tag given on command line

# edit: --draft, --published
# edit: --prerelease, --full-release
# edit tag name
