import sys
from sklearn import linear_model
from sklearn.externals import joblib
from sklearn.datasets import load_digits
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import random
import numpy as np
import os
import csv
from sklearn.metrics import mean_squared_error, r2_score

years = [2016, 2016, 2016, 2016, 2016, 2016, 2017, 2017, 2017, 2017, 2017, 2017]
months = [6, 7, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6]

# trip_distance = float(sys.argv[1])
# passenger_count = float(sys.argv[2])
# total_amount = float(sys.argv[3])
# timespent = float(sys.argv[4])

clf_time = joblib.load('2017-03.time.pkl')
clf_amount = joblib.load('2017-03.amount.pkl')

# print clf.predict([[trip_distance, passenger_count, total_amount, time_spent]])[0]

start_hour = 6
def convertMonth(month):
    if month < 10:
        return '0' + str(month)
    return str(month)


def test():
    times = []
    for val in range(100):
        times.append(val)
    passenger_count = 1
    results_time = []
    results_amount = []

    for var in times:
        results_time.append(clf_time.predict([[start_hour, var]])[0])
        results_amount.append(clf_amount.predict([[start_hour, var]])[0])
    # for distance in distances:
    #     for amount in amounts:
    #         print 'distance is ' + str(distance)
    #         print 'amount is ' + str(amount)
    #         results.append(clf.predict([[start_hour , passenger_count, amount, distance]])[0])
    # # print distances
    # # print amounts
    # # print results
    # plt.plot(times, results_time)
    # # plt.plot(times, results_amount)
    # plt.xlabel('time')
    # plt.show()

    path = "./20170401"
    files = os.listdir(path)
    for file in files:
        print file
    distance = []
    amount = []
    time = []
    for file in files:
        if not os.path.isdir(file):
            flag = 1
            with open(path + "/" + file) as f:
                lines = csv.reader(f)
                for line in lines:
                    if flag:
                        flag = 0
                        continue
                    distance.append(float(line[2]))
                    amount.append(float(line[3]))
                    time.append(float(line[4]))

    plt.scatter(time, distance, s=1)
    plt.xlabel('time')
    plt.plot(times, results_time, c='r')

    # plt.scatter(amount, distance, s=10)
    # plt.xlabel('money spent')
    # plt.plot(times, results_amount, c='r')

    plt.ylabel('distance')

    plt.axis([0, 100, 0, 30])
    plt.show()


def test_start_time():
    start_time = [i for i in range(0,24)]
    times = []
    for val in range(100):
        times.append(val)
    results_time = []
    results_amount = []
    for s in start_time:
        temp = []
        model = '2016-09.time.pkl'
        clf_time = joblib.load(model)
        for time in times:
            temp.append(clf_time.predict([[s, time]])[0])
            results_time.append(temp)

    for r in results_time:
        plt.plot(times, r)
    # plt.plot(times, results_amount)
    plt.show()


if __name__ == '__main__':
    test()



