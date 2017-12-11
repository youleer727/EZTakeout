import os

datasets_path = os.path.abspath(os.path.dirname(__file__)) + '../datasets/'
raw_data_path = datasets_path + 'raw/'
"""
The trip attributes we want are
tpep_pickup_datetime, tpep_dropoff_datetime, passenger_count, trip_distance, total_amount
"""
trip_data_attributes = ['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count', 'trip_distance', 'total_amount']
trip_data_prefix= 'yellow_tripdata_'
trip_data_suffix = 'processed/tripdata/'
month_range = ['2016-06', '2016-07', '2016-08', '2016-09', '2016-10',
               '2016-11', '2016-12', '2017-01', '2017-02', '2017-03', '2017-04',
               '2017-05', '2017-06']







