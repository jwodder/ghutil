- Add docstrings to everything
- Add (more) user documentation
    - Config file fields
    - Bash completion
    - The "edit as mail" interface
- Write more tests (somehow)
    - Test that the correct User-Agent header is being sent?
    - Test that calling `Repository.default_params()` when `get_remote_url()`
      returns a local path always fails
    - `--verbose`
    - Specifying an issue or PR without a repository name, with
      `get_remote_url()` mocked
    - `show`ing more than one object at once
    - Interacting with a renamed repository
    - Test specifying a nonexistent config file
    - Test invoking `delete` commands without `--force`
    - Try to set up integration tests that actually interact with GitHub?
- Support older versions of Git that don't have `git remote get-url`
    - At the very least, figure out and document the minimum required version
      of Git
    - Note that `git config --get remote.origin.url` doesn't perform
      "`insteadOf`" replacements
    - Or just switch to using GitPython or the like instead
- When searching with a limit, be smart about the number of results requested
  per page in order to minimize the number of API calls
- Bodies of issues & PRs (and releases?) created via the web interface seem to
  always be stored in the API with CRLF line endings.  Should issues & PRs
  created/edited with ghutil also use CRLFs?  Should CRLFs be converted to LFs
  when displaying/editing bodies returned by the API?
    - Should trailing line endings be removed when setting object bodies?
- Tag the code at each point it is/was stable
    - At the very least, tag the code before making any breaking changes

API Completeness
================
- Repositories:
    - watching (a.k.a. subscribing)
    - deleting branches
    - protecting branches
    - listing files?
    - getting individual file contents?
    - listing an organization's repositories
    - archiving repositories (once the API also supports unarchiving)
    - transferring repositories
    - downloading branches/trees as ZIPs?

- Issues & pull requests:
    - comments
        - showing individual comments as JSON?
        - editing & deleting comments
    - more reactions
    - listing individual users' reactions?
    - reviewing PRs
        - review comments
    - viewing PR diffs?
    - creating a PR from an issue

- Releases:
    - editing release assets
    - listing release assets (or is the list displayed when showing a release
      enough?)
    - showing individual release assets?
    - downloading release assets?

- Gists:
    - creating gists from non-text files?
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
- enabling & disabling Pages

Interface Improvements
======================
- Give the `list` and `search` commands an option for outputting JSON objects
  instead of names
- Give the `list` and `search` (and `starred`?) subcommands `--format` options
    - Use Jinja for formatting?  `format()` strings?  `git log --format`-style
      pseudo-printf format strings?
- Add options for controlling the amount & detail of debugging output?
    - Add options for showing responses, headers, and/or authentication method
      used?
    - Rename `--verbose` to something like `--full`(?) and use `--verbose` to
      control debugging?
- Default to HTTPS when cloning repositories/gists you don't have push access
  to?
- Give the `search` subcommands a `--raw` option to not add any quotes?
- Editing:
    - (Add an option to) show the API's response?
    - Deleting the entire body should set it to the empty string, not leave it
      unchanged
    - Rethink the way deleted header fields are handled
- Give `ghutil` a `-C`/`--chdir` option?
- Make it easier to configure the use of types like
  `application/vnd.github.v3.full+json` in place of
  `application/vnd.github.v3+json` in the "Accept:" header without having to
  use `append-accept = false`
- Allow specifying `--since` and `--due-on` values in human-friendly formats
  like `2017-06-28` and `1h`
- `edit_as_mail()`: Handle header parser errors in a more human-friendly way
- Give the `search` subcommands an option for just showing the total number of
  results?
- Give `new` and `reply` commands an `--edit` option for opening the editor
  anyway even if all the necessary details are given on the command line
    - How would the user then cancel the operation from the editor?  Leaving
      the input the same produces the same return value from `edit_as_mail()`
      as deleting everything.

- Support configuring the following through the config file:
    - API endpoint (including overriding `https://api.github.com` in URL
      regexes)
    - `ghutil * list`/`search` formats
    - command aliases
    - `Time-Zone:` header to send
    - whether `--verbose` should be on by default?
    - whether `--maintainer-can-modify` should be set on `ghutil pr new` by
      default?
    - timestamp format for `ghutil issue read`
    - editor program to use
    - default protocol to use when cloning repositories/gists
    - per-repository configuration of the name of the GitHub remote?
    - path to the Git executable?
    - default options for `ghutil repo new`?

- `ghutil gist`:
    - Let `web` take more than one repository at a time?

- `ghutil issue`:
    - `reply`:
        - Add an option for including the quoted (or commented-out?) contents
          of a previous comment in the editor
        - Make sure that the issue exists before opening the editor?
    - `read`:
        - Make the main issue "comment" respect `--since`?
        - Add an option for listing comments in reverse chronological order
        - Add the issue's "short ID" to the top of the output?
    - Allow specifying the repository as a local path if `:` (or `#`?) is used
      as the repo-issue separator?
    - Support issue templates when creating issues
    - Let `web` take more than one repository at a time?

- `ghutil milestone`:
    - Specifying a milestone by URL should remove the need to also use the `-R`
      option (regardless of whether the user is in the same repo as the
      milestone or even in a repo at all)
    - Let `web` take more than one repository at a time?

- `ghutil pr`:
    - Add a `search` command that just does `ghutil issue search type:pr ...`?
    - `new`:
        - Should `--maintainer-can-modify` be on by default?
        - (Add an option to) include the (commented out à la `git commit`)
          summaries of the PR's commits in the editor?
        - When a base or head argument is just a local repository path, use the
          given repository's current branch instead of the GitHub repo's
          default branch
        - Should just `<repo>:` be allowed as a base or head argument?  Should
          it mean the same thing as `<repo>`?
        - Support specifying the base repo as just the owner's name?
            - Note that it is possible for the repo name to differ between
              forks; how is the correct repo then supposed to be found from
              just the owner's name?
        - When `base` isn't given, use either the default brach of the
          repository's parent repo (if it has one) or the default branch of the
          repository itself
        - Support PR templates when creating PRs
    - `read`: Show merged status etc.

- `ghutil release`:
    - `new`:
        - Add an option to prepopulate the release message/body with the tagged
          commit's commit message
        - Allow specifying the repository on the command line
    - Support setting `target_commitish` when creating/editing a release
    - Allow specifying the repository as a local path
    - `unattach`: Support specifying assets by URL without a release argument
    - Let `web` take more than one repository at a time?

- `ghutil repo`:
    - Give `new` an option for setting the local repository's origin to the new
      repository and pushing everything to it
    - Give `fork` (and `new`?) an option for cloning the new repository
    - Give `fork` an option for waiting for the fork to be ready (checked by
      repeatedly polling the default branch's endpoint)
    - Come up with a better name for "`list-forks`"
    - Let `fans` take more than one repository at a time?
    - Let `list-forks` take more than one repository at a time?
    - Let `web` take more than one repository at a time?
    - Show repositories' `"organization"` field?
    - `clone`: Determine what protocol to use by default based on whether the
      user has push permission (checked via `repo.data["permissions"]["push"]`)

- `ghutil request`:
    - Add a `--param key=value` option for setting query parameters (and/or
      JSON body elements?)
    - Add an option for dumping response headers?
