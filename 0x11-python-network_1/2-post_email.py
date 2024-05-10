#!/usr/bin/python3
"""Sends a POST request to the given URL with the email as a parameter,
 and displays the body of the response."""

from sys import argv
import urllib.parse
import urllib.request

if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': argv[2]})
    data = data.encode('ascii')
    request = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf8'))
