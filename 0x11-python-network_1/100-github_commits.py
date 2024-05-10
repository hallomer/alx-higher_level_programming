#!/usr/bin/python3
"""List the last 10 commits of a given GitHub repo using GitHub API."""
from sys import argv
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    response = requests.get(url)
    commits = response.json()

    try:
        for commit in commits[:10]:
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print("{}: {}".format(sha, author))
    except IndexError:
        pass
