from sklearn.datasets import load_boston
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

data = load_boston()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target)

clf = LinearRegression()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(f"R^2 score: {r2_score(y_test, y_pred)}")

with open("classifier.pkl", "wb") as f:
    pickle.dump(clf, f)
