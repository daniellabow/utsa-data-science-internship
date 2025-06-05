from tkinter import _test
import numpy as np
from numpy._core.defchararray import center
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
iris = pd.read_csv(url, header=None)

# Add headers manually
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'target']

#0=setosa, 1=versicolor, 2=virginica

x_class = iris.drop(columns="target")
outputs = plt.clf.predict(_test)

#from sklearn.metrics import accuracy_score
performance = accuracy_score(y_test, outputs)
print(f"Accuracy: {performance*100:.2f}%")

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples = 256, centers = 3, cluster_std = 1.0, random_state= 42)
kmeans = KMeans(n_clusters= 3, random_state= 42)
kmeans.fit(X)

import matplotlib.pyplot as plt
plt.figure(figsize=(4,4))
plt.scatter(X[:,0], X[:,1], label="random blob points")
plt.scatter(center[:,0], center[:,1], label="centroids")
plt.title("K-Means Clustering Results")
plt.xlabel("weight (lb)")
plt.ylabel("height (cm)")
plt.legend()

#sklearn-env\Scripts\activate in terminal to activate virtual environment
