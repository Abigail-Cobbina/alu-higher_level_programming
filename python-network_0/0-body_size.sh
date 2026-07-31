#!/bin/bash
# Sends a request and displays the size of the response body
curl -s -o /dev/null -w "%{size_download}" "$1"
