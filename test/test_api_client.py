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
])
def test_accept_configged(tmpdir, config, accept_header):
    cfg = tmpdir.join('config.cfg')
    cfg.write(config)
    gh = GitHub()
    gh.configure(str(cfg))
    assert gh.session.headers["Accept"] == accept_header
