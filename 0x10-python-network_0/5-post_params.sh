#!/bin/bash
# file to connect to given domain name and get its response content lenght
curl -s -X POST -d '{"email": "test@gmail.com", "subject": "I will always be here for PLD"}' "$1"
