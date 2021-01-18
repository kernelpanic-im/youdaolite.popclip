#!/bin/bash

TEST_INPUT=(
    "today"
    "is"
    "a"
    "sad"
    "day"
    "今天是悲伤的一天"
    "today is a sad day"
    "queue"
    "rqworker"
    "rqinfo"
)

COUNT=${#TEST_INPUT[@]}

for ((i=0; i<$COUNT; i++)); do
    export POPCLIP_TEXT="${TEST_INPUT[$i]}"
    printf "test $POPCLIP_TEXT:"
    python3 youdaolite.py
done
