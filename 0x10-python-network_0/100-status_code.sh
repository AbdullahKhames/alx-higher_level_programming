#!/bin/bash
# file to connect to given domain name and get its response content lenght
curl --silent --output /dev/null --write-out "%{http_code}" "$1"
