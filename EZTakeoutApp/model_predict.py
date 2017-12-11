from sklearn import linear_model
from sklearn.externals import joblib
clf = joblib.load('trip_distance.linear_regression_model.pkl')
print clf.predict([[0, 1, 15, 10]])[0]