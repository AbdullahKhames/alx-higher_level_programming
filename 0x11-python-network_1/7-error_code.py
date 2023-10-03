#!/usr/bin/python3
"""module documented"""
from requests import get, exceptions
from sys import argv


def connect():
    """function to connect to check status documented"""
    url = argv[1]
    resp = get(url)
    if resp:
        print(resp.text)
    else:
        print(f'Error code: {resp.status_code}')


if __name__ == '__main__':
    """function to connect to check status documented"""
    connect()
