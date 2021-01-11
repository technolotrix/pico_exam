#!/bin/bash

source config/performance_settings.sh

# -p to POST data
# -T to define content-type header
# -H to send header (e.g. auth token)
# -c to specify concurrency
# -n to specify number of requests
# -g to specify gnu output file
echo "Writing results to $OUTPUTFILE"
ab -p data/post_payload.txt -T application/json -H "Authorization: $AUTH_TOKEN" -c $CONCURRENCY -n $NUM_REQUESTS -g $OUTPUTFILE $PERFORMANCE_URL

# Plot results
python libs/histogram.py
