#!/usr/bin/python3
"""module documented"""
from requests import get, exceptions
from sys import argv


def connect():
    """function to connect to check status documented"""
    url = argv[1]
    try:
        resp = get(url)
        req_id = resp.headers['X-Request-Id']
        print(req_id)
    except exceptions.HTTPError as ex:
        print(f'Error code: {ex.getcode()}')


if __name__ == '__main__':
    """function to connect to check status documented"""
    connect()
