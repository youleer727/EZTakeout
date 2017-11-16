import os
import pandas as pd

DATASETS_PATH = os.path.abspath(os.path.dirname(__file__)) + '/datasets/'

"""
The attribute we want are
tpep_pickup_datetime, tpep_dropoff_datetime, passenger_count, trip_distance, total_amount
"""

"""
datasets:
yellow_trip_data_2016-06.csv - yellow_trip_data_2017-06.csv
"""

TRIPDATA_ATTRIBUTES = ['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count', 'trip_distance', 'total_amount']
DATA_PREFIX= 'yellow_tripdata_'
MONTH_RANGE = ['2016-06', '2016-07', '2016-08', '2016-09', '2016-10',
               '2016-11', '2016-12', '2017-01', '2017-02', '2017-03', '2017-04',
               '2017-05', '2017-06']
FAKE_RANGE = ['2016-07']



def extract_attribute_from_yellow_tripdata(postfix='2016-06'):
    print 'Reading ' + DATA_PREFIX + postfix + '.csv'
    df = pd.read_csv(DATASETS_PATH + 'raw/' + DATA_PREFIX + postfix + '.csv')
    df[TRIPDATA_ATTRIBUTES].to_csv(DATASETS_PATH + 'processed/tripdata/' + postfix + '.extracted.csv', index=False)
    del df


def main():
    for val in MONTH_RANGE:
        extract_attribute_from_yellow_tripdata(val)
        print val + ' is complete'


if __name__ == '__main__':
    main()







