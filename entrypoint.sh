#!/bin/sh -xe
set -e

echo $PWD

echo "$(ls)"

if [[ -z "${RUNNER_WORKSPACE}"]]; then
    cd "${RUNNER_WORKSPACE}"
fi

echo $PWD

echo "$(ls)"

python ./main.py $*
