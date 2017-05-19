- Add more commands for more of the GitHub API:
    - starring & watching repositories
        - <https://developer.github.com/v3/activity/starring/>
    - creating pull requests
    - creating & interacting with issues
        - cf. <https://github.com/stephencelis/ghi>
    - listing users that are watching/have starred given repositories
    - listing a repository's forks
        - showing a tree of forks?
    - deleting gists
    - deleting releases
    - deleting branches?
    - listing all commits to others' repositories you created?
    - show recent activity on a repository/issue?

- Support specifying a repository as a path to a local clone
    - Should `gh repo fork` support this?
- Support specifying a repository owned by the current user as just the
  repository name?
    - Should `gh repo fork` support this?
- Give the `search` commands an option for outputting JSON objects instead of
  names?
- Give all commands that output JSON options (`--full`? `--raw`?) for showing
  all fields returned by the API instead of just selected fields
- Set User Agent
- Tag the code at each point it was stable?
    - Use `setuptools_scm` for managing the version number?
- Add a `--version` option

- `gh repo`:
    - Give `gh repo new` an option for setting the local repository's origin to
      the new repository and pushing everything to it
    - Add a `gh repo clone <repo> [<dir>]` command
    - Give `fork` an option for cloning the new repository
    - Get `gh repo delete`'s prompt to show the full name of the repository
      (This will probably require changes to Click)
    - Give `gh repo list` filtering & sorting options
    - Give `gh repo edit` options for setting everything via the command line
        - Only launch an editor if no options are given

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
      just showing the names/IDs of gists?  (cf. `git stash`)

- `gh request`:
    - Add an `-H`/`--header` option
    - Add support for `--data` reading from a file
    - Add a `--param key=value` option for setting query parameters (and/or
      JSON body elements?)

- `gh issue`:
    - Allow specifying issues on the command line in the following forms:
        - `https://github.com/:owner/:repo/{issues|pull}/:id`
        - `:owner/:repo/:id`
        - `:repo/:id` (for repositories owned by the current user) ?
        - `:id` (for issues of the local repository)

- Add a README
- Fill in the rest of `setup.py`
    - Add a `python_requires` field
    - Move contents to `setup.cfg`
- Upload to GitHub
- cf. <https://github.com/whiteinge/ok.sh>
- cf. <https://github.com/github/hub>
