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
start_hour = 6


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
    clf_2016_6_time, clf_2016_6_amount, clf_2016_7_time,  \
    clf_2016_7_amount, clf_2016_9_time, clf_2016_9_amount,  \
    clf_2016_10_time, clf_2016_10_amount,clf_2016_11_time,  \
    clf_2016_11_amount, clf_2016_12_time, clf_2016_12_amount, \
    clf_2017_1_time, clf_2017_1_amount, clf_2017_2_time, \
    clf_2017_2_amount, clf_2017_3_time, clf_2017_3_amount, \
    clf_2017_4_time, clf_2017_4_amount, clf_2017_5_time, \
    clf_2017_5_amount, clf_2017_6_time, clf_2017_6_amount = load_all_months_models()
    clf_overall_time, clf_overall_amount = load_overall_model()
    amounts = []
    for val in range(200):
        amounts.append(val)
    results_amount_2016_6 = []
    results_amount_2016_7 = []
    results_amount_2016_9 = []
    results_amount_2016_10 = []
    results_amount_2016_11 = []
    results_amount_2016_12 = []
    results_amount_2017_1 = []
    results_amount_2017_2 = []
    results_amount_2017_3 = []
    results_amount_2017_4 = []
    results_amount_2017_5 = []
    results_amount_2017_6 = []
    results_cost_overall = []
    for val in amounts:
        results_amount_2016_6.append(clf_2016_6_amount.predict([[start_hour, val]])[0])
        results_amount_2016_7.append(clf_2016_7_amount.predict([[start_hour, val]])[0])
        results_amount_2016_9.append(clf_2016_9_amount.predict([[start_hour, val]])[0])
        results_amount_2016_10.append(clf_2016_10_amount.predict([[start_hour, val]])[0])
        results_amount_2016_11.append(clf_2016_11_amount.predict([[start_hour, val]])[0])
        results_amount_2016_12.append(clf_2016_12_amount.predict([[start_hour, val]])[0])
        results_amount_2017_1.append(clf_2017_1_amount.predict([[start_hour, val]])[0])
        results_amount_2017_2.append(clf_2017_2_amount.predict([[start_hour, val]])[0])
        results_amount_2017_3.append(clf_2017_3_amount.predict([[start_hour, val]])[0])
        results_amount_2017_4.append(clf_2017_4_amount.predict([[start_hour, val]])[0])
        results_amount_2017_5.append(clf_2017_5_amount.predict([[start_hour, val]])[0])
        results_amount_2017_6.append(clf_2017_6_amount.predict([[start_hour, val]])[0])
        results_cost_overall.append(clf_overall_amount.predict([[start_hour, val]])[0])
    plt.xlabel('cost ($USD)')
    plt.ylabel('predicted distance (miles)')
    plt.title('Distance predicted by trip cost')
    p1 = plt.plot(amounts, results_amount_2016_6, label='Jun 2016')
    p2 = plt.plot(amounts, results_amount_2016_7, label='Jul 2016')
    p3 = plt.plot(amounts, results_amount_2016_9, label='Sep 2016')
    p4 = plt.plot(amounts, results_amount_2016_10, label='Oct 2016')
    p4 = plt.plot(amounts, results_amount_2016_11, label='Nov 2016')
    p6 = plt.plot(amounts, results_amount_2016_12, label='Dec 2016')
    p7 = plt.plot(amounts, results_amount_2017_1, label='Jan 2017')
    p8 = plt.plot(amounts, results_amount_2017_2, label='Feb 2017')
    p9 = plt.plot(amounts, results_amount_2017_3, label='Mar 2017')
    p10 = plt.plot(amounts, results_amount_2017_4, label='Apr 2017')
    p11 = plt.plot(amounts, results_amount_2017_5, label='May 2017')
    p12 = plt.plot(amounts, results_amount_2017_6, label='Jun 2017')
    p13 = plt.plot(amounts, results_cost_overall, label = 'Overall', color='black', lw=3)
    plt.legend(loc=2, prop={'size': 6})
    plt.savefig('distance-cost-predict_by_months_overall.png', format='png', dpi=1200)
    plt.show()



    
