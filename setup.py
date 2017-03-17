import errno
from   os.path    import dirname, join
import re
from   setuptools import setup, find_packages

with open(join(dirname(__file__), 'gh', '__init__.py')) as fp:
    for line in fp:
        m = re.search(r'^\s*__version__\s*=\s*([\'"])([^\'"]+)\1\s*$', line)
        if m:
            version = m.group(2)
            break
    else:
        raise RuntimeError('Unable to find own __version__ string')

try:
    with open(join(dirname(__file__), 'README.rst')) as fp:
        long_desc = fp.read()
except EnvironmentError as e:
    if e.errno == errno.ENOENT:
        long_desc = None
    else:
        raise

setup(
    name='gh',
    version=version,
    packages=find_packages(),
    license='MIT',
    author='John Thorvald Wodder II',
    author_email='gh@varonathe.org',
    ###keywords='',
    description='$SHORT_DESCRIPTION',
    long_description=long_desc,
    #url='https://github.com/jwodder/gh',

    install_requires=[
        'attrs~=16.3',
        'click~=6.5',
        'headerparser~=0.1.0',
        'requests>=2.4.2,<3',
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        #'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',

        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

        'License :: OSI Approved :: MIT License',

        ###
    ],

    entry_points={
        "console_scripts": [
            'gh = gh.__main__:cli',
        ]
    },
)
