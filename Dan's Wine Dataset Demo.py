from sklearn.datasets import load_wine
import pandas as pd
wine   = load_wine()
X_wine = wine.data
y_wine = wine.target
X_wine

df_wine = pd.DataFrame(data=wine.data, columns=wine.feature_names)
df_wine
df_wine.describe()

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
wine_scaled = scaler.fit_transform(df_wine)
wine_scaled

from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
clf_wine = LogisticRegression(max_iter=1000)

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

scores = cross_val_score(clf_wine, wine_scaled, y_wine, cv=cv, scoring="accuracy")
print("CrossVAL Accuracy Scores:", scores)
print("Mean Accuracy: ", scores.mean())
