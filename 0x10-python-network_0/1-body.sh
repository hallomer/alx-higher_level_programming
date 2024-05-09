#!/bin/bash
# Displays body of a 200 status code response
response=$(curl -s -o /dev/null -w "%{http_code}" "$1") && [ "$response" == "200" ] && curl -s "$1"