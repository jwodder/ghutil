from   betamax           import Betamax
import pytest
import requests
from   ghutil.api        import GitHub
from   ghutil.types      import Repository
from   ghutil.cli.pr.new import parse_pr_args

@pytest.mark.parametrize('base_arg,head_arg,base_repo,base_branch,head', [
    (
        'alice/repo:dev',
        'bob/sitory:patch',
        {"owner": "alice", "repo": "repo"},
        "dev",
        "bob:patch",
    ),

    (
        'alice/repo:dev',
        'bob/sitory',
        {"owner": "alice", "repo": "repo"},
        "dev",
        "bob:master",
    ),

    (
        'alice/repo:dev',
        ':patch',
        {"owner": "alice", "repo": "repo"},
        "dev",
        "charles:patch",
    ),

    (
        'alice/repo:dev',
        None,
        {"owner": "alice", "repo": "repo"},
        "dev",
        "charles:spork",
    ),

    (
        'alice/repo',
        'bob/sitory:patch',
        {"owner": "alice", "repo": "repo"},
        "master",
        "bob:patch",
    ),

    (
        'alice/repo',
        'bob/sitory',
        {"owner": "alice", "repo": "repo"},
        "master",
        "bob:master",
    ),

    (
        'alice/repo',
        ':patch',
        {"owner": "alice", "repo": "repo"},
        "master",
        "charles:patch",
    ),

    (
        'alice/repo',
        None,
        {"owner": "alice", "repo": "repo"},
        "master",
        "charles:spork",
    ),

    (
        ':dev',
        'bob/sitory:patch',
        {"owner": "bob", "repo": "sitory"},
        "dev",
        "patch",
    ),

    (
        ':dev',
        'bob/sitory',
        {"owner": "bob", "repo": "sitory"},
        "dev",
        "master",
    ),

    (
        ':dev',
        ':patch',
        {"owner": "charles", "repo": "fork"},
        "dev",
        "patch",
    ),

    (
        ':dev',
        None,
        {"owner": "charles", "repo": "fork"},
        "dev",
        "spork",
    ),
])
def test_parse_pr_args(mocker,base_arg,head_arg,base_repo,base_branch,head):
    mocker.patch(
        'ghutil.git.get_remote_url',
        return_value='https://github.com/charles/fork.git',
    )
    mocker.patch('ghutil.git.get_current_branch', return_value='spork')
    s = requests.Session()
    with Betamax(s).use_cassette('stub_parse_pr_args'):
        pr_repo, pr_branch, pr_head = parse_pr_args(GitHub(s),base_arg,head_arg)
    assert isinstance(pr_repo, Repository)
    assert pr_repo.owner == base_repo["owner"]
    assert pr_repo.repo  == base_repo["repo"]
    assert pr_branch     == base_branch
    assert pr_head       == head
