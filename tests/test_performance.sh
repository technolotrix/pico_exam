#!/bin/bash
source .env

echo $AUTH_TOKEN
echo $OUTPUTFILE
echo $PERFORMANCE_URL


# -p to POST data
# -T to define content-type header
# -H to send header (e.g. auth token)
# -c to specify concurrency
# -n to specify number of requests

ab -p data/post_payload.txt -T application/json -H "Authorization: $AUTH_TOKEN" -c 10 -n 1000 -g $OUTPUTFILE $PERFORMANCE_URL
