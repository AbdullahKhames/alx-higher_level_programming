#!/usr/bin/python3
"""module documented"""
from urllib import request, parse, error
from sys import argv


def connect():
    """function to connect to check status documented"""
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as resp:
            body = resp.read()
        decoded_body = body.decode('utf-8')
        print(decoded_body)
    except error.HTTPError as ex:
        print(f'Error code: {ex.getcode()}')


if __name__ == '__main__':
    """function to connect to check status documented"""
    connect()
