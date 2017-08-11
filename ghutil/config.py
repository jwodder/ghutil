from   configparser import ConfigParser, ExtendedInterpolation, NoSectionError
import re
import shlex
import click
from   ghutil.api   import GitHub

ALIAS_RGX = re.compile(r'^\w(?:[-\w.]*\w)?$')

def configure(cfg_file, ctx):
    cfg = ConfigParser(interpolation=ExtendedInterpolation())
    cfg.read(cfg_file)
    # ctx.obj is ensured elsewhere when mocking with Betamax
    cfg_session(cfg, ctx.ensure_object(GitHub).session)
    cfg_aliases(cfg, ctx)

def cfg_session(cfg, session):
    try:
        auth = cfg['api.auth']
    except KeyError:
        auth = {}
    if 'token' in auth:
        session.headers["Authorization"] = "token " + auth['token']
    elif 'username' in auth and 'password' in auth:
        session.auth = (auth['username'], auth['password'])
    ### TODO: Complain if only one of (username, password) is set?
    try:
        extra_accept = cfg['api']['accept']
    except KeyError:
        pass
    else:
        extra_accept = ','.join(
            re.sub(r'^[\s,]+|[\s,]+$', '', line)
            for line in extra_accept.splitlines()
            if re.search(r'[^\s,]', line)
        )
        if extra_accept:
            if cfg.getboolean('api', 'append-accept', fallback=True):
                session.headers["Accept"] += ',' + extra_accept
            else:
                session.headers["Accept"] = extra_accept
        elif not cfg.getboolean('api', 'append-accept', fallback=True):
            session.headers.pop("Accept", None)

def cfg_aliases(cfg, ctx):
    try:
        aliases = cfg.items('alias')
    except NoSectionError:
        aliases = []
    for name, value in aliases:
        user_args = name.split()
        if not user_args or not all(map(ALIAS_RGX.match, user_args)):
            ctx.fail('Invalid alias name: ' + name)
        gh_args = shlex.split(value)
        if not gh_args:
            ctx.fail('Invalid alias definition: ' + value)
        cmd_parent = ctx.command
        alias_parent = ctx.obj.aliases
        for a in user_args[:-1]:
            alias_parent = alias_parent.setdefault(a, {})
            cmd_parent = cmd_parent.get_command(ctx, a)
            assert cmd_parent is not None
            if not isinstance(cmd_parent, click.Group):
                ctx.fail('Cannot add alias beneath non-group command: ' + name)
        if user_args[-1] in cmd_parent.commands:
            ctx.fail('Command already exists: ' + name)
        elif user_args[-1] in alias_parent:
            ctx.fail('Alias already defined: ' + name)
        alias_parent[user_args[-1]] = alias_cmd(gh_args)

def alias_cmd(real_cmd):
    @click.command(
        context_settings={"ignore_unknown_options": True},
        short_help='Alias: ' + ' '.join(map(shlex.quote, real_cmd)),
    )
    @click.argument('args', nargs=-1)
    @click.pass_context
    def alias(ctx, args):
        while ctx.parent is not None:
            ctx = ctx.parent
        cmd = ctx.command.get_command(ctx, real_cmd[0])
        assert cmd is not None  ### XXX
        ctx.invoke(cmd.main, tuple(real_cmd[1:]) + args, parent=ctx)
    return alias
