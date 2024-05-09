#!/bin/bash
# Gets the size of the response body for a given URL
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
