#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status using requests module."""

import requests


url = "https://alu-intranet.hbtn.io/status"

response = requests.get(url)
content = response.text

print("Body response:")
print(f"\t- type: {type(content)}")
print(f"\t- content: {content}")
