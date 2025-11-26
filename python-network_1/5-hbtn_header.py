#!/usr/bin/python3
"""get specific header"""

import requests
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]

    with requests.get(url) as response:
        headers = response.headers
        id_header = headers.get("X-Request-Id")
        print(id_header)
