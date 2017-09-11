from ghutil import git

# Betamax isn't good with parametrization, and parametrizing lengthy output
# would result in very long cassette file names anyway, so no parametrization
# for me.

REPO_LIST = '''\
jwodder/advent350
jwodder/aptrepo
jwodder/awesome-python
jwodder/binheat
jwodder/bitvector.py
jwodder/caught
jwodder/Chess.hs
jwodder/conjugate
jwodder/daemail
jwodder/doapi
jwodder/envec
jwodder/euler
jwodder/gforth-docker
jwodder/ghutil
jwodder/groups
jwodder/headerparser
jwodder/hsgraphics
jwodder/inplace
jwodder/javaproperties
jwodder/javaproperties-cli
jwodder/jbobaf
jwodder/julian
jwodder/jwodder.github.io
jwodder/lambdas
jwodder/linesep
jwodder/literal_exec
jwodder/logger
jwodder/nethack-docker
jwodder/notesys
jwodder/open-humans-api
jwodder/packaging
jwodder/peps
jwodder/psych
jwodder/python-packaging-user-guide
jwodder/qypi
jwodder/schedule
jwodder/scoreGismu
jwodder/statjson
jwodder/Verity
jwodder/whitaker-docker
jwodder/whitaker2json
jwodder/xattr
'''

def test_repo_list(cmd):
    r = cmd('repo', 'list')
    assert r.exit_code == 0
    assert r.output == REPO_LIST

def test_repo(cmd):
    r = cmd('repo')
    assert r.exit_code == 0
    assert r.output == REPO_LIST

def test_repo_show_ghutil(cmd):
    r = cmd('repo', 'show', 'ghutil')
    assert r.exit_code == 0
    assert r.output == '''\
[
    {
        "clone_url": "https://github.com/jwodder/ghutil.git",
        "created_at": "2017-05-19T19:40:57Z",
        "default_branch": "master",
        "description": "Interact with GitHub from the command line",
        "fork": false,
        "forks_count": 1,
        "full_name": "jwodder/ghutil",
        "git_url": "git://github.com/jwodder/ghutil.git",
        "homepage": null,
        "html_url": "https://github.com/jwodder/ghutil",
        "id": 91839769,
        "language": "Python",
        "license": "MIT",
        "name": "ghutil",
        "network_count": 1,
        "open_issues_count": 1,
        "owner": "jwodder",
        "private": false,
        "pushed_at": "2017-07-20T14:03:23Z",
        "size": 151,
        "ssh_url": "git@github.com:jwodder/ghutil.git",
        "stargazers_count": 3,
        "subscribers_count": 2,
        "topics": [],
        "updated_at": "2017-06-12T16:38:36Z",
        "url": "https://api.github.com/repos/jwodder/ghutil",
        "watchers_count": 3
    }
]
'''

def test_repo_fans_jwodder_ghutil(cmd):
    r = cmd('repo', 'fans', 'jwodder/ghutil')
    assert r.exit_code == 0
    assert r.output == '''\
{
    "forkers": [
        "pombredanne"
    ],
    "stargazers": [
        "jwodder",
        "reduxionist",
        "roscopecoltran"
    ],
    "watchers": [
        "jwodder",
        "roscopecoltran"
    ]
}
'''

def test_repo_starred(cmd):
    r = cmd('repo', 'starred')
    assert r.exit_code == 0
    assert r.output == '''\
john-kurkowski/tldextract
keon/algorithms
vinta/awesome-python
jwodder/ghutil
mitsuhiko/pipsi
rhdunn/ucd-tools
nicowilliams/inplace
nlohmann/json
jwodder/javaproperties-cli
pypa/setuptools
requests/requests
NetHack/NetHack
pret/pokecrystal
jwodder/aptrepo
jwodder/headerparser
jwodder/qypi
jantman/pypi-download-stats
python/cpython
TomasTomecek/sen
pypa/warehouse
pypa/python-packaging-user-guide
jwodder/inplace
jwodder/javaproperties
python/peps
philadams/habitica
digitalocean/do_user_scripts
jwodder/daemail
andreafabrizi/Dropbox-Uploader
veekun/pokedex
certbot/certbot
jwodder/whitaker2json
jwodder/doapi
jwodder/nethack-docker
jwodder/gforth-docker
jwodder/psych
jwodder/scoreGismu
jwodder/advent350
jwodder/julian
jwodder/euler
phusion/baseimage-docker
simplejson/simplejson
HabitRPG/habitica
lojban/cll
cplusplus/draft
rakudo/rakudo
perl6/specs
paxed/Rodney
rakudo/star
perl6/book
'''

