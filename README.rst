.. image:: http://www.repostatus.org/badges/latest/wip.svg
    :target: http://www.repostatus.org/#wip
    :alt: Project Status: WIP — Initial development is in progress, but there
          has not yet been a stable, usable release suitable for the public.

.. image:: https://travis-ci.org/jwodder/ghutil.svg?branch=master
    :target: https://travis-ci.org/jwodder/ghutil

.. image:: https://coveralls.io/repos/github/jwodder/ghutil/badge.svg?branch=master
    :target: https://coveralls.io/github/jwodder/ghutil?branch=master

.. image:: https://img.shields.io/github/license/jwodder/ghutil.svg?maxAge=2592000
    :target: https://opensource.org/licenses/MIT
    :alt: MIT License

.. contents::
    :backlinks: top

The ``ghutil`` package provides a command-line program for interacting with &
managing GitHub repositories, issues, gists, etc.

This is a work in progress; while the program should be usable at any given
point in time, many API features are not yet present, and those features that
are present may have their interface modified at any time.


Installation
============
``ghutil`` requires Python 3.4 or higher to run and `pip
<https://pip.pypa.io>`_ 6.0+, `Setuptools <https://setuptools.readthedocs.io>`_
30.3.0+, & `wheel <https://pypi.python.org/pypi/wheel>`_ to install.  `Once you
have those
<https://packaging.python.org/tutorials/installing-packages/#install-pip-setuptools-and-wheel>`_,
you can install ``ghutil`` and its dependencies by running::

    python3 -m pip install git+https://github.com/jwodder/ghutil.git


Basic Usage
===========

Authentication
--------------
Store your GitHub username & password in ``~/.netrc`` like so::

    machine api.github.com
    login YOUR_USERNAME_HERE
    password YOUR_PASSWORD_HERE

(Make sure the file permissions on ``~/.netrc`` are set to 0600!)

Alternatively, create a ``~/.config/ghutil.cfg`` file and populate it with
either your username & password::

    [api.auth]
    username = YOUR_USERNAME_HERE
    password = YOUR_PASSWORD_HERE

or an OAuth2 token::

    [api.auth]
    token = YOUR_OAUTH_TOKEN_HERE

Commands
--------

Gists
^^^^^

``gh gist clone <gist-id> [<dir>]``
   Locally clone a gist

``gh gist delete [--force] [<gist-id>]``
   Delete a gist

``gh gist [list]``
   List your gists

``gh gist new [-d <description>] [-P|--private] {-f <name> <file> | <file>} ...``
   Create a gist from one or more files

``gh gist show [<gist-id> ...]``
   Show gist details

``gh gist star [<gist-id> ...]``
   Star the given gists

``gh gist starred [--since <timestamp>]``
   List gists you've starred

``gh gist unstar [<gist-id> ...]``
   Unstar the given gists

Issues
^^^^^^

``gh issue assign [--delete|--set] <issue> <user> ...``
   Assign an issue/PR to one or more users

``gh issue close <issue> ...``
   Close one or more issues/PRs

``gh issue comments [--since <timestamp>] <issue>``
   Show comments on an issue/PR as JSON

``gh issue edit [<options>] <issue>``
   Edit an issue

``gh issue label [--delete|--set] <issue> <label> ...``
   (Re)label an issue/PR

``gh issue [list [<options>] [<repo>]]``
   List issues for a repository

``gh issue lock <issue> ...``
   Lock one or more issues/PRs

``gh issue new [<options>] [<repo>]``
   Create an issue in the given repository

``gh issue open <issue> ...``
   Open one or more issues/PRs

``gh issue read [--since <timestamp>] <issue>``
   Read an issue/PR and its comments

``gh issue reply <issue> [<file>]``
   Comment on an issue or pull request

``gh issue search [--limit <N>] [--sort comments|created|updated] [--asc|--desc] <search-term> ...``
   Search for issues and/or pull requests

``gh issue show <issue> ...``
   Show details on the given issues

``gh issue unlock <issue> ...``
   Unlock one or more issues/PRs

Labels
^^^^^^

``gh label delete [-R|--repo <repo>] [--force] <label>``
   Delete a label

``gh label edit [-R|--repo <repo>] [--name <name>] [--color <color>] <label>``
   Edit a label

``gh label [list [-R|--repo <repo>] [--verbose]]``
   List issue/PR labels available in a repository

``gh label new [-R|--repo <repo>] <name> <color>``
   Create a new label

