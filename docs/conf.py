from ghutil import __version__

project   = 'ghutil'
author    = 'John T. Wodder II'
copyright = '2017 John T. Wodder II'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx_click.ext',
]

autodoc_default_flags = [
    'members',
    'private-members',
    'show-inheritance',
    'undoc-members',
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    #"requests": ("http://docs.python-requests.org/en/latest", None),
}

exclude_patterns = ['_build']
source_suffix = '.rst'
source_encoding = 'utf-8-sig'
master_doc = 'index'
version = __version__
release = __version__
today_fmt = '%Y %b %d'
default_role = 'py:obj'
pygments_style = 'sphinx'
todo_include_todos = True

html_theme = 'sphinx_rtd_theme'
html_last_updated_fmt = '%Y %b %d'
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True
