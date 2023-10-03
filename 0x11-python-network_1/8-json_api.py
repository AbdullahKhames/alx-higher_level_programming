#!/usr/bin/python3
"""module documented"""
from requests import post, exceptions
from sys import argv


def connect():
    """function to connect to check status documented"""
    if len(argv) < 2:
        searched = ""
    else:
        searched = argv[1]
    data = {'q': searched}
    url = 'http://0.0.0.0:5000/search_user'
    resp = post(url, data=data)
    if resp:
        text = resp.json()
        if not text:
            print('No result')
            return
        elif not is_json(text):
            print('Not a valid JSON')
            return
        else:
            print(f'[{text["id"]}] {text["name"]}')
    else:
        print(f'Error code: {resp.status_code}')


def is_json(text):
    """function to check if str is json or not"""
    if not type(text) == dict:
        return False
    return True


if __name__ == '__main__':
    """function to connect to check status documented"""
    connect()
