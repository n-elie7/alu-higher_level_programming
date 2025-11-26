#!/usr/bin/python3
"""error code"""

from urllib import request, error
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            result = response.read().decode("utf-8")
            print(result)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
