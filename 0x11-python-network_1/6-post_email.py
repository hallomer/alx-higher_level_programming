#!/usr/bin/python3
"""Sends a POST request to the given URL with the email as a parameter,
and displays the body of the response."""
from sys import argv
import requests

if __name__ == "__main__":
    data = {'email': argv[2]}
    response = requests.post(argv[1], data=data)
    print(response.text)
