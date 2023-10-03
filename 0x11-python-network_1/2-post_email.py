#!/usr/bin/python3
"""module documented"""
from urllib import request
from sys import argv


def connect():
    """function to connect to check status documented"""
    values = {'email': argv[2]}
    values = request.parse.urlencode(values)
    data = values.encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as resp:
        body = resp.read()
    resp_id = resp.getheader('X-Request-Id')
    print(resp_id)


if __name__ == '__main__':
    """function to connect to check status documented"""
    connect()
