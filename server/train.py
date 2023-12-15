from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from joblib import dump

data = load_iris()

X = data.data
y = data.target

clf = LogisticRegression(random_state=0, max_iter=1000).fit(X, y)

dump(clf, 'model.joblib') 