#!/bin/bash
# Displays all HTTP methods the server will accept
curl -sI "$1" | grep -i Allow | awk '{gsub(",", "\n"); print substr($0, index($0,$2))}'
