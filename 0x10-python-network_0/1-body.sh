#!/bin/bash
# file to connect to given domain name and get its response content lenght
url="$1"
status_code=$(curl --head --silent --write-out "%{http_code}" "$url")
echo "$status_code"
if [ "$status_code" -eq 200 ]; then
  echo "$(curl -sL "$url")"
fi
