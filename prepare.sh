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
elif [[ "$2" == "latest" ]]; then
    last=$(find "$1" -mindepth 1 -maxdepth 1 -type d \
        | cut --delimiter=/ --fields=2 \
        | sort -n \
        | tail -n 1)
    day=$(echo "${last} + 1" | bc )
else
    day="$2"
fi

ROOT=$(dirname "$0")
DIR="${ROOT}/${1}/${day}"

mkdir -p "$DIR"
pushd "$DIR" || (echo "Could not enter directory" && exit 2)
ln -s ../../common/config.py .
if [ ! -e a.py ]; then
    cp ../../common/a.py .
fi
touch test_input.txt
touch input.txt
