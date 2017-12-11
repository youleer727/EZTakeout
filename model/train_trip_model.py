import pandas as pd
import sys
import os
from os import listdir
from sklearn import linear_model
from sklearn.externals import joblib


"""
training method needs to be modified
"""


def linear_regression_train_model():
    data_list = []
    lable_list = []
    tripdata_reduced_path = os.path.abspath(os.path.dirname(__file__)) + '/datasets/' + 'processed/tripdata_reduced/'
    for file in listdir(tripdata_reduced_path):
        if (file == '.DS_Store'):
            continue
        try:
            df = pd.read_csv(tripdata_reduced_path + file,
                             usecols=['start_hour', 'passenger_count', 'trip_distance', 'total_amount', 'time_spent'],
                             header=0)
            data_list.append(df[['start_hour', 'passenger_count', 'total_amount', 'time_spent']])
            lable_list.append(df[['trip_distance']])
        except:
            pass
    train_data_df = pd.concat(data_list)
    train_lable_df = pd.concat(lable_list)
    train_data = train_data_df.as_matrix()
    train_labels = train_lable_df.values.flatten()
    clf = linear_model.LinearRegression()
    model = clf.fit(train_data, train_labels)
    joblib.dump(model, 'trip_distance.linear_regression_model.pkl')

if __name__ == '__main__':
    linear_regression_train_model()