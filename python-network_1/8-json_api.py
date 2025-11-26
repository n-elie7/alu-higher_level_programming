#!/usr/bin/python3
"""json api"""

import requests
import sys

if len(sys.argv) == 2:
    param = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": param}

    try:
        # Send POST request
        response = requests.post(url, data=data)

        # Try to parse JSON
        try:
            json_response = response.json()

            # Check if JSON is empty
            if json_response:
                print(
                    "[{}] {}".format(json_response.get("id"), 
                                     json_response.get("name"))
                )
            else:
                print("No result")
        except ValueError:
            # JSON parsing failed
            print("Not a valid JSON")
    except requests.exceptions.RequestException:
        # Handle connection errors
        print("No result")
