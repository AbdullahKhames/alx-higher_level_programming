#!/bin/bash
# file to connect to given domain name and get its response content lenght
curl -s -X POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
