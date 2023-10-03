#!/usr/bin/python3
"""module documented"""
from urllib import request


def connect():
    """function to connect to check status documented"""

    with request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        body = resp.read()
    char_set = resp.headers.get_content_charset()
    decoded_body = body.decode(char_set)
    print('Body response:')
    print(f'\t- type: {type(body)}')
    print(f'\t- content: {body}')
    print(f'\t- utf8 content: {decoded_body}')


if __name__ == '__main__':
    """function to connect to check status documented"""
    connect()
