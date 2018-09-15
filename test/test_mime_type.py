import pytest
from   ghutil.util import mime_type

@pytest.mark.parametrize('filename,mtype', [
    ('foo.txt',     'text/plain'),
    ('foo',         'application/octet-stream'),
    ('foo.gz',      'application/gzip'),
    ('foo.tar.gz',  'application/gzip'),
    ('foo.tgz',     'application/gzip'),
    ('foo.taz',     'application/gzip'),
    ('foo.svg.gz',  'application/gzip'),
    ('foo.svgz',    'application/gzip'),
    ('foo.Z',       'application/x-compress'),
    ('foo.tar.Z',   'application/x-compress'),
    ('foo.bz2',     'application/x-bzip2'),
    ('foo.tar.bz2', 'application/x-bzip2'),
    ('foo.tbz2',    'application/x-bzip2'),
    ('foo.xz',      'application/x-xz'),
    ('foo.tar.xz',  'application/x-xz'),
    ('foo.txz',     'application/x-xz'),
])
def test_mime_type(filename, mtype):
    assert mime_type(filename) == mtype
