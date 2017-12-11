"""
data_clean.py is for tripdata cleaning
"""
import fileinput
from utils import raw_data_path, trip_data_prefix, month_range
import time
import sys


def clean():
    t0 = time.time()
    for month in month_range:
        clean_single_file(month)
    print 'Tripdata cleaning complete, Elapsed time : ' + str(time.time() - t0)


def clean_single_file(month):
    t = time.time()
    cnt = 0
    dataset = trip_data_prefix + month + '.csv'
    print 'Cleaning dataset ' + dataset
    input_path = raw_data_path + dataset
    for line in fileinput.input(input_path, inplace=1):
        if ',,' in line:
            line = line.replace(',,', '')
            cnt += 1
        sys.stdout.write(line)
    print str(cnt) + ' lines cleaned'
    print 'Elapsed time : ' + str(time.time() - t) + ' s'



def main():
    clean()


if __name__ == '__main__':
    main()