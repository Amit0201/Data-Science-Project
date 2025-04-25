#EXPLORATORY DATA ANALYTICS---> DIAGRAMS, PLOTS, HISTOGRAMS, SURVIVAL BY AGE, SURVIVAL BY GENDER AND CLASS

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Step 5: Exploratory Data Analysis
df = pd.read_csv('train.csv')
# Survival Count
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.show()

# Gender vs Survival
sns.countplot(x='Survived', hue='Sex', data=df)
plt.title("Survival by Gender")
plt.show()

# Pclass vs Survival
sns.countplot(x='Survived', hue='Pclass', data=df)
plt.title("Survival by Passenger Class")
plt.show()

# Age distribution
df['Age'].hist(bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
