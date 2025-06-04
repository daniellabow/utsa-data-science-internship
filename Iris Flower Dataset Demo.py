import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
iris = pd.read_csv(url, header=None)

# Add headers manually
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'target']

#0=setosa, 1=versicolor, 2=virginica

#x_class = iris.drop(columns="target")
#outputs = clf.predict(x_test)
#outputs

#accuracy_score = 
#from sklearn.metrics import accuracy_score
#performance = accuracy_score(y_test, outputs)
#print(f"Accuracy: {performance*100:.2f}%")