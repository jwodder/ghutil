- Add docstrings and `help` strings to everything
- Instead of assuming the GitHub remote for a local repository is always
  "origin", get all remotes with `git config --get-regexp 'remote\..*\.url'`
  and check for one that's a GitHub URL?
- Write more tests (somehow)

- cf. <https://github.com/whiteinge/ok.sh>
- cf. <https://github.com/github/hub>
- cf. <https://github.com/stephencelis/ghi>

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

- Issues & pull requests:
    - comments
        - viewing individual comments as JSON?
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
    - forking
    - listing forks
    - commenting on gists
    - getting raw contents?
    - searching (not in the API?)
    - listing users who starred a gist (not in the API?)

- Projects?
- Organizations?
- listing all commits you made to others' repositories?
- showing recent activity on a repository/issue?
- getting data about users
- searching code
- searching commits
- statuses? <https://developer.github.com/v3/repos/statuses/>

Interface Improvements
======================
- Give the `search` commands an option for outputting JSON objects instead of
  names?
- Give the `list` and `search` (and `starred`?) subcommands `--format` options
- Support configuring the following through a config file:
    - credentials
    - API endpoint (including overriding `https://api.github.com` in URL
      regexes)
    - `gh * list`/`search` formats
    - command aliases
    - `Accept:` headers to send
    - `Time-Zone:` header to send
    - whether `--verbose` should be on by default?
    - whether `--maintainer-can-modify` should be set on `gh pr new` by
      default?
    - timestamp format for `gh issue read`?
    - pager & editor programs to use?
- Add debug logging
- Ensure that the results of `get_remote_url()` are only ever passed to
  `parse_repo_url()`, not `parse_repo_spec()`

- `gh repo`:
    - Give `gh repo new` an option for setting the local repository's origin to
      the new repository and pushing everything to it
    - Give `fork` an option for cloning the new repository
    - Get `gh repo delete`'s prompt to show the full name of the repository
      (This will probably require changes to Click)
    - Give `starred` sorting options?
    - Come up with a better name for "`list-forks`"
    - Let `fans` take more than one repository at a time?
    - Let `list-forks` take more than one repository at a time?
    - Remove the `repo` command level and move all repository commands to `gh
      new`, `gh list`, `gh show`, etc.?

- `gh release`:
    - When creating a new release, prepopulate the release message/body with
      the tagged commit's commit message
    - Allow specifying the repository on the command line (and handle the case
      when a tag isn't also specified)
    - Split into `gh release new` and `gh release edit`
    - Add options for setting everything via the command line

- `gh gist`:
    - `new`: Allow creating a gist containing more than one file
    - `new`: Add an `--encoding` option?
    - Support specifying gists as paths to local clones
    - Get `delete`'s prompt to show the full ID(?) of the gist (This will
      probably require changes to Click)

- `gh request`:
    - Add support for `--data` reading from a file
    - Add a `--param key=value` option for setting query parameters (and/or
      JSON body elements?)
    - Add an option for dumping response headers?
    - Support non-JSON responses

- `gh issue`:
    - `list`: Allow specifying `--since` in human-friendly formats like
      `2017-06-28` and `1h`
    - `reply`:
        - Add an option for including the quoted contents of a previous comment
          in the editor
        - Make sure that the issue exists before opening the editor?
    - `read`:
        - Make the main issue "comment" respect `--since`?
        - Add an option for listing comments in reverse chronological order
        - Convert timestamps to local timezone?

- `gh pr`:
    - Improve the syntax of `new` and then document it in the docstring
    - Add a `search` command that just does `gh issue search type:pr ...`?
    - `new`: Should `--maintainer-can-modify` be on by default?