Milestones
^^^^^^^^^^

``gh milestone close [-R|--repo <repo>] <milestone>``
   Close a milestone

``gh milestone delete [-R|--repo <repo>] [--force] <milestone>``
   Delete a milestone

``gh milestone edit [-R|--repo <repo>] [<options>] <milestone>``
   Edit a milestone

``gh milestone [list [-R|--repo <repo>] [--state open|closed|all] [--sort completeness|due_on] [--asc|--desc]]``
   List issue/PR milestones available in a repository

``gh milestone new [-R|--repo <repo>] [-d <description>] [--due-on <timestamp>] [--open|--closed] <title>``
   Create a new milestone

``gh milestone open [-R|--repo <repo>] <milestone>``
   Open a milestone

``gh milestone show [-R|--repo <repo>] <milestone> ...``
   Show details on the given milestones

Pull Requests
^^^^^^^^^^^^^

``gh pr assign [--delete|--set] <pull request> <user> ...``
   Assign an issue/PR to one or more users

``gh pr close <pull request> ...``
   Close one or more issues/PRs

``gh pr comments [--since <timestamp>] <pull request>``
   Show comments on an issue/PR as JSON

``gh pr edit [<options>] <pull request>``
   Edit a pull request

``gh pr label [--delete|--set] <pull request> <label> ...``
   (Re)label an issue/PR

``gh pr [list [<options>] [<repo>]]``
   List pull requests for a repository

``gh pr lock <pull request> ...``
   Lock one or more issues/PRs

``gh pr merge [-T <commit title>] [-m <commit message>] [--merge|--squash|--rebase] [--sha HASH] <pull request>``
   Merge a pull request

``gh pr new [-T <title>] [--body <file>] [--maintainer-can-modify] <base> <head>``
   Create a pull request

``gh pr open <pull request> ...``
   Open one or more issues/PRs

``gh pr read [--since <timestamp>] <pull request>``
   Read an issue/PR and its comments

``gh pr reply <pull request> [<file>]``
   Comment on an issue or pull request

``gh pr show <pull request> ...``
   Show details on the given pull requests

``gh pr unlock <pull request> ...``
   Unlock one or more issues/PRs

Releases
^^^^^^^^

``gh release attach [--content-type <MIME>] [--label <label>] [--name <name>] [<repo>:]<tag> <file>``
   Upload a release asset

``gh release delete [--force] [[<repo>:]<tag>]``
   Delete a release

``gh release edit [<options>] [[<repo>:]<tag>]``
   Edit a release

``gh release [list [<repo>]]``
   List releases for a repository

``gh release new [<options>] [<tag>]``
   Create a release for the given tag (default: the most recent reachable tag)

``gh release show [[<repo>:]<tag> ...]``
   Show details on the given releases

``gh release unattach [--force] [<repo>:]<tag> <asset>``
   Delete a release asset

Repositories
^^^^^^^^^^^^

``gh repo clone <repo> [<dir>]``
   Locally clone a GitHub repository

``gh repo delete [--force] [<repo>]``
   Delete a GitHub repository

``gh repo edit [<options>] [<repo>]``
   Edit a GitHub repository's details

``gh repo fans [<repo>]``
   List users that have forked, starred, or watched the given repository

``gh repo fork <repo>``
   Fork the given repository

``gh repo [list [<options>] [<user>]]``
   List a user's repositories

``gh repo list-forks [<repo>]``
   List a repository's forks

``gh repo network [<repo> ...]``
   Show a repository's network of forks as a tree

``gh repo new [<options>] <name>``
   Create a new repository

``gh repo search [--limit <N>] [--sort stars|forks|updated] [--asc|--desc] <search-term> ...``
   Search for repositories on GitHub

``gh repo show [<repo> ...]``
   Show details on the given repositories

``gh repo star [<repo> ...]``
   Star the given repositories

``gh repo starred [--sort created|updated] [--asc|--desc]``
   List repositories you've starred

``gh repo unstar [<repo> ...]``
   Unstar the given repositories

Other
^^^^^

``gh plus1 <issue_url>|<comment_url> ...``
   Give a thumbs-up to an issue, pull request, or comment thereon

``gh request [--data <data>] [-H <header>] [--paginate] [-X <method>] <path>``
   Make an arbitrary GitHub API request to ``<path>``


Related Prior Art
=================
- https://github.com/github/hub
- https://github.com/stephencelis/ghi
- https://github.com/whiteinge/ok.sh
