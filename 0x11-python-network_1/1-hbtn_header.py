#!/usr/bin/python3
"""module documented"""
from urllib import request
from sys import argv


def connect():
    """function to connect to check status documented"""

    with request.urlopen(argv[1]) as resp:
        body = resp.read()
    resp_id = resp.getheader('X-Request-Id')
    print(resp_id)


if __name__ == '__main__':
    """function to connect to check status documented"""
    connect()
