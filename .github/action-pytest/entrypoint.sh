#!/bin/sh -xe
set -e

echo "********************************************"
echo "Starting ${GITHUB_REPOSITORY}-${GITHUB_WORKFLOW}:${GITHUB_ACTION}"


sh -c "$*"

echo "Completed ${GITHUB_REPOSITORY}-${GITHUB_WORKFLOW}:${GITHUB_ACTION}"
echo "********************************************"