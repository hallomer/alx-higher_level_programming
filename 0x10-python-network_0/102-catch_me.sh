#!/bin/bash
# Makes the server to respond with "You got me!"
curl -s 0.0.0.0:5000/catch_me -o /dev/null
