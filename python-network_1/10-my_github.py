#!/usr/bin/python3
"""Uses GitHub API to display user id with Basic Authentication"""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, password))

        if response.status_code == 200:
            user_data = response.json()
            print(user_data.get("id"))
        else:
            print(None)
    except requests.exceptions.RequestException:
        print(None)
