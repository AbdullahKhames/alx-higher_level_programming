#!/usr/bin/python3
"""module documented"""
from requests import post, exceptions
from sys import argv


def connect():
    """function to connect to check status documented"""
    data = {'email', argv[2]}
    url = argv[1]
    try:
        resp = post(url, data=data)
        print(resp.text)
    except exceptions.HTTPError as ex:
        print(f'Error code: {ex.getcode()}')


if __name__ == '__main__':
    """function to connect to check status documented"""
    connect()
