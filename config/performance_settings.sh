#!/bin/bash

PT_FILENAME=`date '+%F_%H_%M_%S'`;
echo "${PT_FILENAME}"

CONCURRENCY=20
NUM_REQUESTS=500
AUTH_TOKEN='Token fake1234'
PERFORMANCE_URL='https://jsonplaceholder.typicode.com/posts'
OUTPUTFILE=$PWD/tmp/performance_$PT_FILENAME.dat
