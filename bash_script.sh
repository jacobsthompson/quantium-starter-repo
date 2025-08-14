#!/bin/bash

echo "Entering Virtual Environment"
source venv/bin/activate
echo "Starting Test..."
pytest test_app.py --webdriver Firefox --headless
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo "Tests Passed"
    exit 0
else
  echo "Tests Failed with code $EXIT_CODE"
  exit 1
fi
