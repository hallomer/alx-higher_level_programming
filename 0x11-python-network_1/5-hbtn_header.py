#!/usr/bin/python3
"""Sends a request to the given URL and displays the value of
the variable X-Request-Id in the response header."""
from sys import argv
import requests

if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
