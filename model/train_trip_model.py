import pandas as pd
import os
from os import listdir
from sklearn import linear_model
from sklearn.externals import joblib
import time
from utils import datasets_path, raw_data_path, trip_data_attributes, trip_data_prefix, month_range, trip_data_suffix


def linear_regression_train_model():
    data_list = []
    lable_list = []
    tripdata_reduced_path = datasets_path + 'processed/tripdata_reduced/'
    for file in listdir(tripdata_reduced_path):
        if (file != '.DS_Store'):
            try:
                df = pd.read_csv(tripdata_reduced_path + file,
                                 usecols=['start_hour', 'passenger_count', 'trip_distance', 'total_amount', 'time_spent'],
                                 header=0)
                data_list.append(df[['start_hour', 'passenger_count', 'trip_distance']])
                lable_list.append(df[['total_amount']])
            except:
                pass
    train_data_df = pd.concat(data_list)
    train_lable_df = pd.concat(lable_list)
    train_data = train_data_df.as_matrix()
    train_labels = train_lable_df.values.flatten()
    clf = linear_model.LinearRegression()
    model = clf.fit(train_data, train_labels)
    joblib.dump(model, 'total_amount.linear_regression_model.pkl')

if __name__ == '__main__':
    linear_regression_train_model()