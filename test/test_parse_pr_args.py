import pytest
import responses
from   ghutil.api        import GitHub
from   ghutil.cli.pr.new import parse_pr_args

@pytest.fixture(autouse=True, scope='module')
def echo_headers():
    with responses.RequestsMock() as rsps:
        rsps.add(
            responses.GET,
            'https://api.github.com/repos/alice/repo',
            json={
                "id": 1,
                "default_branch": "master",
                "owner": {"login": "alice"},
                "name": "repo"
            },
        )
        rsps.add(
            responses.GET,
            'https://api.github.com/repos/bob/sitory',
            json={
                "id": 2,
                "default_branch": "master",
                "owner": {"login": "bob"},
                "name": "sitory",
                "source": {
                    "id": 1,
                    "default_branch": "master",
                    "owner": {"login": "alice"},
                    "name": "repo"
                }
            },
        )
        rsps.add(
            responses.GET,
            'https://api.github.com/repos/charles/fork',
            json={
                "id": 3,
                "default_branch": "master",
                "owner": {"login": "charles"},
                "name": "fork",
                "source": {
                    "id": 1,
                    "default_branch": "master",
                    "owner": {"login": "alice"},
                    "name": "repo"
                }
            }
        )
        yield

@pytest.mark.parametrize('base_arg,head_arg,output', [
    (
        'alice/repo:dev',
        'bob/sitory:patch',
        ({"owner": "alice", "repo": "repo"}, "dev", "bob:patch"),
    ),

    (
        'alice/repo:dev',
        'bob/sitory',
        ({"owner": "alice", "repo": "repo"}, "dev", "bob:master"),
    ),

    (
        'alice/repo:dev',
        ':patch',
        ({"owner": "alice", "repo": "repo"}, "dev", "charles:patch"),
    ),

    (
        'alice/repo:dev',
        None,
        ({"owner": "alice", "repo": "repo"}, "dev", "charles:spork"),
    ),

    (
        'alice/repo',
        'bob/sitory:patch',
        ({"owner": "alice", "repo": "repo"}, "master", "bob:patch"),
    ),

    (
        'alice/repo',
        'bob/sitory',
        ({"owner": "alice", "repo": "repo"}, "master", "bob:master"),
    ),

    (
        'alice/repo',
        ':patch',
        ({"owner": "alice", "repo": "repo"}, "master", "charles:patch"),
    ),

    (
        'alice/repo',
        None,
        ({"owner": "alice", "repo": "repo"}, "master", "charles:spork"),
    ),

    (
        ':dev',
        'bob/sitory:patch',
        ({"owner": "bob", "repo": "sitory"}, "dev", "patch"),
    ),

    (
        ':dev',
        'bob/sitory',
        ({"owner": "bob", "repo": "sitory"}, "dev", "master"),
    ),

    (
        ':dev',
        ':patch',
        ({"owner": "charles", "repo": "fork"}, "dev", "patch"),
    ),

    (
        ':dev',
        None,
        ({"owner": "charles", "repo": "fork"}, "dev", "spork"),
    ),
])
def test_parse_pr_args(mocker, base_arg, head_arg, output):
    mocker.patch(
        'ghutil.git.get_remote_url',
        return_value='https://github.com/charles/fork.git',
    )
    mocker.patch('ghutil.git.get_current_branch', return_value='spork')
    assert parse_pr_args(GitHub(),base_arg,head_arg) == output
