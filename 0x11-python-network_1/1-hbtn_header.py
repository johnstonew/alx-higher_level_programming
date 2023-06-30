#!/usr/bin/python3
"""script that makes a request to the url and gets a header value"""
import urllib.request
import sys

url = sys.argv[1]

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    x_request_id = response.headers.get('X-Request-Id')

print('X-Request-Id:', x_request_id)
