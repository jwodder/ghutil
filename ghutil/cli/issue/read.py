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

def show_comment(obj):
    # Based on the output format of "git log"
    headers = []
    if "title" in obj:
        # Must be the actual issue object
        headers.append(('Title:', obj["title"]))
        headers.append((
            'State:',
            obj["state"] + (' [LOCKED]' if obj["locked"] else '')
        ))
    else:
        # Must be just a comment
        headers.append(('comment', obj["id"]))
    headers.append(('Author:', obj["user"]["login"]))
    date = obj["created_at"]
    if obj.get("updated_at") is not None and \
            obj["updated_at"] != obj["created_at"]:
        date += '  (last updated {updated_at})'.format(**obj)
    headers.append(('Date:', date))
    if "title" in obj:
        headers.append(('Labels:',', '.join(l["name"] for l in obj["labels"])))
        headers.append((
            'Assignees:',
            ', '.join(u["login"] for u in obj["assignees"])
        ))
        if obj["milestone"] is not None:
            headers.append(('Milestone:', obj["milestone"]["title"]))
        if obj["closed_at"] is not None:
            headers.append((
                'Closed:',
                '{closed_at} by {closed_by[login]}'.format(**obj)
            ))
    reactions = []
    for k,v in sorted(obj.get("reactions", {}).items()):
        if k not in ('total_count', 'url') and v:
            symbol = EMOJI.get(k, ':' + k + ':')
            reactions.append('{} {}'.format(symbol, v))
    if reactions:
        headers.append(('Reactions:', '  '.join(reactions)))
    width = max(len(k) for k,v in headers)
    return ''.join(
        '{:{width}} {}\n'.format(k, v, width=width) for k,v in headers
    ) + '\n' + indent(obj["body"], ' ' * 4).rstrip('\r\n') + '\n'
