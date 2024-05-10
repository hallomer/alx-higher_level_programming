#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user
with the given letter as a parameter."""
from sys import argv
import requests

if __name__ == "__main__":
    if len(argv) > 1:
        data = {'q': argv[1]}
    else:
        data = {'q': ""}

    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data=data)

    try:
        body = response.json()
        if body:
            print("[{}] {}".format(body.get('id'), body.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
