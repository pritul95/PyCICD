#!/bin/sh -xe
set -e

echo $PWD

echo "$(ls)"

python ./main.py $*
