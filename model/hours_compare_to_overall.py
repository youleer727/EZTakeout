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
start_hour = 0


def convertMonth(month):
    if month < 10:
        return '0' + str(month)
    return str(month)


def load_all_months_models():
    for i in range(len(years)):
        time_model = str(years[i]) + '-' + convertMonth(months[i]) + '.time.pkl'
        amount_model = str(years[i]) + '-' + convertMonth(months[i]) + '.amount.pkl'
        yield joblib.load(time_model)
        yield joblib.load(amount_model)


def load_overall_model():
    yield joblib.load('trip_distance.linear_regression_model.time.pkl')
    yield joblib.load('trip_distance.linear_regression_model.amount.pkl')


def compare_all_months_to_overall_cost():
    clf_overall_time, clf_overall_amount = load_overall_model()
    amounts = []
    hours = []
    for val in range(200):
        amounts.append(val)
    results_amount_0 = []
    results_amount_1 = []
    results_amount_2 = []
    results_amount_3 = []
    results_amount_4 = []
    results_amount_5 = []
    results_amount_6 = []
    results_amount_7 = []
    results_amount_8 = []
    results_amount_9 = []
    results_amount_10 = []
    results_amount_11 = []
    results_amount_12 = []
    results_amount_13 = []
    results_amount_14 = []
    results_amount_15 = []
    results_amount_16 = []
    results_amount_17 = []
    results_amount_18 = []
    results_amount_19 = []
    results_amount_20 = []
    results_amount_21 = []
    results_amount_22 = []
    results_amount_23 = []
    for amount in amounts:
        results_amount_0.append(clf_overall_amount.predict([[0, amount]])[0])
        results_amount_1.append(clf_overall_amount.predict([[1, amount]])[0])
        results_amount_2.append(clf_overall_amount.predict([[2, amount]])[0])
        results_amount_3.append(clf_overall_amount.predict([[3, amount]])[0])
        results_amount_4.append(clf_overall_amount.predict([[4, amount]])[0])
        results_amount_5.append(clf_overall_amount.predict([[5, amount]])[0])
        results_amount_6.append(clf_overall_amount.predict([[6, amount]])[0])
        results_amount_7.append(clf_overall_amount.predict([[7, amount]])[0])
        results_amount_8.append(clf_overall_amount.predict([[8, amount]])[0])
        results_amount_9.append(clf_overall_amount.predict([[9, amount]])[0])
        results_amount_10.append(clf_overall_amount.predict([[10, amount]])[0])
        results_amount_11.append(clf_overall_amount.predict([[11, amount]])[0])
        results_amount_12.append(clf_overall_amount.predict([[12, amount]])[0])
        results_amount_13.append(clf_overall_amount.predict([[13, amount]])[0])
        results_amount_14.append(clf_overall_amount.predict([[14, amount]])[0])
        results_amount_15.append(clf_overall_amount.predict([[15, amount]])[0])
        results_amount_16.append(clf_overall_amount.predict([[16, amount]])[0])
        results_amount_17.append(clf_overall_amount.predict([[17, amount]])[0])
        results_amount_18.append(clf_overall_amount.predict([[18, amount]])[0])
        results_amount_19.append(clf_overall_amount.predict([[19, amount]])[0])
        results_amount_20.append(clf_overall_amount.predict([[20, amount]])[0])
        results_amount_21.append(clf_overall_amount.predict([[21, amount]])[0])
        results_amount_22.append(clf_overall_amount.predict([[22, amount]])[0])
        results_amount_23.append(clf_overall_amount.predict([[23, amount]])[0])
    plt.xlabel('cost ($USD)')
    plt.ylabel('overall predicted distance (miles)')
    plt.title('Distance predicted by trip cost')
    p1 = plt.plot(amounts, results_amount_0, label='hours = 0')
    p2 = plt.plot(amounts, results_amount_1, label='hours = 1')
    p3 = plt.plot(amounts, results_amount_2, label='hours = 2')
    p4 = plt.plot(amounts, results_amount_3, label='hours = 3')
    p4 = plt.plot(amounts, results_amount_4, label='hours = 4')
    p6 = plt.plot(amounts, results_amount_5, label='hours = 5')
    p7 = plt.plot(amounts, results_amount_6, label='hours = 6')
    p8 = plt.plot(amounts, results_amount_7, label='hours = 7')
    p9 = plt.plot(amounts, results_amount_8, label='hours = 8')
    p10 = plt.plot(amounts, results_amount_9, label='hours = 9')
    p11 = plt.plot(amounts, results_amount_10, label='hours = 10')
    p12 = plt.plot(amounts, results_amount_11, label='hours = 11')
    p12 = plt.plot(amounts, results_amount_12, label='hours = 12')
    p12 = plt.plot(amounts, results_amount_13, label='hours = 13')
    p12 = plt.plot(amounts, results_amount_14, label='hours = 14')
    p12 = plt.plot(amounts, results_amount_15, label='hours = 15')
    p12 = plt.plot(amounts, results_amount_16, label='hours = 16')
    p12 = plt.plot(amounts, results_amount_17, label='hours = 17')
    p12 = plt.plot(amounts, results_amount_18, label='hours = 18')
    p12 = plt.plot(amounts, results_amount_19, label='hours = 19')
    p12 = plt.plot(amounts, results_amount_20, label='hours = 20')
    p12 = plt.plot(amounts, results_amount_21, label='hours = 21')
    p12 = plt.plot(amounts, results_amount_22, label='hours = 22')
    p12 = plt.plot(amounts, results_amount_23, label='hours = 23')
    # p13 = plt.plot(amounts, results_cost_overall, label = 'Overall', color='black', lw=3)
    plt.legend(loc=2, prop={'size': 6})
    plt.savefig('distance-cost-predict_by_overall_with_hours.png', format='png', dpi=1200)
    plt.show()


