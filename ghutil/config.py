from   configparser import ConfigParser, ExtendedInterpolation
import re
import click
from   ghutil.api   import GitHub

def configure(cfg_file, ctx):
    cfg = ConfigParser(interpolation=ExtendedInterpolation())
    cfg.read(cfg_file)
    # ctx.obj is ensured elsewhere when mocking with Betamax
    cfg_session(cfg, ctx.ensure_object(GitHub).session)

def cfg_session(cfg, session):
    try:
        auth = cfg['api.auth']
    except KeyError:
        auth = {}
    if 'token' in auth:
        session.headers["Authorization"] = "token " + auth['token']
    elif 'username' in auth and 'password' in auth:
        session.auth = (auth['username'], auth['password'])
    elif 'username' in auth:
        raise click.UsageError('Config file contains username but no password')
    elif 'password' in auth:
        raise click.UsageError('Config file contains password but no username')
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
