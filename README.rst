.. image:: http://www.repostatus.org/badges/latest/wip.svg
    :target: http://www.repostatus.org/#wip
    :alt: Project Status: WIP — Initial development is in progress, but there
          has not yet been a stable, usable release suitable for the public.

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
``ghutil`` requires Python 3.3 or higher to run and `pip
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

``gh gist delete [<gist-id>]``
   Delete a gist

``gh gist [list]``
   List your gists

``gh gist new [-d <description>] [-f <filename>] [-P|--private] [<file>]``
   Create a gist from a file

``gh gist show [<gist-id> ...]``
   Show gist details

``gh gist star [<gist-id> ...]``
   Star the given gists

``gh gist starred``
   List gists you've starred

``gh gist unstar [<gist-id> ...]``
   Unstar the given gists

Issues
^^^^^^

``gh issue [list [<options>] [<repo>]]``
   List issues for a repository

``gh issue new [-T <title>] [--body <file>] [-a <assignee>] [-l <label>] [-m <milestone>] [<repo>]``
   Create an issue in the given repository

``gh issue read [--since <timestamp>] <issue>``
   Read an issue/PR and its comments

``gh issue reply <issue> [<file>]``
   Comment on an issue or pull request

``gh issue search <search-term> ...``
   Search for issues and/or pull requests

``gh issue show <issue> ...``
   Show details on the given issues

Pull Requests
^^^^^^^^^^^^^

``gh pr [list [<options>] [<repo>]]``
   List pull requests for a repository

``gh pr new [-T <title>] [--body <file>] [--maintainer-can-modify] <base> <head>``
   Create a pull request

``gh pr read [--since <timestamp>] <issue>``
   Read an issue/PR and its comments

``gh pr reply <issue> [<file>]``
   Comment on an issue or pull request

``gh pr show <pull request> ...``
   Show details on the given pull requests

Releases
^^^^^^^^

``gh release edit [<tag>]``
   Edit the release for the given tag (default: the most recent reachable tag)

``gh release [list [<repo>]]``
   List releases for a repository

``gh release new [<tag>]``
   Create a release for the given tag (default: the most recent reachable tag)

Repositories
^^^^^^^^^^^^

``gh repo clone <repo> [<dir>]``
   Locally clone a GitHub repository

``gh repo delete [<repo>]``
   Delete a GitHub repository

``gh repo edit [<options>] [<repo>]``
   Edit a GitHub repository's details

``gh repo fans [<repo>]``
   List users that have forked, starred, or watched the given repository

``gh repo fork <repo>``
   Fork the given repository

``gh repo [list [--type all|owner|public|private|member] [--sort created|updated|pushed|full_name] [--asc|--desc]]``
   List your repositories

``gh repo list-forks [<repo>]``
   List a repository's forks

``gh repo network [<repo> ...]``
   Show a repository's network of forks as a tree

``gh repo new [-d <description>] [-H <homepage>] [-P|--private] <name>``
   Create a new repository

``gh repo search <search-term> ...``
   Search for repositories on GitHub

``gh repo show [<repo> ...]``
   Show details on the given repositories

``gh repo star [<repo> ...]``
   Star the given repositories

``gh repo starred``
   List repositories you've starred

``gh repo unstar [<repo> ...]``
   Unstar the given repositories

Other
^^^^^

``gh plus1 <issue_url>|<comment_url> ...``
   Give a thumbs-up to an issue, pull request, or comment thereon

``gh request [--accept <MIME type>] [--data <data>] [-H <header>] [-X <method>] <path>``
   Make an arbitrary GitHub API request to ``<path>``
