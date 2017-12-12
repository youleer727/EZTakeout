import sys
from sklearn import linear_model
from sklearn.externals import joblib
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import random

years = [2016, 2016, 2016, 2016, 2016, 2016, 2017, 2017, 2017, 2017, 2017, 2017]
months = [6, 7, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6]

# trip_distance = float(sys.argv[1])
# passenger_count = float(sys.argv[2])
# total_amount = float(sys.argv[3])
# time_spent = float(sys.argv[4])
clf = joblib.load('trip_distance.linear_regression_model.time.pkl')
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
    results = []
    for time in times:
        results.append(clf.predict([[start_hour, time]])[0])
    # for distance in distances:
    #     for amount in amounts:
    #         print 'distance is ' + str(distance)
    #         print 'amount is ' + str(amount)
    #         results.append(clf.predict([[start_hour , passenger_count, amount, distance]])[0])
    # print distances
    # print amounts
    # print results
    plt.plot(times, results)
    plt.show()


if __name__ == '__main__':
    test()



