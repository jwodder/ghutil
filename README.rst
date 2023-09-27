.. image:: https://www.repostatus.org/badges/latest/abandoned.svg
    :target: https://www.repostatus.org/#abandoned
    :alt: Project Status: Abandoned – Initial development has started, but
          there has not yet been a stable, usable release; the project has been
          abandoned and the author(s) do not intend on continuing development.

.. image:: https://github.com/jwodder/ghutil/workflows/Test/badge.svg?branch=master
    :target: https://github.com/jwodder/ghutil/actions?workflow=Test
    :alt: CI Status

.. image:: https://codecov.io/gh/jwodder/ghutil/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/jwodder/ghutil

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
``ghutil`` requires Python 3.7 or higher to run and `pip
<https://pip.pypa.io>`_ 19.0 or higher to install.  You can install ``ghutil``
and its dependencies by running::

    python3 -m pip install git+https://github.com/jwodder/ghutil.git


Basic Usage
===========

Authentication
--------------

Create a ``~/.config/ghutil.cfg`` file and store a GitHub token in it like so::

    [api.auth]
    token = YOUR_GITHUB_TOKEN_HERE

Commands
--------

Commands that allow the repository (or gist) to be unspecified will operate on
the current repository by default.

Gists
^^^^^

Run ``ghutil gist --help`` for details on specifying gists on the command line.

``ghutil gist clone <gist-id> [<dir>]``
   Locally clone a gist

``ghutil gist delete [--force] [<gist-id>]``
   Delete a gist

``ghutil gist [list]``
   List your gists

``ghutil gist new [-d <description>] [-P|--private] {-f <name> <file> | <file>} ...``
   Create a gist from one or more files

``ghutil gist show [<gist-id> ...]``
   Show gist details

``ghutil gist star [<gist-id> ...]``
   Star the given gists

``ghutil gist starred [--since <timestamp>]``
   List gists you've starred

``ghutil gist unstar [<gist-id> ...]``
   Unstar the given gists

``ghutil gist web [<gist-id>]``
   Open the given gist in a web browser

Issues
^^^^^^

Run ``ghutil issue --help`` for details on specifying issues on the command line.

``ghutil issue assign [--delete|--set] <issue> <user> ...``
   Assign an issue/PR to one or more users

``ghutil issue close <issue> ...``
   Close one or more issues/PRs

``ghutil issue comments [--since <timestamp>] <issue>``
   Show comments on an issue/PR as JSON

``ghutil issue edit [<options>] <issue>``
   Edit an issue

``ghutil issue label [--delete|--set] <issue> <label> ...``
   (Re)label an issue/PR

``ghutil issue [list [<options>] [<repo>]]``
   List issues for a repository

``ghutil issue lock <issue> ...``
   Lock one or more issues/PRs

``ghutil issue new [<options>] [<repo>]``
   Create an issue in the given repository

``ghutil issue open <issue> ...``
   Open one or more issues/PRs

``ghutil issue read [--since <timestamp>] <issue>``
   Read an issue/PR and its comments

``ghutil issue reply <issue> [<file>]``
   Comment on an issue or pull request

``ghutil issue search [--limit <N>] [--sort comments|created|updated] [--asc|--desc] <search-term> ...``
   Search for issues and/or pull requests

``ghutil issue show <issue> ...``
   Show details on the given issues

``ghutil issue unlock <issue> ...``
   Unlock one or more issues/PRs

``ghutil issue web <issue>``
   Open the given issue/PR in a web browser

Labels
^^^^^^

``ghutil label delete [-R|--repo <repo>] [--force] <label>``
   Delete a label

``ghutil label edit [-R|--repo <repo>] [--name <name>] [--color <color>] [-d <description>] <label>``
   Edit a label

``ghutil label [list [-R|--repo <repo>] [--verbose]]``
   List issue/PR labels available in a repository

``ghutil label new [-R|--repo <repo>] [-d <description>] <name> <color>``
   Create a new label

Milestones
^^^^^^^^^^

``ghutil milestone close [-R|--repo <repo>] <milestone>``
   Close a milestone

``ghutil milestone delete [-R|--repo <repo>] [--force] <milestone>``
   Delete a milestone

``ghutil milestone edit [-R|--repo <repo>] [<options>] <milestone>``
   Edit a milestone

``ghutil milestone [list [-R|--repo <repo>] [--state open|closed|all] [--sort completeness|due_on] [--asc|--desc]]``
   List issue/PR milestones available in a repository

``ghutil milestone new [-R|--repo <repo>] [-d <description>] [--due-on <timestamp>] [--open|--closed] <title>``
   Create a new milestone

