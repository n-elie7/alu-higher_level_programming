#!/usr/bin/python3
"""Lists 10 most recent commits from a GitHub repository"""

import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner_name, repo_name)

    params = {"per_page": 10}

    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            commits = response.json()

            for commit in commits:
                sha = commit.get("sha")
                author_name = commit.get("commit").get("author").get("name")
                print("{}: {}".format(sha, author_name))
    except (requests.exceptions.RequestException, AttributeError, KeyError):
        pass
