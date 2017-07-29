import os
from   pathlib                         import Path
from   betamax                         import Betamax
from   betamax.cassette.cassette       import Placeholder
from   betamax_matchers.json_body      import JSONBodyMatcher
from   betamax_serializers.pretty_json import PrettyJSONSerializer
from   click.testing                   import CliRunner
import pytest
from   ghutil.api                      import GitHub
from   ghutil.cli.__main__             import cli

CASSETTE_DIR = Path(__file__).with_name('data') / 'cassettes'
try:
    # Path.mkdir() only got `exist_ok` in Python 3.5.
    CASSETTE_DIR.mkdir(parents=True)
except FileExistsError:
    pass

def redact(interaction, cassette):
    try:
        cassette.placeholders.append(Placeholder(
            placeholder='---REDACTED---',
            replace=interaction.data['request']['headers']['Authorization'][0],
        ))
    except LookupError:
        pass

Betamax.register_request_matcher(JSONBodyMatcher)
Betamax.register_serializer(PrettyJSONSerializer)

with Betamax.configure() as config:
    config.cassette_library_dir = str(CASSETTE_DIR)
    config.before_record(callback=redact)
    config.default_cassette_options['match_requests_on'] = [
        'method', 'uri', 'json-body',
    ]
    config.default_cassette_options['serialize_with'] = 'prettyjson'

@pytest.fixture
def cmd(betamax_session):
    def runner(*args):
        return CliRunner().invoke(
            cli,
            ['-c', os.devnull] + list(args),
            obj=GitHub(betamax_session),
        )
    return runner
