import re
import pytest
from   ghutil.regex import GH_USER_RGX, GH_REPO_RGX, GIT_REFNAME_RGX

@pytest.mark.parametrize('name', [
    'steven-universe',
    'steven',
    's',
    's-u',
    '7152',
    's-t-e-v-e-n',
    's-t-eeeeee-v-e-n',
    'peridot-2F5L-5XG',
    'nonely',
    'none-one',
    'none-none',
    'nonenone',
    'none0',
    '0none',
    # The following are actual usernames on GitHub that violate the current
    # username restrictions:
    '-',
    '-Jerry-',
    '-SFT-Clan',
    '123456----',
    'FirE-Fly-',
    'None-',
    'alex--evil',
    'johan--',
    'pj_nitin',
    'up_the_irons',
])
def test_good_users(name):
    assert bool(re.fullmatch(GH_USER_RGX, name))

@pytest.mark.parametrize('name', [
    'steven.universe',
    'steven-universe@beachcity.dv',
    'steven-univerß',
    '',
    'none',
    'NONE',
])
def test_bad_users(name):
    assert re.fullmatch(GH_USER_RGX, name) is None

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
    '---',
    '.---',
    '.steven',
])
def test_good_repos(repo):
    assert bool(re.fullmatch(GH_REPO_RGX, repo))

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
    assert re.fullmatch(GH_REPO_RGX, repo) is None

@pytest.mark.parametrize('ref', [
    '!"#$%&\'()+,-./;<=>@]_`{|}',
    '-',
    '---',
    '-steven',
    '-steven-',
    '7152',
    '@.tag',
    '@/tag',
    '@tag',
    '\U0001F615',
    '\u2000',
    '_',
    'branch',
    'git',
    'git.steven',
    'latest',
    'lock',
    'peridot-2F5L-5XG',
    's',
    's--u',
    's-t-e-v-e-n',
    's-t-eeeeee-v-e-n',
    's-u',
    'steven',
    'steven-'
    'steven--universe',
    'steven-universe',
    'steven-univerß',
    'steven.git',
    'steven.git.txt',
    'steven.gitt',
    'steven.universe',
    'steven_universe',
    't/a/g',
    'tag',
    'tag./name',
    'tag.@',
    'tag.lock.unlock',
    'tag/@',
    'tag/lock',
    'tag@branch',
    '{@}',
    'ß',
])
def test_good_refnames(ref):
    assert bool(re.fullmatch(GIT_REFNAME_RGX, ref))

@pytest.mark.parametrize('ref', [
    ' ',
    '',
    '*',
    '.',
    '.---',
    '..',
    '...',
    '...git',
    '..git',
    '.git',
    '.gitt',
    '.tag',
    '/',
    '//',
    '/tag',
    ':',
    '?',
    '@',
    '[',
    '\\',
    '\n',
    '^',
    'steven..universe',
    'tag.',
    'tag.lock',
    'tag.lock/name',
    'tag/',
    'tag/.lock',
    'tag/.name',
    'tag//lock',
    'tag@{branch}',
    '~',
])
def test_bad_refnames(ref):
    assert re.fullmatch(GIT_REFNAME_RGX, ref) is None
