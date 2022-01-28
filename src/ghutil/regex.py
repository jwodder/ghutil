#: Regular expression for a valid GitHub username or organization name.  As of
#: 2017-07-23, trying to sign up to GitHub with an invalid username or create
#: an organization with an invalid name gives the message "Username may only
#: contain alphanumeric characters or single hyphens, and cannot begin or end
#: with a hyphen".  Additionally, trying to create a user named "none" (case
#: insensitive) gives the message "Username name 'none' is a reserved word."
#:
#: Unfortunately, there are a number of users who made accounts before the
#: current name restrictions were put in place, and so this regex also needs to
#: accept names that contain underscores, contain multiple consecutive hyphens,
#: begin with a hyphen, and/or end with a hyphen.
GH_USER_RGX = r"(?![Nn][Oo][Nn][Ee]($|[^-A-Za-z0-9]))[-_A-Za-z0-9]+"

# GH_USER_RGX_DE_JURE = r'(?![Nn][Oo][Nn][Ee]($|[^-A-Za-z0-9]))'\
#                      r'[A-Za-z0-9](?:-?[A-Za-z0-9])*'

#: Regular expression for a valid GitHub repository name.  Testing as of
#: 2017-05-21 indicates that repository names can be composed of alphanumeric
#: ASCII characters, hyphens, periods, and/or underscores, with the names ``.``
#: and ``..`` being reserved and names ending with ``.git`` forbidden.
GH_REPO_RGX = r"(?:\.?[-A-Za-z0-9_][-A-Za-z0-9_.]*|\.\.[-A-Za-z0-9_.]+)" r"(?<!\.git)"

_REF_COMPONENT = r"(?!\.)[^\x00-\x20/~^:?*[\\\x7F]+(?<!\.lock)"

#: Regular expression for a (possibly one-level) valid normalized Git refname
#: (e.g., a branch or tag name) as specified in
#: :manpage:`git-check-ref-format(1)`
#: <https://git-scm.com/docs/git-check-ref-format> as of 2017-07-23 (Git
#: 2.13.1)
GIT_REFNAME_RGX = r"(?!@/?$)(?!.*(?:\.\.|@\{{)){0}(?:/{0})*(?<!\.)".format(
    _REF_COMPONENT
)

#: Convenience regular expression for ``<owner>/<repo>``, including named
#: capturing groups
OWNER_REPO_RGX = fr"(?P<owner>{GH_USER_RGX})/(?P<repo>{GH_REPO_RGX})"

API_REPO_RGX = r"(?:https?://)?api\.github\.com/repos/" + OWNER_REPO_RGX

WEB_REPO_RGX = r"(?:https?://)?(?:www\.)?github\.com/" + OWNER_REPO_RGX
