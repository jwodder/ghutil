import re
import pytest
from   ghutil.repos import GH_USER_RGX, GH_REPO_RGX

@pytest.mark.parametrize('name', [
    'steven-universe',
    'steven',
    's',
    's-u',
    '7152',
    's-t-e-v-e-n',
    's-t-eeeeee-v-e-n',
    'peridot-2F5L-5XG',
])
def test_good_users(name):
    assert bool(re.match('^{}$'.format(GH_USER_RGX), name))

@pytest.mark.parametrize('name', [
    '-steven',
    'steven-'
    '-steven-',
    'steven.universe',
    'steven_universe',
    'steven-univerß',
    'steven--universe',
    's--u',
    '-',
    '',
])
def test_bad_users(name):
    assert re.match('^{}$'.format(GH_USER_RGX), name) is None

@pytest.mark.parametrize('repo', [
    'steven-universe',
    'steven',
    's',
    's-u',
    '7152',
    's-t-e-v-e-n',
    's-t-eeeeee-v-e-n',
    'peridot-2F5L-5XG',
    '...',
    '-steven',
    'steven-'
    '-steven-',
    'steven.universe',
    'steven_universe',
    'steven--universe',
    's--u',
    'git.steven',
    'steven.git.txt',
    'steven.gitt',
    '.gitt',
    'git',
    '-',
    '_',
])
def test_good_repos(repo):
    assert bool(re.match('^{}$'.format(GH_REPO_RGX), repo))

@pytest.mark.parametrize('repo', [
    'steven-univerß',
    '.',
    '..',
    '...git',
    '..git',
    '.git',
    '',
    'steven.git',
])
def test_bad_repos(repo):
    assert re.match('^{}$'.format(GH_REPO_RGX), repo) is None
