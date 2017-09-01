import tempfile
import click
import pytest
from   ghutil.cli.__main__ import cli

@click.command(context_settings={"ignore_unknown_options": True})
@click.argument('args', nargs=-1)
def mock_cmd(args):
    click.echo('mock')
    for a in args:
        click.echo(a)

@pytest.mark.parametrize('alias_config,cmdline,output', [
    ('foo = mock', ['foo'], 'mock\n'),
    ('foo = mock', ['foo', 'bar'], 'mock\nbar\n'),
    ('foo = mock', ['foo', '-x', '--opt'], 'mock\n-x\n--opt\n'),
    (
        'foo = mock',
        ['foo', '-x', '--opt', 'bar', '-y', '--flag'],
        'mock\n-x\n--opt\nbar\n-y\n--flag\n',
    ),

    ('foo = mock bar', ['foo'], 'mock\nbar\n'),
    ('foo = mock bar', ['foo', 'baz'], 'mock\nbar\nbaz\n'),
    ('foo = mock bar', ['foo', '-x', '--opt'], 'mock\nbar\n-x\n--opt\n'),
    (
        'foo = mock bar',
        ['foo', '-x', '--opt', 'baz', '-y', '--flag'],
        'mock\nbar\n-x\n--opt\nbaz\n-y\n--flag\n',
    ),

    ('foo = mock "an argument"', ['foo'], 'mock\nan argument\n'),

    ('foo = mock -z --switch', ['foo'], 'mock\n-z\n--switch\n'),
    ('foo = mock -z --switch', ['foo', 'baz'], 'mock\n-z\n--switch\nbaz\n'),
    (
        'foo = mock -z --switch',
        ['foo', '-x', '--opt'],
        'mock\n-z\n--switch\n-x\n--opt\n',
    ),
    (
        'foo = mock -z --switch',
        ['foo', '-x', '--opt', 'baz', '-y', '--flag'],
        'mock\n-z\n--switch\n-x\n--opt\nbaz\n-y\n--flag\n',
    ),

    ('foo bar = mock', ['foo', 'bar'], 'mock\n'),
    ('repo foo = mock', ['repo', 'foo'], 'mock\n'),
    ('repo foo bar = mock', ['repo', 'foo', 'bar'], 'mock\n'),

    ('foo bar = mock 1\nfoo baz = mock 2', ['foo', 'bar'], 'mock\n1\n'),
    ('foo bar = mock 1\nfoo baz = mock 2', ['foo', 'baz'], 'mock\n2\n'),

    ('foo = mock 1\nrepo foo = mock 2\n', ['foo'], 'mock\n1\n'),
    ('foo = mock 1\nrepo foo = mock 2\n', ['repo', 'foo'], 'mock\n2\n'),

    ('foo = bar 1\nbar = mock 2\n', ['foo'], 'mock\n2\n1\n'),

    ### passing `--`?
])
def test_alias(monkeypatch, nullcmd, alias_config, cmdline, output):
    monkeypatch.setitem(cli.commands, 'mock', mock_cmd)
    with tempfile.NamedTemporaryFile(mode='w+') as cfg:
        cfg.write('[alias]\n' + alias_config + '\n')
        cfg.flush()
        r = nullcmd('-c', cfg.name, *cmdline)
        assert r.exit_code == 0, r.output
        assert r.output == output

@pytest.mark.parametrize('alias_config,errmsg', [
    # Configparser error:
    #('= mock',           'Invalid alias name'),
    ('foo -x = mock',    'Invalid alias name'),
    ('-x = mock',        'Invalid alias name'),
    ('-x foo = mock',    'Invalid alias name'),
    ('"foo" = mock',     'Invalid alias name'),
    ('"foo bar" = mock', 'Invalid alias name'),
    ('foo =',            'Invalid alias definition'),
    ('request foo = mock',        'Cannot add alias beneath non-group command'),
    ('foo = mock\nfoo bar=mock2', 'Cannot add alias beneath non-group command'),
    ('repo = mock',     'Command already exists'),
    ('repo new = mock', 'Command already exists'),
    # Configparser error:
    #('foo = mock\nfoo = mock2',          'Alias already defined'),
    ('foo bar = mock\nfoo  bar = mock2', 'Alias already defined'),
    ('foo bar = mock\nfoo = mock2',      'Alias already defined'),
])
def test_bad_alias(nullcmd, alias_config, errmsg):
    with tempfile.NamedTemporaryFile(mode='w+') as cfg:
        cfg.write('[alias]\n' + alias_config + '\n')
        cfg.flush()
        r = nullcmd('-c', cfg.name, 'nop')
        assert r.exit_code != 0
        assert errmsg in r.output


### Invocation errors:
### foo bar = mock; gh foo
### foo bar = mock; gh foo baz
### foo = nonexistent; gh foo

### Test that top-level aliases show up in `gh -h` (Not possible?)
### Test that second-level aliases show up in `gh <cmd> -h` (Not possible?)
### Test that `gh alias -h` shows the help for the real command
