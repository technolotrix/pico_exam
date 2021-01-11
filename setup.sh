#!/bin/bash

python -m venv qa_dev
source qa_dev/bin/activate
pip install -r requirements.txt

# nosetests -vs tests/test_onboarding_wizard.py &
bash tests/test_performance.sh
python histogram.py

