#!/usr/bin/python3
"""script that fetches a url"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read().decode('utf-8')

print('- Body response:')
print('\t', body)
