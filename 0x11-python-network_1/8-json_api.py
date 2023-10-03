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
        try:
            text = resp.json()
        except Exception:
            print('Not a valid JSON')
            return
        if not text:
            print('No result')
            return
        else:
            print(f'[{text["id"]}] {text["name"]}')
    else:
        print(f'Error code: {resp.status_code}')


if __name__ == '__main__':
    """function to connect to check status documented"""
    connect()
