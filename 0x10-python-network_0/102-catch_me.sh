#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me specify origin and user
curl -s -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
