#!/usr/bin/python3
"""sends a request to the URL and displays the value"""

from urllib import request, error
import sys


if len(sys.argv) == 2:
    url = sys.argv[1]


def fetch_header(url):
    """fetch and print value of header"""
    try:
        with request.urlopen(url) as response:
            headers = response.headers
            id_header = headers.get("X-Request-Id")
            print(id_header)
        return True
    except error.URLError:
        return False


fetch_header(url)
