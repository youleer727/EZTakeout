"""
month_day_reducer.py is to reduce data from .processed.csv
"""
import time
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pandas import DataFrame
from datetime import datetime
from utils import datasets_path, trip_data_suffix

conf = SparkConf().setAppName("EECS6893")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)


def parse_month(i):
    if (i < 10):
        return '0' + str(i)
    else:
        return str(i)

def generate_new_file_name(s):
    tokens = s.split()
    return tokens[0] + '-' + convert_time(tokens[1])

def convert_time(time):
    return time.split(':')[0]

def parse_start_time(col):
    return int(col.split()[1].split(':')[0])

def appendAB(a, b):
    if (type(a) is list and type(b) is not list):
        a.append(b)
        return a
    elif (type(b) is list and type(a) is not list):
        b.append(a)
        return b
    elif (type(a) is list and type(b) is list):
        return a + b
    else:
        row = [a]
        row.append(b)
        return row

def calculate_time(d1, d2):
    fmt = '%Y-%m-%d %H:%M:%S'
    t0 = datetime.strptime(d1, fmt)
    t1 = datetime.strptime(d2, fmt)
    d1_ts = time.mktime(t0.timetuple())
    d2_ts = time.mktime(t1.timetuple())
    return int(d2_ts - d1_ts) / 60


def reducer():
    year = 2016
    month = 6
    while (True):
        single_reduce(year, month)
        month += 1
        if(month == 13):
            year = 2017
            month = 1
        elif(month == 7):
            break


def single_reduce(year, month):
    input_file = str(year) + '-' + parse_month(month) + '.extracted.csv'
    input_path = datasets_path + trip_data_suffix + input_file
    trip_file = sc.textFile(input_path)
    trip_file_header = trip_file.filter(lambda l: 'tpep_pickup_datetime' in l)
    trip_file = trip_file.subtract(trip_file_header)
    lines = trip_file.map(lambda line: line.split(','))
    RDD = lines.map(lambda cols: (
        # Note that per now we do not include dropoff time
        generate_new_file_name(cols[0]), (parse_start_time(cols[0]), int(cols[2]), float(cols[3]), float(cols[4]),
                                          calculate_time(cols[0], cols[1])))).reduceByKey(lambda a, b: appendAB(a, b))
    sqlDF = sqlContext.createDataFrame(RDD, ['fileName', 'data'])
    dfMatrix = sqlDF.toPandas().as_matrix()
    for i in range(0, dfMatrix.shape[0]):
        row = dfMatrix[i]
        df = DataFrame(row[1], columns=['start_hour', 'passenger_count', 'trip_distance', 'total_amount', 'time_spent'])
        df.to_csv(path_or_buf=(datasets_path + 'processed/' + 'tripdata_reduced/' + row[0] + '.csv').encode('ascii', 'ignore'),
                  index=False)



def main():
    # reducer()
    single_reduce(2016, 8)


if __name__ == '__main__':
    main()