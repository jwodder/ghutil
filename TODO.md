- Support more of the GitHub API
    - starring & watching repositories
        - <https://developer.github.com/v3/activity/starring/>
    - creating pull requests
    - creating & interacting with issues

- When creating a new release, prepopulate the release message/body with the
  tagged commit's commit message
- `edit` and `release`: Allow the user to specify the repository on the command
  line
- `gist`:
    - Allow creating a gist containing more than one file
    - Allow reading the file from stdin
- Accept command-line references to remote repositories in the same formats as
  accepted by `parse_github_remote()` and also in the form `owner/repo`
    - Also accept just the name of the repository for repositories owned by the
      current user
- Give `new` an option for setting the local repository's origin to the new
  repository and pushing everything to it
- Add a `gh clone {<repo> | <owner>/<repo>} [<dir>]` command?
- Give `fork` an option for cloning the new repository

- Rename `gist` and/or `gists` so that they're not so similar
- Make `release` use `edit_as_mail`
- Consolidate the API-calling code
- cf. <https://github.com/whiteinge/ok.sh>

- Add a README
- Upload to GitHub
