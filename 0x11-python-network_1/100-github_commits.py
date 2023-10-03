#!/usr/bin/python3
"""module documented"""
from requests.auth import HTTPBasicAuth
from requests import get
from sys import argv


def connect():
    """function to connect to check status documented"""
    heads={'accept': 'application/vnd.github+json'}
    params = {'per_page': 15}
    url = f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits'
    resp = get(url, params=params, headers=heads, auth=HTTPBasicAuth('AbdullahKhames', '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'))
    print(resp.url)
    if resp:
        text = resp.json()
        for json_commit in text:
            print(json_commit)
            # print(json_commit['commit']["author"]["name"])
            # print(json_commit['sha'])
    else:
        print(f'None')


if __name__ == '__main__':
    """function to connect to check status documented"""
    connect()
