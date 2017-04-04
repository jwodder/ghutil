- Add more commands for more of the GitHub API:
    - starring & watching repositories
        - <https://developer.github.com/v3/activity/starring/>
    - creating pull requests
    - creating & interacting with issues
        - cf. <https://github.com/stephencelis/ghi>
    - listing users that are watching/have starred given repositories
    - listing a repository's forks
        - showing a tree of forks?
    - deleting gists, repositories, and releases
    - deleting branches?
    - listing all issues & PRs (and commits to others' repositories?) you
      created
    - a generic "`gh request [-X <method>] /path`" command

- When creating a new release, prepopulate the release message/body with the
  tagged commit's commit message
- Either rename `parse_github_remote()` or split apart its URL parsing code
  from its `owner/repo` parsing code
- Support specifying a repository as a path to a local clone
    - Should `fork` support this?
- Support specifying a repository owned by the current user as just the
  repository name?
    - Should `fork` support this?
- `release`: Allow specifying the repository on the command line (and handle
  the case when a tag isn't also specified)
- `gist`:
    - Allow creating a gist containing more than one file
    - Allow reading the file from stdin
- Give `new` an option for setting the local repository's origin to the new
  repository and pushing everything to it
- Add a `gh clone <repo> [<dir>]` command
- Add a `gh gist clone <id> [<dir>]` command
- Give `fork` an option for cloning the new repository
- Rename `gist` and/or `gists` so that they're not so similar
- Consider reorganizing the commands as follows:
    - `gh list`  → `gh repo [list]`
    - `gh new`   → `gh repo new`
    - `gh edit`  → `gh repo edit`
    - `gh fork`  → `gh repo fork` ?
    - `gh gists` → `gh gist [list]`
    - `gh gist`  → `gh gist new`
- Rename the "`list`" commands to "`show`" and use the "`list`" name for just
  showing the names/IDs of objects?  (cf. `git stash`)
    - Let "`show`" take an argument (required?) for which repository to show
      details for
        - Eliminate `gh remote` and give `show` (et alii?) a `--sh` option

- Add a README
- Fill in the rest of `setup.py`
- Upload to GitHub
- cf. <https://github.com/whiteinge/ok.sh>
