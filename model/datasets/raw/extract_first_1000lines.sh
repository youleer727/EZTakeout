#!/usr/bin/env bash
# this shell is used to extract first 1000 lines from a file into a new file
# head -1000 input > output && sed -i '1,+999d' input
head -1000 2016-06-first-1000.txt > 2016-06-first-1000.csv && sed -i '1,+999d' 2016-06-first-1000.txt
