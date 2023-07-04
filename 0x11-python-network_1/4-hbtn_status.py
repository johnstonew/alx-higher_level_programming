#!/usr/bin/python3
#  Python script that fetches https://alx-intranet.hbtn.io/status
import requests

def get_request():
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))


if __name__ == "__main__":
    get_request()
