import json
import netrc
import tempfile
from   click.testing       import CliRunner
import pytest
import responses
from   ghutil.api.client   import ACCEPT
from   ghutil.cli.__main__ import cli

@pytest.fixture
def echo_headers():
    with responses.RequestsMock() as rsps:
        rsps.add_callback(
            responses.GET,
            'https://api.github.com/echo-headers',
            callback=lambda r: (200, {}, json.dumps(dict(r.headers))),
            content_type='application/json',
        )
        yield

@pytest.mark.usefixtures('echo_headers')
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
def test_accept(config, accept_header):
    with tempfile.NamedTemporaryFile(mode='w+') as cfg:
        cfg.write(config)
        cfg.flush()
        r = CliRunner().invoke(cli, ['-c',cfg.name,'request','/echo-headers'])
        assert r.exit_code == 0
        headers = json.loads(r.output)
        assert headers.get("Accept") == accept_header

@pytest.mark.usefixtures('echo_headers')
@pytest.mark.parametrize('config,auth_header', [
    ('', None),
    (
        '[api.auth]\ntoken = legitimateoauthtoken\n',
        'token legitimateoauthtoken',
    ),
    (
        '[api.auth]\nusername = l.user\npassword = hunter2\n',
        None,
    ),
    (
        '[api.auth]\n'
        'token = legitimateoauthtoken\n'
        'username = l.user\n'
        'password = hunter2\n',
        'token legitimateoauthtoken',
    ),
])
def test_auth(monkeypatch, config, auth_header):
    # Keep `requests` from using the local user's ~/.netrc file; this is needed
    # not only for the empty config case but also for the tests that set the
    # "Authorization" header directly (see
    # <https://github.com/requests/requests/issues/3929>)
    monkeypatch.delattr(netrc, 'netrc')
    with tempfile.NamedTemporaryFile(mode='w+') as cfg:
        cfg.write(config)
        cfg.flush()
        r = CliRunner().invoke(cli, ['-c',cfg.name,'request','/echo-headers'])
        assert r.exit_code == 0
        headers = json.loads(r.output)
        assert headers.get("Authorization") == auth_header
