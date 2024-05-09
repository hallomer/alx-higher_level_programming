#!/bin/bash
# Displays the size of the body response for a given URL
echo "$(curl -s "$1" -o /dev/null -w "%{size_download}")"
