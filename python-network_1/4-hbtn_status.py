#!/usr/bin/python3
"""Fetches url using requests module."""

import requests


url = "https://intranet.hbtn.io/status"

response = requests.get(url)
content = response.text

print("Body response:")
print(f"\t- type: {type(content)}")
print(f"\t- content: {content}")
