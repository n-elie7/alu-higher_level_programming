#!/bin/bash
# Script that takes a URL and displays the size of the response body in bytes
curl -s "$1" | wc -c
