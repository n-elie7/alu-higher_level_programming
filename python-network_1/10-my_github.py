#!/usr/bin/python3
"""Uses GitHub API to display the user's id using Basic Authentication"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]  # personal access token as password

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print("None")
