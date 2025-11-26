#!/usr/bin/python3
"""Fetch status from local or remote URL with redirect support."""

from urllib import request, error


def fetch_status(url):
    """Try to fetch URL and print formatted output."""
    try:
        with request.urlopen(url) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode("utf-8")))
        return True
    except error.URLError:
        return False


if __name__ == "__main__":
    local_url = "http://127.0.0.1:5050/status"
    remote_url = "https://alu-intranet.hbtn.io/status"

    if not fetch_status(local_url):
        fetch_status(remote_url)