def compare_all_months_to_overall_time():
    clf_2016_6_time, clf_2016_6_amount, clf_2016_7_time,  \
    clf_2016_7_amount, clf_2016_9_time, clf_2016_9_amount,  \
    clf_2016_10_time, clf_2016_10_amount,clf_2016_11_time,  \
    clf_2016_11_amount, clf_2016_12_time, clf_2016_12_amount, \
    clf_2017_1_time, clf_2017_1_amount, clf_2017_2_time, \
    clf_2017_2_amount, clf_2017_3_time, clf_2017_3_amount, \
    clf_2017_4_time, clf_2017_4_amount, clf_2017_5_time, \
    clf_2017_5_amount, clf_2017_6_time, clf_2017_6_amount = load_all_months_models()
    clf_overall_time, clf_overall_amount = load_overall_model()
    times = []
    for val in range(1000):
        times.append(val)
    results_time_2016_6 = []
    results_time_2016_7 = []
    results_time_2016_9 = []
    results_time_2016_10 = []
    results_time_2016_11 = []
    results_time_2016_12 = []
    results_time_2017_1 = []
    results_time_2017_2 = []
    results_time_2017_3 = []
    results_time_2017_4 = []
    results_time_2017_5 = []
    results_time_2017_6 = []
    results_time_overall = []
    for val in times:
        results_time_2016_6.append(clf_2016_6_time.predict([[start_hour, val]])[0])
        results_time_2016_7.append(clf_2016_7_time.predict([[start_hour, val]])[0])
        results_time_2016_9.append(clf_2016_9_time.predict([[start_hour, val]])[0])
        results_time_2016_10.append(clf_2016_10_time.predict([[start_hour, val]])[0])
        results_time_2016_11.append(clf_2016_11_time.predict([[start_hour, val]])[0])
        results_time_2016_12.append(clf_2016_12_time.predict([[start_hour, val]])[0])
        results_time_2017_1.append(clf_2017_1_time.predict([[start_hour, val]])[0])
        results_time_2017_2.append(clf_2017_2_time.predict([[start_hour, val]])[0])
        results_time_2017_3.append(clf_2017_3_time.predict([[start_hour, val]])[0])
        results_time_2017_4.append(clf_2017_4_time.predict([[start_hour, val]])[0])
        results_time_2017_5.append(clf_2017_5_time.predict([[start_hour, val]])[0])
        results_time_2017_6.append(clf_2017_6_time.predict([[start_hour, val]])[0])
        results_time_overall.append(clf_overall_time.predict([[start_hour, val]])[0])
    plt.xlabel('time (min)')
    plt.ylabel('predicted distance (miles)')
    plt.title('Distance predicted by times(Overall model v.s. month model)')
    p1 = plt.plot(times, results_time_2016_6, label='Jun 2016')
    p2 = plt.plot(times, results_time_2016_7, label='Jul 2016')
    p3 = plt.plot(times, results_time_2016_9, label='Sep 2016')
    p4 = plt.plot(times, results_time_2016_10, label='Oct 2016')
    p4 = plt.plot(times, results_time_2016_11, label='Nov 2016')
    p6 = plt.plot(times, results_time_2016_12, label='Dec 2016')
    p7 = plt.plot(times, results_time_2017_1, label='Jan 2017')
    p8 = plt.plot(times, results_time_2017_2, label='Feb 2017')
    p9 = plt.plot(times, results_time_2017_3, label='Mar 2017')
    p10 = plt.plot(times, results_time_2017_4, label='Apr 2017')
    p11 = plt.plot(times, results_time_2017_5, label='May 2017')
    p12 = plt.plot(times, results_time_2017_6, label='Jun 2017')
    p13 = plt.plot(times, results_time_overall, label = 'Overall', color='black', lw=3)
    plt.legend(loc=2, prop={'size': 6})
    plt.savefig('distance-time-predict_by_months_overall.png', format='png', dpi=1200)
    plt.show()

