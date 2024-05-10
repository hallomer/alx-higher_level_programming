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
        response_body = response.json()
        if response_body:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
