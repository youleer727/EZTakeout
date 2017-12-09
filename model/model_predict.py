from sklearn import linear_model
from sklearn.externals import joblib
clf = joblib.load('model.pkl')
print clf.predict([[0, 1, 3.16]])