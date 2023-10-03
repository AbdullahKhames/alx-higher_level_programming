#!/usr/bin/python3
"""module documented"""
from requests import get, exceptions


def connect():
    """function to connect to check status documented"""
    try:
        resp = get('https://alx-intranet.hbtn.io/status')
        body = resp.text
        print('Body response:')
        print(f'\t- type: {type(body)}')
        print(f'\t- content: {body}')
    except exceptions.HTTPError as ex:
        print(f'Error code: {ex.getcode()}')


if __name__ == '__main__':
    """function to connect to check status documented"""
    connect()
