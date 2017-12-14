import sys
from sklearn import linear_model
from sklearn.externals import joblib
# 'start_hour', 'passenger_count', 'total_amount', 'time_spent'
import datetime
import os.path

# TODO: modify predict scheme focusing on month instead of year

def convertMonth(month):
    if month < 10:
        return '0' + str(month)
    return str(month)

now = datetime.datetime.now()
year = now.year
month = now.month
target_amount_file = str(year) + '-' + str(convertMonth(month)) + '.amount.pkl'
target_time_file = str(year) + '-' + str(convertMonth(month)) + '.time.pkl'
start_hour = float(sys.argv[1])
passenger_count = float(sys.argv[2])
total_amount = float(sys.argv[3])
time_spent = float(sys.argv[4])
if os.path.isfile(target_amount_file) and os.path.isfile(target_time_file):
    clf_amount = joblib.load(target_amount_file)
    val1 = clf_amount.predict([[start_hour, total_amount]])[0]
    clf_time = joblib.load(target_time_file)
    val2 = clf_time.predict([start_hour, time_spent])[0]
    if val1 > val2:
        print val1
    else:
        print val2
else:
    clf_amount = joblib.load('trip_distance.linear_regression_model.amount.pkl')
    val1 = clf_amount.predict([[start_hour, total_amount]])[0]
    clf_time = joblib.load('trip_distance.linear_regression_model.time.pkl')
    val2 = clf_time.predict([[start_hour, time_spent]])[0]
    if val1 > val2:
        print val1
    else:
        print val2


