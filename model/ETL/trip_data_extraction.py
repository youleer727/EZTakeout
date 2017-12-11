import pandas as pd
from utils import datasets_path, raw_data_path, trip_data_attributes, trip_data_prefix, month_range, trip_data_suffix
import time


def extract():
    t0 = time.time()
    for month in month_range:
        single_dataset_extract(month)
    print 'Extracting attributes complete, Elapsed time : ' + str(time.time() - t0)


def single_dataset_extract(month):
    t = time.time()
    dataset = trip_data_prefix + month + '.csv'
    print 'Extracting attributes from dataset ' + dataset
    input_path = raw_data_path + dataset
    output_path = datasets_path + trip_data_suffix + month + '.extracted.csv'
    df = pd.read_csv(input_path)
    df[trip_data_attributes].to_csv(output_path, index=False)
    print str(sum(1 for line in open(output_path))) + ' lines extracted'
    print 'Elapsed time : ' + str(time.time() - t) + ' s'
    del df


def main():
    extract()


if __name__ == '__main__':
    main()







