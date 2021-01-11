#!/bin/bash

source .env

# nosetests -vs tests/test_onboarding_wizard.py &
bash tests/test_performance.sh
python histogram.py

