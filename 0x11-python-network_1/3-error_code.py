#!/usr/bin/python3
"""Sends a request to the given URL and displays the body of the response."""

from sys import argv
import urllib.error
import urllib.request

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf8'))
    except urllib.error.HTTPError as error:
        print('Error code:', error.code)
