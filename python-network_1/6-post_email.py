#!/usr/bin/python3
"""post email"""

import requests
import sys


if len(sys.argv) == 3:
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}

    with requests.post(url=url, params=data) as response:
        result = response.text
        print(result)
