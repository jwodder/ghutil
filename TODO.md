- Add docstrings to everything
- Add (more) user documentation
    - Config file fields
    - Bash completion
- Write more tests (somehow)
    - Somewhere test that credentials are being redacted from cassettes
    - Test that the correct User-Agent header is being sent?
    - Test that calling `Repository.default_params()` when `get_remote_url()`
      returns a local path always fails
    - `--verbose`
    - Specifying an issue or PR without a repository name, with
      `get_remote_url()` mocked
    - `show`ing more than one object at once
    - Editing a renamed repository
    - Test specifying a nonexistent config file
- It appears that not all URL path components are treated case-insensitively by
  GitHub (just the variable/user-defined ones?).  Fix the regexes to match.
- Support older versions of Git that don't have `git remote get-url`
    - At the very least, figure out and document the minimum required version
      of Git
    - Note that `git config --get remote.origin.url` doesn't perform
      "`insteadOf`" replacements
    - Or just switch to using GitPython or the like instead
- Several tests assume that they're being run in a Git clone of jwodder/ghutil,
  and thus they fail when run from sdists.  Fix this.

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
    - editing topics

- Issues & pull requests:
    - comments
        - showing individual comments as JSON?
        - editing & deleting comments
    - more reactions
    - listing individual users' reactions?
    - reviewing PRs
        - review comments
    - merging PRs
    - assigning
    - labelling & milestones
    - editing PRs
    - opening, closing, locking, & unlocking PRs
    - viewing PR diffs?

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
- Add options for controlling the amount & detail of debugging output?
    - Add options for showing responses, headers, and/or authentication method
      used?
    - Rename `--verbose` to something like `--full`(?) and use `--verbose` to
      control debugging?
- Add a command for showing rate limit information?
- Default to HTTPS when cloning repositories/gists you don't have push access
  to?
- When no arguments are given to a `show` subcommand, output an empty list?
- Accept api.github.com URLs without "https://"?
- Change resources' `__str__` methods to use `self.data` instead of
  user-supplied params in order to ensure redirects over renames are taken into
  account (cf. `gh repo delete`)
- Give the `search` subcommands a `--raw` option to not add any quotes?
- `edit` subcommands: (Add an option to) show the API's response?
- Editing:
    - Deleting the entire body should set it to the empty string, not leave it
      unchanged
    - Rethink the way deleted header fields are handled
- Give `gh` a `-C`/`--chdir` option?
- Make it easier to configure the use of types like
  `application/vnd.github.v3.full+json` in place of
  `application/vnd.github.v3+json` in the "Accept:" header without having to
  use `append-accept = false`
- Print out lists of JSON objects as each page is received instead of waiting
  for everything to be fetched before printing anything

- Support configuring the following through the config file:
    - API endpoint (including overriding `https://api.github.com` in URL
      regexes)
    - `gh * list`/`search` formats
    - command aliases
    - `Time-Zone:` header to send
    - whether `--verbose` should be on by default?
    - whether `--maintainer-can-modify` should be set on `gh pr new` by
      default?
    - timestamp format for `gh issue read`
    - editor program to use
    - default protocol to use when cloning repositories/gists
    - per-repository configuration of the name of the GitHub remote?
    - path to the Git executable?

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
        - Add the issue's "short ID" to the top of the output?
    - Should user-supplied milestones always be interpreted as milestone names
      instead of numbers?
        - But then how would one list issues with milestone "none"?
    - Allow specifying the repository as a local path if `:` (or `#`?) is used
      as the repo-issue separator?
    - Support issue templates when creating issues

- `gh pr`:
    - Improve the syntax of `new` and then document it in the docstring
    - Add a `search` command that just does `gh issue search type:pr ...`?
    - `new`:
        - Should `--maintainer-can-modify` be on by default?
        - (Add an option to) include the (commented out à la `git commit`)
          summaries of the PR's commits in the editor?
    - Support PR templates when creating issues
    - Add a way to list/show all pull requests to/from the current/given
      branch?

- `gh release`:
    - `new`:
        - Add an option to prepopulate the release message/body with the tagged
          commit's commit message
        - Allow specifying the repository on the command line
    - Support setting `target_commitish` when creating/editing a release
    - Allow specifying the repository as a local path

- `gh repo`:
    - Give `new` an option for setting the local repository's origin to the new
      repository and pushing everything to it
    - Give `fork` (and `new`?) an option for cloning the new repository
    - Come up with a better name for "`list-forks`"
    - Let `fans` take more than one repository at a time?
    - Let `list-forks` take more than one repository at a time?
    - Remove the `repo` command level and move all repository commands to `gh
      new`, `gh list`, `gh show`, etc.?

- `gh request`:
    - Add support for `--data` reading from a file
    - Add a `--param key=value` option for setting query parameters (and/or
      JSON body elements?)
    - Add an option for dumping response headers?