def compare_all_months_to_overall_time():
    clf_overall_time, clf_overall_amount = load_overall_model()
    times = []
    hours = []
    for val in range(1000):
        times.append(val)
    results_time_0 = []
    results_time_1 = []
    results_time_2 = []
    results_time_3 = []
    results_time_4 = []
    results_time_5 = []
    results_time_6 = []
    results_time_7 = []
    results_time_8 = []
    results_time_9 = []
    results_time_10 = []
    results_time_11 = []
    results_time_12 = []
    results_time_13 = []
    results_time_14 = []
    results_time_15 = []
    results_time_16 = []
    results_time_17 = []
    results_time_18 = []
    results_time_19 = []
    results_time_20 = []
    results_time_21 = []
    results_time_22 = []
    results_time_23 = []
    for time in times:
        results_time_0.append(clf_overall_time.predict([[0, time]])[0])
        results_time_1.append(clf_overall_time.predict([[1, time]])[0])
        results_time_2.append(clf_overall_time.predict([[2, time]])[0])
        results_time_3.append(clf_overall_time.predict([[3, time]])[0])
        results_time_4.append(clf_overall_time.predict([[4, time]])[0])
        results_time_5.append(clf_overall_time.predict([[5, time]])[0])
        results_time_6.append(clf_overall_time.predict([[6, time]])[0])
        results_time_7.append(clf_overall_time.predict([[7, time]])[0])
        results_time_8.append(clf_overall_time.predict([[8, time]])[0])
        results_time_9.append(clf_overall_time.predict([[9, time]])[0])
        results_time_10.append(clf_overall_time.predict([[10, time]])[0])
        results_time_11.append(clf_overall_time.predict([[11, time]])[0])
        results_time_12.append(clf_overall_time.predict([[12, time]])[0])
        results_time_13.append(clf_overall_time.predict([[13, time]])[0])
        results_time_14.append(clf_overall_time.predict([[14, time]])[0])
        results_time_15.append(clf_overall_time.predict([[15, time]])[0])
        results_time_16.append(clf_overall_time.predict([[16, time]])[0])
        results_time_17.append(clf_overall_time.predict([[17, time]])[0])
        results_time_18.append(clf_overall_time.predict([[18, time]])[0])
        results_time_19.append(clf_overall_time.predict([[19, time]])[0])
        results_time_20.append(clf_overall_time.predict([[20, time]])[0])
        results_time_21.append(clf_overall_time.predict([[21, time]])[0])
        results_time_22.append(clf_overall_time.predict([[22, time]])[0])
        results_time_23.append(clf_overall_time.predict([[23, time]])[0])
    plt.xlabel('time spent (min)')
    plt.ylabel('overall predicted distance (miles)')
    plt.title('Distance predicted by trip time')
    p1 = plt.plot(times, results_time_0, label='hours = 0')
    p2 = plt.plot(times, results_time_1, label='hours = 1')
    p3 = plt.plot(times, results_time_2, label='hours = 2')
    p4 = plt.plot(times, results_time_3, label='hours = 3')
    p4 = plt.plot(times, results_time_4, label='hours = 4')
    p6 = plt.plot(times, results_time_5, label='hours = 5')
    p7 = plt.plot(times, results_time_6, label='hours = 6')
    p8 = plt.plot(times, results_time_7, label='hours = 7')
    p9 = plt.plot(times, results_time_8, label='hours = 8')
    p10 = plt.plot(times, results_time_9, label='hours = 9')
    p11 = plt.plot(times, results_time_10, label='hours = 10')
    p12 = plt.plot(times, results_time_11, label='hours = 11')
    p12 = plt.plot(times, results_time_12, label='hours = 12')
    p12 = plt.plot(times, results_time_13, label='hours = 13')
    p12 = plt.plot(times, results_time_14, label='hours = 14')
    p12 = plt.plot(times, results_time_15, label='hours = 15')
    p12 = plt.plot(times, results_time_16, label='hours = 16')
    p12 = plt.plot(times, results_time_17, label='hours = 17')
    p12 = plt.plot(times, results_time_18, label='hours = 18')
    p12 = plt.plot(times, results_time_19, label='hours = 19')
    p12 = plt.plot(times, results_time_20, label='hours = 20')
    p12 = plt.plot(times, results_time_21, label='hours = 21')
    p12 = plt.plot(times, results_time_22, label='hours = 22')
    p12 = plt.plot(times, results_time_23, label='hours = 23')
    # p13 = plt.plot(times, results_cost_overall, label = 'Overall', color='black', lw=3)
    plt.legend(loc=2, prop={'size': 6})
    plt.savefig('distance-time-predict_by_overall_with_hours.png', format='png', dpi=1200)
    plt.show()


if __name__ == '__main__':
    # compare_all_months_to_overall_cost()
    compare_all_months_to_overall_time()