#!/bin/bash
set -e

echo "********************************************"
echo "Starting ${GITHUB_REPOSITORY}-${GITHUB_WORKFLOW}:${GITHUB_ACTION}"
echo "********************************************"


sh -c pytest "$*"

echo "********************************************"
echo "Completed ${GITHUB_REPOSITORY}-${GITHUB_WORKFLOW}:${GITHUB_ACTION}"
echo "********************************************"