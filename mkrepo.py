#!/usr/bin/python3
import argparse
import requests
from   ghutil import show_response

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--description')
parser.add_argument('-H', '--homepage')
parser.add_argument('-P', '--private', action='store_true')
parser.add_argument('name')
args = parser.parse_args()

data = {
    "name": args.name,
    "private": args.private,
}
if args.description is not None:
    data["description"] = args.description
if args.homepage is not None:
    data["homepage"] = args.homepage

# requests uses .netrc automatically
show_response(requests.post('https://api.github.com/user/repos', json=data))
