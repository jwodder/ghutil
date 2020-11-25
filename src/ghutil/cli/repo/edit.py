import click
from   ghutil.edit  import edit_as_mail
from   ghutil.types import Repository
from   ghutil.util  import optional

@click.command()
@optional('--allow-merge-commit/--no-merge-commit',
          help='Allow/disallow merging PRs with merge commits')
@optional('--allow-rebase-merge/--no-rebase-merge',
          help='Allow/disallow rebase-merging PRs')
@optional('--allow-squash-merge/--no-squash-merge',
          help='Allow/disallow squash-merging PRs')
@optional('-b', '--default-branch',
          help="Change the repository's default branch")
@optional('-d', '--description', help='Set repository description')
@optional('--has-issues/--no-issues',
          help='Enable/disable issues for repository')
@optional('--has-projects/--no-projects',
          help='Enable/disable projects in the repository')
@optional('--has-wiki/--no-wiki', help="Enable/disable the repository's wiki")
@optional('-H', '--homepage', metavar='URL', help='Set repository homepage')
@optional('-n', '--name', help='Rename repository')
@optional('-P/-p', '--private/--public', help='Make repository private/public')
@Repository.argument('repo')
def cli(repo, **edited):
    """
    Edit repository details.

    If one or more options are given on the command line, the repository is
    modified accordingly.  Otherwise, an editor is started, allowing you to
    modify the repository's details as a text file.
    """
    if not edited:
        edited = edit_as_mail(
            repo.data, '''
                name
                description
                homepage
                private
                default_branch
                allow_merge_commit
                allow_rebase_merge
                allow_squash_merge
                has_issues
                has_projects
                has_wiki
            '''
        )
        if not edited:
            click.echo('No modifications made; exiting')
            return
    # The GitHub API requires submitting the repository name when editing, even
    # if the name hasn't been changed.  However, the repository may have been
    # renamed previously, leaving a redirect at the old name, and so the name
    # supplied by the user, despite working, might not equal the current one.
    # Thus, in order to avoid accidentally un-renaming the repository, get its
    # name from the API via `repo.data["name"]` instead of using the one
    # supplied by the user via `repo.repo`.
    edited.setdefault("name", repo.data["name"])
    repo.patch(json=edited)
