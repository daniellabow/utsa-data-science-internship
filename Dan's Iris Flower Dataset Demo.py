from tkinter import _test
import numpy as np
from numpy._core.defchararray import center
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from sklearn.datasets import load_iris

iris = load_iris()
df_iris = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df_iris

df_iris["target"] = iris.target
df_iris  #0=setosa, 1=versicolor, 2=virginica
X_class = df_iris.drop(columns="target")
y_class = df_iris['target']

#first: create data splits
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test   = train_test_split(X_class, y_class, test_size=.2)
#X_train, X_valid, y_valid, y_valid = train_test_split(X_train, y_train, test_size=.1)

#second: train the model on some input data
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

#third: test/eval the model
outputs = clf.predict(X_test)
outputs

performance = accuracy_score(y_test, outputs)
print(f"Accuracy: {performance*100:.2f}%")

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

#generate some data
X, _ = make_blobs(n_samples=256, centers=3, cluster_std=1.0, random_state=42)

#train the model
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

y_kmeans = kmeans.predict(X)
y_kmeans

centers = kmeans.cluster_centers_

import matplotlib.pyplot as plt

plt.figure(figsize=(4,4))
plt.scatter(X[:, 0], X[:, 1], label="random blob points")  #input data
plt.scatter(centers[:, 0], centers[:, 1], label="centroids")

plt.title("K-Means Clustering Results")
plt.xlabel("weight (lb)")
plt.ylabel("height (cm)")
plt.legend()

#sklearn-env\Scripts\activate in terminal to activate virtual environment
