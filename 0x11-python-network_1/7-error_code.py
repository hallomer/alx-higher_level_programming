#!/usr/bin/python3
"""Sends a request to the given URL
and displays the body of the response."""
from sys import argv
import requests

if __name__ == "__main__":
    response = requests.get(argv[1])
    if response.status_code >= 400:
        print('Error code:', response.status_code)
    else:
        print(response.text)
