#: Regular expression for a valid GitHub username or organization name.  As of
#: 2017-07-23, trying to sign up to GitHub with an invalid username or create
#: an organization with an invalid name gives the message "Username may only
#: contain alphanumeric characters or single hyphens, and cannot begin or end
#: with a hyphen".
GH_USER_RGX = r'[A-Za-z0-9](?:-?[A-Za-z0-9])*'

#: Regular expression for a valid GitHub repository name.  Testing as of
#: 2017-05-21 indicates that repository names can be composed of alphanumeric
#: ASCII characters, hyphens, periods, and/or underscores, with the names ``.``
#: and ``..`` being reserved and names ending with ``.git`` forbidden.
GH_REPO_RGX = r'(?:\.?[-A-Za-z0-9_][-A-Za-z0-9_.]*|\.\.[-A-Za-z0-9_.]+)'\
              r'(?<!\.git)'

#: Convenience regular expression for ``<owner>/<repo>``, including named
#: capturing groups
OWNER_REPO_RGX = r'(?P<owner>{})/(?P<repo>{})'.format(GH_USER_RGX, GH_REPO_RGX)
