from   subprocess import CalledProcessError, check_output
import click

def cmdline(*args, **kwargs):
    try:
        return check_output(args, universal_newlines=True, **kwargs).strip()
    except CalledProcessError as e:
        click.get_current_context().exit(e.returncode)

def get_remote_url(chdir=None, remote='origin'):
    return cmdline('git', 'remote', 'get-url', remote, cwd=chdir)

def get_last_tag(chdir=None):
    return cmdline('git', 'describe', '--abbrev=0', '--tags', cwd=chdir)
