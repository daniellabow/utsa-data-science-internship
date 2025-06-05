import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"
titanic_df = pd.read_csv(url)

titanic_cleaned = (
    titanic_df
    .drop(columns=["Cabin", "Name", "Ticket"]) #drop columns
    .dropna(subset=["Embarked"]) #drop rows w missing embarked
    .assign(
        Age=lambda df: df["Age"].fillna(df["Age"].median()), #fill missing ages w age avg
        Sex=lambda df: df["Sex"].map({"male": 0, "female": 1}), #convert sex to nums
        Embarked=lambda df: df["Embarked"].astype("category").cat.codes #encode 'embarked'
    )
    [["Survived", "Pclass", "Sex", "Age", "Fare", "Embarked"]] #keep useful columns
)

X = titanic_cleaned.drop("Survived", axis=1)
y = titanic_cleaned["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model accuracy:", round(accuracy, 4))
