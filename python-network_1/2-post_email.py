#!/usr/bin/python3
"""send data"""

from urllib import request, parse
import sys

if len(sys.argv) == 3:
    url = sys.argv[1]
    email = sys.argv[2]

    params = {"email": email}
    query_string = parse.urlencode(params).encode("utf-8")

    request_object = request.Request(url=url, data=query_string, method="POST")

    with request.urlopen(request_object) as response:
        result = response.read()
        response_string = result.decode("utf-8")
        print(response_string)
