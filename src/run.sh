#!/bin/bash

if [ "$MODE" = "test" ]; then
  ./test.sh
else
  smee -u $SMEE_LINK --target http://127.0.0.1:3000/github-event &
  poetry run uvicorn main:app --host 0.0.0.0 --port 3000
fi
