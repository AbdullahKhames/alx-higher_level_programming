#!/usr/bin/python3
"""module documented"""
from requests import get
from sys import argv


def connect():
    """function to connect to check status documented"""
    heads = {'accept': 'application/vnd.github+json'}
    params = {'per_page': 10}
    url = f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits'
    resp = get(url, params=params, headers=heads)
    if resp:
        text = resp.json()
        for i in range(len(text)):
            print(f"{text[i]['sha']}: {text[i]['commit']['author']['name']}")
    else:
        print(f'None')


if __name__ == '__main__':
    """function to connect to check status documented"""
    connect()