def test_repo_network(cmd):
    r = cmd('repo', 'network', 'sgillies/Fiona', color=True)
    assert r.exit_code == 0
    assert r.output == '''\
Toblerity/Fiona
 ├── johnbickmore/Fiona
 ├── Python3pkg/Fiona
 ├── leijiancd/Fiona
 ├── JesseCrocker/Fiona
 ├── QuLogic/Fiona
 ├── youngpm/Fiona
 ├── zandy19/Fiona
 ├── rouault/Fiona
 ├── sunnyk-skk456/Fiona
 ├── wesky93/Fiona
 ├── chefren/Fiona
 ├── shiweihappy/Fiona
 ├── sposs/Fiona
 ├── qinfeng/Fiona
 ├── smnorris/Fiona
 ├── aashish24/Fiona
 ├── imagingearth/Fiona
 ├── techtronics/Fiona
 ├── paladin74/Fiona
 ├── SIGISLV/Fiona
 ├── sebastic/Fiona
 ├── perrygeo/Fiona
 ├── gislite/Fiona
 ├── eotp/Fiona
 ├── antmd/Fiona
 ├── groutr/Fiona
 ├── MatthewArrott/Fiona
 ├── idonglei/Fiona
 ├── cjthomas730/Fiona
 ├── hroncok/Fiona
 ├── geowurster/Fiona
 ├── visr/Fiona
 ├── jdmcbr/Fiona
 ├── dmkent/Fiona
 ├── johanvdw/Fiona
 ├── citterio/Fiona
 ├── jlivni/Fiona
 ├── barrycug/Fiona
 ├── shannonyu/Fiona
 ├── dimlev/Fiona
 ├── rbuffat/Fiona
 ├── mwtoews/Fiona
 ├── walkerjeffd/Fiona
 ├── snorfalorpagus/Fiona
 ├── brendan-ward/Fiona
 ├── kod3r/Fiona
 ├── jonathanrocher/Fiona
 ├── jwass/Fiona
 ├── kjordahl/Fiona
 │   └── mukolx/Fiona
 ├── shakythesherpa/Fiona
 ├── WeatherGod/Fiona
 ├── justb4/Fiona
 ├── wilsaj/Fiona
 ├── igiroux/Fiona
 ├── prologic/Fiona
 ├── ldgeo/Fiona
 ├── fgcartographix/Fiona
 ├── davidmarcus/Fiona
 ├── gridcell/Fiona
 ├── lordi/Fiona
 ├── dandye/Fiona
 ├── olt/Fiona
 ├── paulsmith/Fiona
 ├── steko/Fiona
 ├── ingenieroariel/Fiona
 ├── fredj/Fiona
 ├── aaronr/Fiona
 ├── drwelby/Fiona
 ├── mweisman/Fiona
 └── \x1B[1msgillies/Fiona\x1B[0m
     ├── taoteg/Fiona
     ├── wyom/Fiona
     ├── Joe-Blabbah/Fiona
     └── yuanshankongmeng/Fiona
'''

def test_repo_list_forks(cmd):
    r = cmd('repo', 'list-forks', 'sgillies/Fiona')
    assert r.exit_code == 0
    assert r.output == '''\
taoteg/Fiona
wyom/Fiona
Joe-Blabbah/Fiona
yuanshankongmeng/Fiona
'''

def test_repo_search(cmd):
    r = cmd('repo', 'search', 'halting', 'problem')
    assert r.exit_code == 0
    assert r.output == '''\
ZongzheYuan/HaltingProblem
ForbesLindesay/halting-problem
davidtadams/HaltingProblem
Solidsoft-Reply/Halting
siusoon/halting
ebassi/halting_problem
freddieswift/HaltingProblem
gitpan/Acme-HaltingProblem
GiacomoPinardi/HaltingProblemTuring
jsenko/halting-problem-solver
Tatsuonline/The-Halting-Problem-Ezine
gstark/talk-halting-problem
YorkCodeDojo/TheHaltingProblem
mkotov/htm
mrkline/ece556-router
spruceb/kolmogorov
cloudmine/cm-exitcheck
spiderworthy/getRunningTime
Aearnus/bf-genetic-generator
vincentclee/csci2670-intro_to_theory_of_computation
'''

