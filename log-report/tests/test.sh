#!/bin/bash
# pytest and pytest-json-ctrf are baked into environment/Dockerfile, so nothing
# is installed here at verify time.
set -uo pipefail

VERIFIER_DIR=/logs/verifier
mkdir -p "$VERIFIER_DIR"

pytest /tests/test_outputs.py -rA \
  --ctrf "$VERIFIER_DIR/ctrf.json"
status=$?

if [ "$status" -eq 0 ]; then
  echo 1 > "$VERIFIER_DIR/reward.txt"
else
  echo 0 > "$VERIFIER_DIR/reward.txt"
fi

exit 0
