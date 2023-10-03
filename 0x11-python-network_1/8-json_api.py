#!/usr/bin/python3
"""module documented"""
from requests import post, exceptions
from sys import argv


def connect():
    """function to connect to check status documented"""
    if len(argv) < 2:
        print('No result')
        return
    if len(argv) < 3:
        searched = ""
    else:
        searched = argv[2]
    data = {'q': searched}
    url = argv[1]
    resp = post(url, params=data)
    if resp:
        text = resp.text
        if len(text) == 0:
            print('No result')
        elif not is_json(text):
            print('Not a valid JSON')
    else:
        print(f'Error code: {resp.status_code}')


def is_json(text):
    """function to check if str is json or not"""
    if not type(text) == str:
        return False
    if not text[0] == '{' and not text[-1] == '}':
        return False
    return True

if __name__ == '__main__':
    """function to connect to check status documented"""
    connect()
