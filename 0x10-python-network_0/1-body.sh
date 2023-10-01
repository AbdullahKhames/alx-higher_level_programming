#!/bin/bash
# file to connect to given domain name and get its response content lenght
url="$1"
status_code=$(curl --head --silent --write-out "%{http_code}" "$url")
if [ "$status_code" -eq 200 ]; then
  response=$(curl -sL "$url")
  echo "$response"
fi
