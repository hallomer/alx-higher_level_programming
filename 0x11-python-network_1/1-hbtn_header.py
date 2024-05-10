#!/usr/bin/python3
"""Sends a request to the given URL and
displays the value of the X-Request-Id variable."""

from sys import argv
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        html = response.read()
        print(response.headers.get('X-Request-Id'))
