#!/bin/bash

# python -m venv qa_dev
# source qa_dev/bin/activate
# pip install -r requirements.txt


bash tests/performance/performance.sh &
nosetests -vs tests/ui/

