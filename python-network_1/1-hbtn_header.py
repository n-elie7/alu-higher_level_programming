#!/usr/bin/python3
"""A script that takes a url, sends a request and prints a header."""
from urllib.request import urlopen
import sys
if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        with urlopen(url) as response:
            try:
                headers = response.headers
                id_header = headers.get("X-Request-Id")
                print(id_header)
            except Exception as error:
                print(error)
