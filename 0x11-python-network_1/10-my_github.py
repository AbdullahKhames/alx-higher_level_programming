#!/usr/bin/python3
"""module documented"""
from requests.auth import HTTPBasicAuth
from requests import get
from sys import argv


def connect():
    """function to connect to check status documented"""
    url = 'https://api.github.com/user'
    resp = get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    if resp:
        text = resp.json()
        print(text["id"])
    else:
        print(f'Error code: {resp.status_code}')


if __name__ == '__main__':
    """function to connect to check status documented"""
    connect()
