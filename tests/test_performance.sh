#!/bin/bash

# Ideally the following variables are in a different file
#  and sourced as env variables

PERFORMANCE_URL="http://example.com/api/v1/locations/"
NOW=`date '+%F_%H:%M:%S'`;
OUTPUTFILE="~/Desktop/pico_qa/tmp/histogram-$NOW.dat"

CONCURRENCY=10
NUM_REQUESTS=1000

# -p to POST data
# -T to define content-type header
# -H to send header (e.g. auth token)
# -c to specify concurrency
# -n to specify number of requests
# -g to specify gnu output file


ab -p data/post_payload.txt -T application/json -H "Authorization: $AUTH_TOKEN" -c $CONCURRENCY -n $NUM_REQUESTS -g $OUTPUTFILE $PERFORMANCE_URL
