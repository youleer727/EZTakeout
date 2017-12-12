import pandas as pd
import sys
import os
from os import listdir
from sklearn import linear_model
from sklearn.externals import joblib
import matplotlib.patches as mpatches



"""
training method needs to be modified
"""

tripdata_reduced_path = os.path.abspath(os.path.dirname(__file__)) + '/datasets/' + 'processed/tripdata_reduced/'

def linear_regression_train_model_amount():
    data_list = []
    lable_list = []
    for file in listdir(tripdata_reduced_path):
        if (file == '.DS_Store'):
            continue
        try:
            df = pd.read_csv(tripdata_reduced_path + file,
                             usecols=['start_hour', 'passenger_count', 'trip_distance', 'total_amount', 'time_spent'],
                             header=0)
            data_list.append(df[['start_hour','total_amount']])
            lable_list.append(df[['trip_distance']])
        except:
            pass
    train_data_df = pd.concat(data_list)
    train_lable_df = pd.concat(lable_list)
    train_data = train_data_df.as_matrix()
    train_labels = train_lable_df.values.flatten()
    clf = linear_model.LinearRegression()
    model = clf.fit(train_data, train_labels)
    joblib.dump(model, 'trip_distance.linear_regression_model.amount.pkl')

def linear_regression_train_model_time():
    data_list = []
    lable_list = []
    for file in listdir(tripdata_reduced_path):
        if (file == '.DS_Store'):
            continue
        try:
            df = pd.read_csv(tripdata_reduced_path + file,
                             usecols=['start_hour', 'passenger_count', 'trip_distance', 'total_amount', 'time_spent'],
                             header=0)
            data_list.append(df[['start_hour','time_spent']])
            lable_list.append(df[['trip_distance']])
        except:
            pass
    train_data_df = pd.concat(data_list)
    train_lable_df = pd.concat(lable_list)
    train_data = train_data_df.as_matrix()
    train_labels = train_lable_df.values.flatten()
    clf = linear_model.LinearRegression()
    model = clf.fit(train_data, train_labels)
    joblib.dump(model, 'trip_distance.linear_regression_model.time.pkl')

def train_single_month_amount(year, month):
    data_list = []
    lable_list = []
    prefix = str(year) + '-' + convertMonth(month)
    print 'training ' + prefix
    for file in listdir(tripdata_reduced_path):
        if file.startswith(prefix):
            try:
                df = pd.read_csv(tripdata_reduced_path + file,
                                 usecols=['start_hour', 'passenger_count', 'trip_distance', 'total_amount',
                                          'time_spent'],
                                 header=0)
                data_list.append(df[['start_hour', 'total_amount']])
                lable_list.append(df[['trip_distance']])
            except:
                pass
    train_data_df = pd.concat(data_list)
    train_lable_df = pd.concat(lable_list)
    train_data = train_data_df.as_matrix()
    train_labels = train_lable_df.values.flatten()
    clf = linear_model.LinearRegression()
    model = clf.fit(train_data, train_labels)
    joblib.dump(model, prefix +'.amount.pkl')


def train_single_month_time(year, month):
    data_list = []
    lable_list = []
    prefix = str(year) + '-' + convertMonth(month)
    print 'training ' + prefix
    for file in listdir(tripdata_reduced_path):
        if file.startswith(prefix):
            try:
                df = pd.read_csv(tripdata_reduced_path + file,
                                 usecols=['start_hour', 'passenger_count', 'trip_distance', 'total_amount',
                                          'time_spent'],
                                 header=0)
                data_list.append(df[['start_hour','time_spent']])
                lable_list.append(df[['trip_distance']])
            except:
                pass
    train_data_df = pd.concat(data_list)
    train_lable_df = pd.concat(lable_list)
    train_data = train_data_df.as_matrix()
    train_labels = train_lable_df.values.flatten()
    clf = linear_model.LinearRegression()
    model = clf.fit(train_data, train_labels)
    joblib.dump(model, prefix +'.time.pkl')

def train():
    years = [2016, 2016, 2016, 2016, 2016, 2016, 2017, 2017, 2017, 2017, 2017, 2017]
    months = [6, 7, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6]
    for i in range(len(years)):
        train_single_month_amount(years[i], months[i])
        train_single_month_time(years[i], months[i])
    linear_regression_train_model_amount()
    linear_regression_train_model_time()

def convertMonth(month):
    if month < 10:
        return '0' + str(month)
    return str(month)

if __name__ == '__main__':
    train()


