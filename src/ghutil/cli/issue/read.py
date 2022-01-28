from datetime import datetime
from textwrap import indent
import click
from dateutil.tz import tzlocal, tzutc
from ghutil.types import Issue

EMOJI = {
    "+1": "\U0001F44D",
    "-1": "\U0001F44E",
    "laugh": "\U0001F604",
    "confused": "\U0001F615",
    "heart": "\u2764",
    "hooray": "\U0001F389",
}


@click.command()
@click.option(
    "--since",
    metavar="TIMESTAMP",
    help="Only show comments newer than the given timestamp",
)
@Issue.argument("issue")
def cli(issue, since):
    """View comments on an issue/PR"""
    output = show_comment(issue.data)
    for comment in issue.comments.get(params={"since": since}):
        output += "\n" + show_comment(comment)
    # echo_via_pager adds a newline, so remove the "extra" newline at the end
    click.echo_via_pager(output.rstrip("\r\n"))


def reformat_date(ts):
    return (
        datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ")
        .replace(tzinfo=tzutc())
        .astimezone(tzlocal())
        .strftime("%Y-%m-%d %H:%M:%S %z")
    )


def show_comment(obj):
    # Based on the output format of "git log"
    headers = []
    if "title" in obj:
        # Must be the actual issue object
        headers.append(
            (
                "PR:" if obj.get("pull_request") else "Issue:",
                obj["title"],
            )
        )
        headers.append(
            ("State:", obj["state"] + (" [LOCKED]" if obj["locked"] else ""))
        )
    else:
        # Must be just a comment
        headers.append(("comment", obj["id"]))
    headers.append(("Author:", obj["user"]["login"]))
    date = reformat_date(obj["created_at"])
    if obj.get("updated_at") is not None and obj["updated_at"] != obj["created_at"]:
        date += f'  (last updated {reformat_date(obj["updated_at"])})'
    headers.append(("Date:", date))
    if "title" in obj:
        headers.append(("Labels:", ", ".join(lb["name"] for lb in obj["labels"])))
        headers.append(("Assignees:", ", ".join(u["login"] for u in obj["assignees"])))
        if obj["milestone"] is not None:
            headers.append(("Milestone:", obj["milestone"]["title"]))
        if obj["closed_at"] is not None:
            headers.append(
                (
                    "Closed:",
                    "{} by {}".format(
                        reformat_date(obj["closed_at"]),
                        obj["closed_by"]["login"],
                    ),
                )
            )
    reactions = []
    for k, v in sorted(obj.get("reactions", {}).items()):
        if k not in ("total_count", "url") and v:
            symbol = EMOJI.get(k, ":" + k + ":")
            reactions.append(f"{symbol} {v}")
    if reactions:
        headers.append(("Reactions:", "  ".join(reactions)))
    width = max(len(k) for k, v in headers)
    return (
        "".join(f"{k:{width}} {v}\n" for k, v in headers)
        + "\n"
        + indent(obj["body"], " " * 4).rstrip("\r\n")
        + "\n"
    )
