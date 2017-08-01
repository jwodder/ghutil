- Add docstrings to everything
- Instead of assuming the GitHub remote for a local repository is always
  "origin", get all remotes with `git config --get-regexp 'remote\..*\.url'`
  and check for one that's a GitHub URL?
- Write more tests (somehow)
    - Somewhere test that credentials are being redacted from cassettes
    - Test that the correct User-Agent and Accept headers are being sent?
    - Test that calling `Repository.default_params()` when `get_remote_url()`
      returns a local path always fails
    - `--verbose`
    - Specifying an issue or PR without a repository name, with
      `get_remote_url()` mocked
    - `show`ing more than one object at once
    - Editing a renamed repository
- It appears that not all URL path components are treated case-insensitively by
  GitHub (just the variable/user-defined ones?).  Fix the regexes to match.

API Completeness
================
- Repositories:
    - watching
    - showing subscribers?
        - Are subscribers already listed by the /repos/:owner/:repo/subscribers
          endpoint despite the documentation saying it lists watchers?  If so,
          how are watchers fetched?
    - deleting branches
    - protecting branches
    - editing all options
    - editing topics

- Issues & pull requests:
    - comments
        - showing individual comments as JSON?
        - editing comments
    - more reactions
    - listing individual users' reactions?
    - reviewing PRs
        - review comments
    - merging PRs
    - assigning
    - labelling & milestones
    - editing
    - closing

- Releases:
    - deleting
    - adding, editing, & deleting release assets

- Gists:
    - editing
    - forking
    - listing forks
    - commenting on gists
    - getting raw contents?
    - searching (not in the API?)
    - listing users who starred a gist (not in the API?)

- Projects?
- Organizations?
- listing all commits you made to others' repositories?
- showing recent activity on a repository/issue
- getting data about users
- searching code
- searching commits
- statuses? <https://developer.github.com/v3/repos/statuses/>

Interface Improvements
======================
- Give the `list` and `search` commands an option for outputting JSON objects
  instead of names
- Give the `list` and `search` (and `starred`?) subcommands `--format` options
- Add debug logging
    - Rename `--verbose` to something like `--full`(?) and use `--verbose` to
      control logging level
- Support bash completion
- Add a command for showing rate limit information?
- Default to HTTPS when cloning repositories/gists you don't have push access
  to?
- `edit_as_mail()`: Set temporary file extension to `.eml`?
- Die gracefully when 'origin' is a non-GitHub URL
- When no arguments are given to a `show` subcommand, output an empty list?
- Allow web URLs to start with "https://www.github.com", "github.com", or
  "www.github.com"
- Change resources' `__str__` methods to use `self.data` instead of
  user-supplied params in order to ensure redirects over renames are taken into
  account (cf. `gh repo delete`)

- Support configuring the following through the config file:
    - API endpoint (including overriding `https://api.github.com` in URL
      regexes)
    - `gh * list`/`search` formats
    - command aliases
    - `Accept:` headers to send
    - `Time-Zone:` header to send
    - whether `--verbose` should be on by default?
    - whether `--maintainer-can-modify` should be set on `gh pr new` by
      default?
    - timestamp format for `gh issue read`
    - editor program to use
    - default protocol to use when cloning repositories/gists

- `gh gist`:
    - `new`: Allow creating a gist containing more than one file
    - `new`: Add an `--encoding` option?
    - Get `delete`'s prompt to show the full ID(?) of the gist (This will
      probably require changes to Click)

- `gh issue`:
    - `list`: Allow specifying `--since` in human-friendly formats like
      `2017-06-28` and `1h`
    - `reply`:
        - Add an option for including the quoted (or commented-out?) contents
          of a previous comment in the editor
        - Make sure that the issue exists before opening the editor?
    - `read`:
        - Make the main issue "comment" respect `--since`?
        - Add an option for listing comments in reverse chronological order
        - Convert timestamps to local timezone?
    - `new`: Abort if the user closes the editor without saving?
    - Should user-supplied milestones always be interpreted as milestone names
      instead of numbers?
    - Allow specifying the repository as a local path if `:` (or `#`?) is used
      as the repo-issue separator?

- `gh pr`:
    - Improve the syntax of `new` and then document it in the docstring
    - Add a `search` command that just does `gh issue search type:pr ...`?
    - `new`: Should `--maintainer-can-modify` be on by default?
    - `new`: Abort if the user closes the editor without saving?

- `gh release`:
    - When creating a new release, (add an option to) prepopulate the release
      message/body with the tagged commit's commit message
    - `new`: Allow specifying the repository on the command line
    - Support setting `target_commitish` when creating/editing a release
    - `new`: Abort if the user closes the editor without saving?
    - Allow specifying the repository as a local path?

- `gh repo`:
    - Give `new` an option for setting the local repository's origin to the new
      repository and pushing everything to it
    - Give `fork` (and `new`?) an option for cloning the new repository
    - Give `starred` sorting options?
    - Come up with a better name for "`list-forks`"
    - Let `fans` take more than one repository at a time?
    - Let `list-forks` take more than one repository at a time?
    - Remove the `repo` command level and move all repository commands to `gh
      new`, `gh list`, `gh show`, etc.?
    - `list`: Add visibility and affiliation options?

- `gh request`:
    - Add support for `--data` reading from a file
    - Add a `--param key=value` option for setting query parameters (and/or
      JSON body elements?)
    - Add an option for dumping response headers?
    - Support non-JSON responses
