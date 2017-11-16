"""
data_clean.py is for tripdata cleaning
"""

import os

DATASETS_PATH = os.path.abspath(os.path.dirname(__file__)) + '/datasets/'
DATA_PREFIX= 'yellow_tripdata_'
MONTH_RANGE = ['2016-06', '2016-07', '2016-08', '2016-09', '2016-10',
               '2016-11', '2016-12', '2017-01', '2017-02', '2017-03', '2017-04',
               '2017-05', '2017-06']
FAKE_RANGE = ['2016-07']

def clean():
    for i in FAKE_RANGE:
        with open(DATASETS_PATH + 'raw/' + DATA_PREFIX + i + '.csv', "w") as infile:
            for line in infile:
                if line[::-1][2:4] == ',,':




def main():
    clean()


if __name__ == '__main__':
    main()