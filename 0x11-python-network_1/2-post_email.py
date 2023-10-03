#!/usr/bin/python3
"""module documented"""
from urllib import request, parse
from sys import argv


def connect():
    """function to connect to check status documented"""
    values = {'email': argv[2]}
    values = parse.urlencode(values)
    data = values.encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as resp:
        body = resp.read()
    decoded_body = body.decode('utf-8')
    print(decoded_body)


if __name__ == '__main__':
    """function to connect to check status documented"""
    connect()
