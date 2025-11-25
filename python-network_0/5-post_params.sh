#!/bin/bash
# A script that sends an HTTP request with a custom header
curl -sX POST --data "email=test@gmail.com&subject=I will always be here for PLD" "$1"
