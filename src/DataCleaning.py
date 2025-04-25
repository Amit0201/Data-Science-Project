#Step 2 ---> DATA CLEANING

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#CHECKING FOR MISSING VALUES
df = pd.read_csv('train.csv')

#Statistical Summary
print(df.describe())
print(f"---------------------------------------------------------------------------------------------------------------")
#Checking for NULL VALUES in columns
print("\nMissing Values:\n", df.isnull().sum())
print(f"---------------------------------------------------------------------------------------------------------------")
#Filling the null values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
#Drop irrelevant or high-missing columns
df.drop(['Cabin'], axis=1, inplace=True)
print(f"---------------------------------------------------------------------------------------------------------------")
print("Missing values after cleaning:\n", df.isnull().sum)
