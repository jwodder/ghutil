import re
import pytest
from   ghutil.repos import GH_USER_RGX

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
])
def test_bad_users(name):
    assert re.match('^{}$'.format(GH_USER_RGX), name) is None