``ghutil milestone open [-R|--repo <repo>] <milestone>``
   Open a milestone

``ghutil milestone show [-R|--repo <repo>] <milestone> ...``
   Show details on the given milestones

``ghutil milestone web [-R|--repo <repo>] <milestone>``
   Open the given milestone in a web browser

Pull Requests
^^^^^^^^^^^^^

Run ``ghutil pr --help`` for details on specifying pull requests on the command
line.

``ghutil pr assign [--delete|--set] <pull request> <user> ...``
   Assign an issue/PR to one or more users

``ghutil pr close <pull request> ...``
   Close one or more issues/PRs

``ghutil pr comments [--since <timestamp>] <pull request>``
   Show comments on an issue/PR as JSON

``ghutil pr edit [<options>] <pull request>``
   Edit a pull request

``ghutil pr label [--delete|--set] <pull request> <label> ...``
   (Re)label an issue/PR

``ghutil pr [list [<options>] [<repo>]]``
   List pull requests for a repository

``ghutil pr lock <pull request> ...``
   Lock one or more issues/PRs

``ghutil pr merge [-T <commit title>] [-m <commit message>] [--merge|--squash|--rebase] [--sha HASH] <pull request>``
   Merge a pull request

``ghutil pr new [-T <title>] [--body <file>] [--maintainer-can-modify] <base> <head>``
   Create a pull request

``ghutil pr open <pull request> ...``
   Open one or more issues/PRs

``ghutil pr read [--since <timestamp>] <pull request>``
   Read an issue/PR and its comments

``ghutil pr reply <pull request> [<file>]``
   Comment on an issue or pull request

``ghutil pr show <pull request> ...``
   Show details on the given pull requests

``ghutil pr unlock <pull request> ...``
   Unlock one or more issues/PRs

``ghutil pr web <pull request>``
   Open the given pull request in a web browser

Releases
^^^^^^^^

Run ``ghutil release --help`` for details on specifying releases on the command
line.  Commands that allow the release to be unspecified will operate on the
latest release by default.

``ghutil release attach [--content-type <MIME>] [--label <label>] [--name <name>] [<repo>:]<tag> <file>``
   Upload a release asset

``ghutil release delete [--force] [[<repo>:]<tag>]``
   Delete a release

``ghutil release edit [<options>] [[<repo>:]<tag>]``
   Edit a release

``ghutil release [list [<repo>]]``
   List releases for a repository

``ghutil release new [<options>] [<tag>]``
   Create a release for the given tag (default: the most recent reachable tag)

``ghutil release show [[<repo>:]<tag> ...]``
   Show details on the given releases

``ghutil release unattach [--force] [<repo>:]<tag> <asset>``
   Delete a release asset

``ghutil release web [[<repo>:]<tag>]``
   Open the given release in a web browser

Repositories
^^^^^^^^^^^^

Run ``ghutil repo --help`` for details on specifying repositories on the command
line.

``ghutil repo clone <repo> [<dir>]``
   Locally clone a GitHub repository

``ghutil repo delete [--force] [<repo>]``
   Delete a GitHub repository

``ghutil repo edit [<options>] [<repo>]``
   Edit a GitHub repository's details

``ghutil repo fans [<repo>]``
   List users that have forked, starred, or watched the given repository

``ghutil repo fork <repo>``
   Fork the given repository

``ghutil repo [list [<options>] [<user>]]``
   List a user's repositories

``ghutil repo list-forks [<repo>]``
   List a repository's forks

``ghutil repo network [<repo> ...]``
   Show a repository's network of forks as a tree

``ghutil repo new [<options>] <name>``
   Create a new repository

``ghutil repo search [--limit <N>] [--sort stars|forks|updated] [--asc|--desc] <search-term> ...``
   Search for repositories on GitHub

``ghutil repo set-topics <repo> <topic> ...``
   Set a repository's topics

``ghutil repo show [<repo> ...]``
   Show details on the given repositories

``ghutil repo star [<repo> ...]``
   Star the given repositories

``ghutil repo starred [--sort created|updated] [--asc|--desc]``
   List repositories you've starred

``ghutil repo unstar [<repo> ...]``
   Unstar the given repositories

``ghutil repo web [<repo>]``
   Open the given repository in a web browser

Other
^^^^^

``ghutil plus1 <issue_url>|<comment_url> ...``
   Give a thumbs-up to an issue, pull request, or comment thereon

``ghutil request [--data <data>] [-H <header>] [--paginate] [-X <method>] <path>``
   Make an arbitrary GitHub API request to ``<path>``


Related Prior Art
=================
- https://github.com/github/hub
- https://github.com/stephencelis/ghi
- https://github.com/whiteinge/ok.sh
