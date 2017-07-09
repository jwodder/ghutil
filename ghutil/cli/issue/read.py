from   textwrap      import indent
import click
from   ghutil.issues import GHIssue

EMOJI = {
    '+1': '\U0001F44D',
    '-1': '\U0001F44E',
    'laugh': '\U0001F604',
    'confused': '\U0001F615',
    'heart': '\u2764',
    'hooray': '\U0001F389',
}

@click.command()
@click.option('--since', metavar='TIMESTAMP')
@click.argument('issue', type=GHIssue())
def cli(issue, since):
    """ View comments on an issue/PR """
    output = show_comment(issue.get())
    for comment in issue.comments.get(params={"since": since}):
        output += '\n' + show_comment(comment)
    # echo_via_pager adds a newline, so remove the "extra" newline at the end
    click.echo_via_pager(output.rstrip('\r\n'))

def show_comment(comment):
    # Based on the output format of "git log"
    output = 'comment {id}\n' \
             'Author: {user[login]}\n' \
             'Date:   {created_at}'.format(**comment)
    if comment.get("updated_at") is not None and \
            comment["updated_at"] != comment["created_at"]:
        output += '  (last edited {updated_at})'.format(**comment)
    output += '\n'
    reactions = []
    for k,v in comment.get("reactions", {}).items():
        if k not in ('total_count', 'url') and v:
            symbol = EMOJI.get(k, ':' + k + ':')
            reactions.append('{} {}'.format(symbol, v))
    if reactions:
        output += '  '.join(reactions) + '\n'
    output += '\n' + indent(comment["body"], ' ' * 4).rstrip('\r\n') + '\n'
    return output
