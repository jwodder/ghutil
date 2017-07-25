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
    ### TODO: Try to preserve (and test) the bolding of the command-line
    ### argument
    r = cmd('repo', 'network', 'sgillies/Fiona')
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
 └── sgillies/Fiona
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

# repo search
