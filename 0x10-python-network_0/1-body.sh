#!/bin/bash
# file to connect to given domain name and get its response content lenght
url="$1"
status_code=$(curl --silent --head --output /dev/null --write-out "%{http_code}" "$url")
if [ "$status_code" -eq 200 ]; then
  echo "$(curl -sL "$url")"
fi
