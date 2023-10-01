#!/bin/bash
# file to connect to given domain name and get its response content lenght
curl -sIX OPTIONS "$1" | grep -i '^Allow:' | sed 's/^Allow: //i'
