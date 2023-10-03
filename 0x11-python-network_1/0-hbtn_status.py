#!/usr/bin/python3
from urllib import request


def connect():
    with request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        body = resp.read()
    char_set = resp.headers.get_content_charset()
    decoded_body = body.decode(char_set)
    print(decoded_body)


if __name__ == '__main__':
    connect()
