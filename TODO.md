- Add more commands for more of the GitHub API:
    - starring & watching repositories
        - <https://developer.github.com/v3/activity/starring/>
    - creating pull requests
    - creating & interacting with issues
        - cf. <https://github.com/stephencelis/ghi>
    - listing users that are watching/have starred given repositories
    - listing a repository's forks
    - deleting gists, repositories, and releases
    - deleting branches?

- When creating a new release, prepopulate the release message/body with the
  tagged commit's commit message
- `edit`, `release`, and `remote`: Allow the user to specify the repository on
  the command line
    - Formats to accept:
        - HTTPS and Git/SSH URLs
        - `owner/repo`
        - just the repository name for repositories owned by the current user?
        - path to a local clone of a GitHub repository (`--git-dir`?)
    - Adjust the usage of `fork` to match
- `gist`:
    - Allow creating a gist containing more than one file
    - Allow reading the file from stdin
- Give `new` an option for setting the local repository's origin to the new
  repository and pushing everything to it
- Add a `gh clone {<repo> | <owner>/<repo>} [<dir>]` command
- Give `fork` an option for cloning the new repository
- Rename `gist` and/or `gists` so that they're not so similar

- Add a README
- Upload to GitHub
- cf. <https://github.com/whiteinge/ok.sh>
