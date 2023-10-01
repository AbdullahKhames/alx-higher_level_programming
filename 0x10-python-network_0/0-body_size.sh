#!/bin/bash
# file to connect to given domain name and get its response content lenght
curl -sI "$1" | grep -i '^Content-Length:' | awk '{print $2}'
