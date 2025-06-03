import numpy as np
import pandas as pd
import os

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"
titanic_df = pd.read_csv(url)


for dirname, _, filenames in os.walk(url):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# infile =open(url)
# lines = infile.readlines()

# print(type(lines))
# print(lines)
# print(lines.split('\n'))
print(titanic_df.head())

titanic_df.info()
titanic_df.describe()
print(type(titanic_df))

titanic_df.tail()
ages = titanic_df["Age"]
ages.min()
columns = ["Age", "Sex"]
age_sex = titanic_df[columns]
#under_25 = titanic_df["Age"] < 25
people_1_2 = titanic_df["Pclass"].isin([1,2])
people_1_2
under_25 = titanic_df[(titanic_df["Pclass"] == 1) | (titanic_df["Pclass"] == 2) & (titanic_df["Age"] <25)]

titanic_clean_df = titanic_df
titanic_clean_df.isnull().sum()

titanic_clean_df.drop("Cabin", axis=1, inplace=True) #axis 0 is row and axis 1 is column

titanic_clean_df["Age"].describe()
titanic_clean_df["Age"] = titanic_clean_df["Age"].fillna(29.6)

columns = ["Age", "Sex"]
titanic_clean_df[columns]

titanic_clean_df_new = titanic_clean_df

print(titanic_clean_df_new)

cleaned_chain = (
titanic_clean_df_new.dropna(subset="Age")
    [["PassengerId", "Age", "Embarked", "Fare", "Pclass"]]
    .sort_values(by="Fare")
    )

print("Data after method chaining:\n", cleaned_chain)
print("DF WITHOUT AGE COLUMN!!!!!!!!!!!!")

print(titanic_clean_df_new)

def rename_pclass(df):
    mapping = {"First":1, "Second":2, "Third":3}
    df = df.copy
    return df


cleaned_pipeline = (
    #.pipe(rename_pclass)
    [["PassengerId", "Age", "Embarked", "Fare", "Pclass"]]
    #.sort_values(by="Fare")
)

print("Data after method chaining:\n", cleaned_pipeline)