def all_months_predict_amount():
    clf_2016_6_time, clf_2016_6_amount, clf_2016_7_time,  \
    clf_2016_7_amount, clf_2016_9_time, clf_2016_9_amount,  \
    clf_2016_10_time, clf_2016_10_amount,clf_2016_11_time,  \
    clf_2016_11_amount, clf_2016_12_time, clf_2016_12_amount, \
    clf_2017_1_time, clf_2017_1_amount, clf_2017_2_time, \
    clf_2017_2_amount, clf_2017_3_time, clf_2017_3_amount, \
    clf_2017_4_time, clf_2017_4_amount, clf_2017_5_time, \
    clf_2017_5_amount, clf_2017_6_time, clf_2017_6_amount = load_all_months_models()
    amounts = []
    for val in range(200):
        amounts.append(val)
    results_amount_2016_6 = []
    results_amount_2016_7 = []
    results_amount_2016_9 = []
    results_amount_2016_10 = []
    results_amount_2016_11 = []
    results_amount_2016_12 = []
    results_amount_2017_1 = []
    results_amount_2017_2 = []
    results_amount_2017_3 = []
    results_amount_2017_4 = []
    results_amount_2017_5 = []
    results_amount_2017_6 = []
    for val in amounts:
        results_amount_2016_6.append(clf_2016_6_amount.predict([[start_hour, val]])[0])
        results_amount_2016_7.append(clf_2016_7_amount.predict([[start_hour, val]])[0])
        results_amount_2016_9.append(clf_2016_9_amount.predict([[start_hour, val]])[0])
        results_amount_2016_10.append(clf_2016_10_amount.predict([[start_hour, val]])[0])
        results_amount_2016_11.append(clf_2016_11_amount.predict([[start_hour, val]])[0])
        results_amount_2016_12.append(clf_2016_12_amount.predict([[start_hour, val]])[0])
        results_amount_2017_1.append(clf_2017_1_amount.predict([[start_hour, val]])[0])
        results_amount_2017_2.append(clf_2017_2_amount.predict([[start_hour, val]])[0])
        results_amount_2017_3.append(clf_2017_3_amount.predict([[start_hour, val]])[0])
        results_amount_2017_4.append(clf_2017_4_amount.predict([[start_hour, val]])[0])
        results_amount_2017_5.append(clf_2017_5_amount.predict([[start_hour, val]])[0])
        results_amount_2017_6.append(clf_2017_6_amount.predict([[start_hour, val]])[0])
    plt.xlabel('cost ($USD)')
    plt.ylabel('predicted distance (miles)')
    plt.title('Distance predicted by trip cost')
    p1 = plt.plot(amounts, results_amount_2016_6, label='Jun 2016')
    p2 = plt.plot(amounts, results_amount_2016_7, label='Jul 2016')
    p3 = plt.plot(amounts, results_amount_2016_9, label='Sep 2016')
    p4 = plt.plot(amounts, results_amount_2016_10, label='Oct 2016')
    p4 = plt.plot(amounts, results_amount_2016_11, label='Nov 2016')
    p6 = plt.plot(amounts, results_amount_2016_12, label='Dec 2016')
    p7 = plt.plot(amounts, results_amount_2017_1, label='Jan 2017')
    p8 = plt.plot(amounts, results_amount_2017_2, label='Feb 2017')
    p9 = plt.plot(amounts, results_amount_2017_3, label='Mar 2017')
    p10 = plt.plot(amounts, results_amount_2017_4, label='Apr 2017')
    p11 = plt.plot(amounts, results_amount_2017_5, label='May 2017')
    p12 = plt.plot(amounts, results_amount_2017_6, label='Jun 2017')
    plt.legend(loc=2, prop={'size': 6})
    plt.savefig('distance-cost-predict_by_months.png', format='png', dpi=1200)
    plt.show()
    
