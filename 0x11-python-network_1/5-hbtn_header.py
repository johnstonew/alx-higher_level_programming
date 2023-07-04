#!/usr/bin/python3
#  Python script that takes in a URL
import requests
from sys import argv


def get_request(url: str):
    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))


if __name__ == "__main__":
    get_request(argv[1])
