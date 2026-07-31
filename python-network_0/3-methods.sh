#!/bin/bash
# Sends an OPTIONS request and displays accepted HTTP methods
curl -s -X OPTIONS -i "$1" | grep Allow | cut -d' ' -f2-
