#!/usr/bin/python3
"""error-code"""

import requests
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]

    try:
        result = requests.get(url)
        print(result.text)
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e}")
