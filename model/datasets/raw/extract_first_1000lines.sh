#!/usr/bin/env bash
# this shell is to extract first 1000 lines from a csv
head -1000 yellow_tripdata_2016-06.csv > 2016-06-first-1000.txt && sed -i '1,+999d' yellow_tripdata_2016-06.csv
