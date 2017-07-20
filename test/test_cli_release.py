def test_release_list_qypi(cmd):
    r = cmd('release', 'list', 'qypi')
    assert r.exit_code == 0
    assert r.output == '''\
v0.4.1
v0.4.0
v0.3.0
v0.2.0
v0.1.0.post1
v0.1.0
'''

# release show
