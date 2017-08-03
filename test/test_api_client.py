import os
import pytest
from   ghutil.api.client import ACCEPT, GitHub

def test_accept_noconfig():
    gh = GitHub()
    assert gh.session.headers["Accept"] == ACCEPT

def test_accept_nullconfig():
    gh = GitHub()
    gh.configure(os.devnull)
    assert gh.session.headers["Accept"] == ACCEPT

@pytest.mark.parametrize('config,accept_header', [
    ('', ACCEPT),
    ('[api]', ACCEPT),
    ('[api]\naccept =\n', ACCEPT),
    ('[api]\naccept = \n', ACCEPT),
    ('[api]\naccept = ' + ACCEPT, ACCEPT + ',' + ACCEPT),
    (
        '[api]\naccept = application/vnd.github.batman-preview+json\n',
        ACCEPT + ',application/vnd.github.batman-preview+json',
    ),
    (
        '[api]\n'
        'accept = application/vnd.github.batman-preview+json\n'
        '    text/plain\n',
        ACCEPT + ',application/vnd.github.batman-preview+json,text/plain',
    ),
    (
        '[api]\n'
        'accept =\n'
        '    application/vnd.github.batman-preview+json\n'
        '    text/plain\n',
        ACCEPT + ',application/vnd.github.batman-preview+json,text/plain',
    ),
    (
        '[api]\n'
        'accept =\n'
        '    application/vnd.github.batman-preview+json,\n'
        '    text/plain,\n',
        ACCEPT + ',application/vnd.github.batman-preview+json,text/plain'
    ),
    (
        '[api]\n'
        'accept =\n'
        '    application/vnd.github.batman-preview+json\n'
        '\n'
        '    text/plain\n',
        ACCEPT + ',application/vnd.github.batman-preview+json,text/plain'
    ),
    (
        '[api]\n'
        'accept =\n'
        '    application/vnd.github.batman-preview+json\n'
        '    \n'
        '    text/plain\n',
        ACCEPT + ',application/vnd.github.batman-preview+json,text/plain'
    ),
    (
        '[api]\n'
        'accept =\n'
        '    application/vnd.github.batman-preview+json\n'
        '    text/plain, application/octet-stream\n',
        ACCEPT + ',application/vnd.github.batman-preview+json,text/plain,'
                 ' application/octet-stream',
    ),
    ('[api]\nappend-accept = false', ACCEPT),
    ('[api]\naccept =\nappend-accept = false', None),
    ('[api]\naccept = text/plain\nappend-accept = false', 'text/plain'),
    ('[api]\nappend-accept = true', ACCEPT),
    ('[api]\naccept =\nappend-accept = true', ACCEPT),
    ('[api]\naccept = text/plain\nappend-accept = true', ACCEPT+',text/plain'),
])
def test_accept_configged(tmpdir, config, accept_header):
    cfg = tmpdir.join('config.cfg')
    cfg.write(config)
    gh = GitHub()
    gh.configure(str(cfg))
    assert gh.session.headers.get("Accept") == accept_header

@pytest.mark.parametrize('config,auth_header,auth_basic', [
    ('', None, None),
    (
        '[api.auth]\ntoken = legitimateoauthtoken\n',
        'token legitimateoauthtoken',
        None,
    ),
    (
        '[api.auth]\nusername = l.user\npassword = hunter2\n',
        None,
        ('l.user', 'hunter2'),
    ),
    (
        '[api.auth]\n'
        'token = legitimateoauthtoken\n'
        'username = l.user\n'
        'password = hunter2\n',
        'token legitimateoauthtoken',
        None,
    ),
])
def test_auth_config(tmpdir, config, auth_header, auth_basic):
    cfg = tmpdir.join('config.cfg')
    cfg.write(config)
    gh = GitHub()
    gh.configure(str(cfg))
    assert gh.session.headers.get("Authorization") == auth_header
    assert gh.session.auth == auth_basic
