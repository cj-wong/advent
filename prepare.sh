#!/usr/bin/env bash
#
# Prepare skeleton files for a day in Advent of Code
#
# Args:
#   $1: year
#   $2: day

if [[ -z "$1" || -z "$2" ]]; then
    echo "Usage: prepare.sh <year> <day>"
    exit 1
fi

ROOT=$(dirname "$0")
DIR="${ROOT}/${1}/${2}"

mkdir -p "$DIR"
pushd "$DIR" || (echo "Could not enter directory" && exit 2)
ln -s ../../common/config.py .
cp ../../common/a.py .
touch test_input.txt
touch input.txt
