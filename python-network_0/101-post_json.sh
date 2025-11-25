#!/bin/bash
# Script that sends a JSON POST request and displays the response body
curl -sS -X POST -H "Content-Type: application/json" -d @"$2" "$1"
