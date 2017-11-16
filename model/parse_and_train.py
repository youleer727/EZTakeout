"""
parse_and_clean.py is for parsing data from .processed.csv and training model
"""

from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext
import numpy as np
import pandas as pd
from pandas import DataFrame
import os.path
from os import listdir
from sklearn import linear_model
import sklearn.externals
from sklearn.externals import joblib

conf = SparkConf().setAppName("eecs6893")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

DATASETS_PATH = os.path.abspath(os.path.dirname(__file__)) + '/datasets/'
YEAR = 2016
MONTH = 6


def parseMonth(i):
    if (i < 10):
        return '0' + str(i)
    else:
        return str(i)

def new_file_name(s):
    tokens = s.split()
    return tokens[0] + '-' + convert_time(tokens[1])

def convert_time(time):
    return time.split(':')[0]

def parse_start_time(col):
    return int(col.split()[1].split(':')[0]) / 3 + 1

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

def proc():
    global YEAR, MONTH
    store_dir = 'testdir/'
    while (True):
        file = str(YEAR) + '-' + parseMonth(MONTH) + '.extracted.csv'
        taxiFile = sc.textFile(DATASETS_PATH + 'processed/tripdata/' + file)
        taxiFileHeader = taxiFile.filter(lambda l: 'tpep_pickup_datetime' in l)
        taxiFileContent = taxiFile.subtract(taxiFileHeader)
        lines = taxiFileContent.map(lambda line: line.split(','))
        RDD = lines.map(lambda cols: (
        # Note that per now we do not include dropoff time
        new_file_name(cols[0]), (parse_start_time(cols[0]), int(cols[2]), float(cols[3]), float(cols[4])))).reduceByKey(lambda a, b: appendAB(a, b))
        sqlDF = sqlContext.createDataFrame(RDD, ['fileName', 'data'])
        dfMatrix = sqlDF.toPandas().as_matrix()

        for i in range(0, dfMatrix.shape[0]):
            row = dfMatrix[i]
            df = DataFrame(row[1], columns=['tpep_pickup_datetime', 'passenger_count', 'trip_distance', 'total_amount'])
            df.to_csv(path_or_buf=(DATASETS_PATH + 'tripdata_reduced/' + row[0] + '.csv').encode('ascii', 'ignore'), index=False)


def main():
    proc()


if __name__ == '__main__':
    main()