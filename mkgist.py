#!/usr/bin/python3
import argparse
import os.path
import requests
from   ghutil import show_response

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--description')
parser.add_argument('-P', '--private', action='store_true')
parser.add_argument('-f', '--filename')
parser.add_argument('file')
args = parser.parse_args()

with open(args.file) as fp:
    content = fp.read()

if args.filename is not None:
    filename = args.filename
else:
    filename = os.path.basename(args.file)

data = {
    "files": {filename: {"content": content}},
    "public": not args.private,
}
if args.description is not None:
    data["description"] = args.description

# requests uses .netrc automatically
show_response(requests.post('https://api.github.com/gists', json=data))