def all_months_predict_time():
    clf_2016_6_time, clf_2016_6_amount, clf_2016_7_time,  \
    clf_2016_7_amount, clf_2016_9_time, clf_2016_9_amount,  \
    clf_2016_10_time, clf_2016_10_amount,clf_2016_11_time,  \
    clf_2016_11_amount, clf_2016_12_time, clf_2016_12_amount, \
    clf_2017_1_time, clf_2017_1_amount, clf_2017_2_time, \
    clf_2017_2_amount, clf_2017_3_time, clf_2017_3_amount, \
    clf_2017_4_time, clf_2017_4_amount, clf_2017_5_time, \
    clf_2017_5_amount, clf_2017_6_time, clf_2017_6_amount = load_all_months_models()
    times = []
    for val in range(1000):
        times.append(val)
    results_time_2016_6 = []
    results_time_2016_7 = []
    results_time_2016_9 = []
    results_time_2016_10 = []
    results_time_2016_11 = []
    results_time_2016_12 = []
    results_time_2017_1 = []
    results_time_2017_2 = []
    results_time_2017_3 = []
    results_time_2017_4 = []
    results_time_2017_5 = []
    results_time_2017_6 = []
    for val in times:
        results_time_2016_6.append(clf_2016_6_time.predict([[start_hour, val]])[0])
        results_time_2016_7.append(clf_2016_7_time.predict([[start_hour, val]])[0])
        results_time_2016_9.append(clf_2016_9_time.predict([[start_hour, val]])[0])
        results_time_2016_10.append(clf_2016_10_time.predict([[start_hour, val]])[0])
        results_time_2016_11.append(clf_2016_11_time.predict([[start_hour, val]])[0])
        results_time_2016_12.append(clf_2016_12_time.predict([[start_hour, val]])[0])
        results_time_2017_1.append(clf_2017_1_time.predict([[start_hour, val]])[0])
        results_time_2017_2.append(clf_2017_2_time.predict([[start_hour, val]])[0])
        results_time_2017_3.append(clf_2017_3_time.predict([[start_hour, val]])[0])
        results_time_2017_4.append(clf_2017_4_time.predict([[start_hour, val]])[0])
        results_time_2017_5.append(clf_2017_5_time.predict([[start_hour, val]])[0])
        results_time_2017_6.append(clf_2017_6_time.predict([[start_hour, val]])[0])
    plt.xlabel('time (min)')
    plt.ylabel('predicted distance (miles)')
    plt.title('Distance predicted by times')
    p1 = plt.plot(times, results_time_2016_6, label='Jun 2016')
    p2 = plt.plot(times, results_time_2016_7, label='Jul 2016')
    p3 = plt.plot(times, results_time_2016_9, label='Sep 2016')
    p4 = plt.plot(times, results_time_2016_10, label='Oct 2016')
    p4 = plt.plot(times, results_time_2016_11, label='Nov 2016')
    p6 = plt.plot(times, results_time_2016_12, label='Dec 2016')
    p7 = plt.plot(times, results_time_2017_1, label='Jan 2017')
    p8 = plt.plot(times, results_time_2017_2, label='Feb 2017')
    p9 = plt.plot(times, results_time_2017_3, label='Mar 2017')
    p10 = plt.plot(times, results_time_2017_4, label='Apr 2017')
    p11 = plt.plot(times, results_time_2017_5, label='May 2017')
    p12 = plt.plot(times, results_time_2017_6, label='Jun 2017')
    plt.legend(loc=2, prop={'size': 6})
    plt.savefig('distance-time-predict_by_months.png', format='png', dpi=1200)
    plt.show()
    # plt.gcf().clear()





# print clf.predict([[trip_distance, passenger_count, total_amount, time_spent]])[0]




def test():
    clf_time, clf_amount = load_overall_model()
    times = []
    for val in range(100):
        times.append(val)
    passenger_count = 1
    results_time = []
    results_amount = []
    #
    for var in times:
        results_time.append(clf_time.predict([[start_hour, var]])[0])
        results_amount.append(clf_amount.predict([[start_hour, var]])[0])
    # plt.plot(times, results_time)
    # plt.plot(times, results_amount, c='firebrick')
    # plt.show()
    # # for distance in distances:
    # #     for amount in amounts:
    # #         print 'distance is ' + str(distance)
    # #         print 'amount is ' + str(amount)
    # #         results.append(clf.predict([[start_hour , passenger_count, amount, distance]])[0])
    # # print distances
    # # print amounts
    # # print results
    # plt.plot(times, results_time)
    # # plt.plot(times, results_amount)
    # plt.xlabel('time')
    # plt.show()

    path = "./datasets/processed/tripdata_reduced"
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

    # plt.scatter(time, distance, s=1)
    plt.scatter(amount, distance, s=1)
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
    # all_months_predict_time()
    # compare_all_months_to_overall_time()
    # all_months_predict_amount()
    # compare_all_months_to_overall_cost()


