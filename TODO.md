- Add docstrings and `help` strings to everything
- Tag the code at each point it was stable?
- Instead of assuming the GitHub remote for a local repository is always
  "origin", get all remotes with `git config --get-regexp 'remote\..*\.url'`
  and check for one that's a GitHub URL?

- cf. <https://github.com/whiteinge/ok.sh>
- cf. <https://github.com/github/hub>
- cf. <https://github.com/stephencelis/ghi>

API Completeness
================
- Repositories:
    - watching
    - listing forks
    - deleting branches?
    - showing subscribers?
        - Are subscribers already listed by the /repos/:owner/:repo/subscribers
          endpoint despite the documentation saying it lists watchers?  If so,
          how are watchers fetched?

- Issues & pull requests:
    - creating pull requests
    - searching issues
    - comments
        - viewing comments
        - commenting
        - more reactions
        - viewing issue, PR, and comment reactions
    - reviewing PRs
    - merging PRs
    - assigning
    - labelling & milestones
    - closing

- Releases:
    - deleting
    - adding, editing, & deleting release assets

- Gists:
    - starring
    - forking
    - commenting on gists
    - deleting

- Projects?
- Organizations?
- listing all commits you made to others' repositories?
- showing recent activity on a repository/issue?
- getting data about users

Interface Improvements
======================
- Give the `search` commands an option for outputting JSON objects instead of
  names?
- Give all commands that output JSON options (`--full`? `--raw`?) for showing
  all fields returned by the API instead of just selected fields
- Give the `list` subcommands `--format` options

- `gh repo`:
    - Give `gh repo new` an option for setting the local repository's origin to
      the new repository and pushing everything to it
    - Give `fork` an option for cloning the new repository
    - Get `gh repo delete`'s prompt to show the full name of the repository
      (This will probably require changes to Click)
    - Give `gh repo list` filtering & sorting options
    - Give `gh repo edit` options for setting everything via the command line
        - Only launch an editor if no options are given
    - Give `starred` sorting options?

- `gh release`:
    - When creating a new release, prepopulate the release message/body with
      the tagged commit's commit message
    - Allow specifying the repository on the command line (and handle the case
      when a tag isn't also specified)
    - Split into `gh release new` and `gh release edit`?
    - Add options for setting everything via the command line

- `gh gist`:
    - `new`: Allow creating a gist containing more than one file
    - `new`: Allow reading the file from stdin
    - Add a `gh gist clone <id> [<dir>]` command
    - Rename "`gh gist list`" to "`gh gist show`" and use the "`list`" name for
      just showing the names/IDs of gists (cf. `git stash`)

- `gh request`:
    - Add an `-H`/`--header` option
    - Add support for `--data` reading from a file
    - Add a `--param key=value` option for setting query parameters (and/or
      JSON body elements?)

- `gh issue`:
    - Allow specifying issues as
      `https://github.com/:owner/:repo/{issues|pull}/:id`
