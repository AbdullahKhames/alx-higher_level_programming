#!/bin/bash
# file to connect to given domain name and get its response content lenght
curl -s -H "Content-Type: application/json" -X POST -d @"$2" "$1"
