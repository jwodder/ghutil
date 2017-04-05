- Add more commands for more of the GitHub API:
    - starring & watching repositories
        - <https://developer.github.com/v3/activity/starring/>
    - creating pull requests
    - creating & interacting with issues
        - cf. <https://github.com/stephencelis/ghi>
    - listing users that are watching/have starred given repositories
    - listing a repository's forks
        - showing a tree of forks?
    - deleting gists and releases
    - deleting branches?
    - listing all issues & PRs (and commits to others' repositories?) you
      created
    - a generic "`gh request [-X <method>] /path`" command

- When creating a new release, prepopulate the release message/body with the
  tagged commit's commit message
- Either rename `parse_github_remote()` or split apart its URL parsing code
  from its `owner/repo` parsing code
- Support specifying a repository as a path to a local clone
    - Should `gh repo fork` support this?
- Support specifying a repository owned by the current user as just the
  repository name?
    - Should `gh repo fork` support this?
- `release`: Allow specifying the repository on the command line (and handle
  the case when a tag isn't also specified)
- `gh gist new`:
    - Allow creating a gist containing more than one file
    - Allow reading the file from stdin
- Give `gh repo new` an option for setting the local repository's origin to the
  new repository and pushing everything to it
- Add a `gh repo clone <repo> [<dir>]` command
- Add a `gh gist clone <id> [<dir>]` command
- Give `fork` an option for cloning the new repository
- Rename "`gh gist list`" to "`gh gist show`" and use the "`list`" name for
  just showing the names/IDs of gists?  (cf. `git stash`)
- Get `gh repo delete`'s prompt to show the full name of the repository (This
  will probably require changes in Click)

- Add a README
- Fill in the rest of `setup.py`
- Upload to GitHub
- cf. <https://github.com/whiteinge/ok.sh>