def test_repo_search_limit(cmd):
    r = cmd('repo', 'search', '--limit', '10', 'halting', 'problem')
    assert r.exit_code == 0
    assert r.output == '''\
ZongzheYuan/HaltingProblem
ForbesLindesay/halting-problem
davidtadams/HaltingProblem
Solidsoft-Reply/Halting
siusoon/halting
ebassi/halting_problem
freddieswift/HaltingProblem
gitpan/Acme-HaltingProblem
GiacomoPinardi/HaltingProblemTuring
jsenko/halting-problem-solver
'''

def test_repo_show_bad_implicit_repo(nullcmd, mocker):
    mocker.patch(
        'ghutil.git.get_remote_url',
        return_value='/home/jwodder/git/private.git',
    )
    r = nullcmd('repo', 'show')
    assert r.exit_code != 0
    assert r.output == '''\
Usage: gh repo show [OPTIONS] [REPOS]...

Error: Not a GitHub remote: /home/jwodder/git/private.git
'''
    git.get_remote_url.assert_called_once_with()

def test_repo_show_bad_explicit_repo(nullcmd, mocker):
    mocker.patch(
        'ghutil.git.get_remote_url',
        return_value='/home/jwodder/git/private.git',
    )
    r = nullcmd('repo', 'show', '/some/path')
    assert r.exit_code != 0
    assert r.output == '''\
Usage: gh repo show [OPTIONS] [REPOS]...

Error: Not a GitHub remote: /home/jwodder/git/private.git
'''
    git.get_remote_url.assert_called_once_with(chdir='/some/path')

def test_repo_new(cmd):
    r = cmd('--debug', 'repo', 'new', 'test')
    assert r.exit_code == 0
    assert r.output == '''\
POST https://api.github.com/user/repos
{
    "allow_merge_commit": true,
    "allow_rebase_merge": true,
    "allow_squash_merge": true,
    "auto_init": false,
    "description": null,
    "gitignore_template": null,
    "has_issues": true,
    "has_wiki": true,
    "homepage": null,
    "license_template": null,
    "name": "test",
    "private": false
}
{
    "clone_url": "https://github.com/jwodder/test.git",
    "created_at": "2017-09-11T15:33:42Z",
    "default_branch": "master",
    "description": null,
    "fork": false,
    "forks_count": 0,
    "full_name": "jwodder/test",
    "git_url": "git://github.com/jwodder/test.git",
    "homepage": null,
    "html_url": "https://github.com/jwodder/test",
    "id": 103154035,
    "language": null,
    "name": "test",
    "network_count": 0,
    "open_issues_count": 0,
    "owner": "jwodder",
    "private": false,
    "pushed_at": "2017-09-11T15:33:42Z",
    "size": 0,
    "ssh_url": "git@github.com:jwodder/test.git",
    "stargazers_count": 0,
    "subscribers_count": 1,
    "topics": [],
    "updated_at": "2017-09-11T15:33:42Z",
    "url": "https://api.github.com/repos/jwodder/test",
    "watchers_count": 0
}
'''

def test_repo_delete_noforce(cmd):
    r = cmd('--debug', 'repo', 'delete', 'jwodder/test', input='y\n')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test
Delete repository jwodder/test? [y/N]: y
DELETE https://api.github.com/repos/jwodder/test
Repository jwodder/test deleted
'''

def test_repo_delete_force(cmd):
    r = cmd('--debug', 'repo', 'delete', '-f', 'jwodder/test')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test
DELETE https://api.github.com/repos/jwodder/test
Repository jwodder/test deleted
'''

def test_repo_no_delete(cmd):
    r = cmd('--debug', 'repo', 'delete', 'jwodder/test', input='n\n')
    assert r.exit_code == 0
    assert r.output == '''\
GET https://api.github.com/repos/jwodder/test
Delete repository jwodder/test? [y/N]: n
Repository not deleted
'''
