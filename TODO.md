- Add docstrings and `help` strings to everything
- Tag the code at each point it was stable?
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
    - deleting branches?
    - showing subscribers?
        - Are subscribers already listed by the /repos/:owner/:repo/subscribers
          endpoint despite the documentation saying it lists watchers?  If so,
          how are watchers fetched?

- Issues & pull requests:
    - comments
        - viewing comments
        - editing comments
    - more reactions
    - listing individual users' reactions?
    - reviewing PRs
        - review comments
    - merging PRs
    - assigning
    - labelling & milestones
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

- `gh release`:
    - When creating a new release, prepopulate the release message/body with
      the tagged commit's commit message
    - Allow specifying the repository on the command line (and handle the case
      when a tag isn't also specified)
    - Split into `gh release new` and `gh release edit`
    - Add options for setting everything via the command line

- `gh gist`:
    - `new`: Allow creating a gist containing more than one file
    - `new`: Allow reading the file from stdin
    - When no arguments are given to `show`, `star`, `unstar`, or `delete`, use
      the current repository
    - Support specifying gists as paths to local clones
    - Get `delete`'s prompt to show the full ID(?) of the gist (This will
      probably require changes to Click)

- `gh request`:
    - Add an `-H`/`--header` option
    - Add support for `--data` reading from a file
    - Add a `--param key=value` option for setting query parameters (and/or
      JSON body elements?)
    - Add an option for dumping response headers?

- `gh issue`:
    - `list`: Allow specifying `--since` in human-friendly formats like
      `2017-06-28` and `1h`
    - `reply`:
        - Add an option for including the quoted contents of a previous comment
          in the editor
        - Make sure that the issue exists before opening the editor?

- `gh pr`:
    - Improve the syntax of `new` and then document it in the docstring
    - Add a `search` command that just does `gh issue search type:pr ...`?
