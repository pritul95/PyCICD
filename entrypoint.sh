#!/bin/sh -xe
set -e

echo "********************************************"
echo "Starting ${GITHUB_REPOSITORY}-${GITHUB_WORKFLOW}:${GITHUB_ACTION}"


python ./main.py "$*"

echo "Completed ${GITHUB_REPOSITORY}-${GITHUB_WORKFLOW}:${GITHUB_ACTION}"
echo "********************************************"