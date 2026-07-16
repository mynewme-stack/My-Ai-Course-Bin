import seaborn as sns
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

# file
dff = pd.read_csv('My Assignments Week 8\Datasets_Download\StudentsPerformance.csv')
df = pd.get_dummies(dff, columns=["gender","race/ethnicity","parental level of education","lunch","test preparation course"], drop_first= True)
print(df.columns)

# columns
X = df.drop(columns=['math score']).values
Y = df['math score'].values

# graph

column = ['reading score', 'writing score', 'gender_male', 'race/ethnicity_group B', 'race/ethnicity_group C', 'race/ethnicity_group D', 'race/ethnicity_group Ε', 'parental level of education_bachelor\'s degree', 'parental level of education_high school', 'parental level of education_master\'s degree', 'parental level of education_some college', 'parental level of education_some high school', 'lunch_standard']

for col in column:
    plt.figure()
    sns.scatterplot(data=df, x=col, y="math score").set(title=f'General plot of {col}');
    plt.show()

for col in column:
    plt.figure()
    sns.histplot(data=df, x=col, y="math score").set(title=f'Regression plot of {col}');
    plt.show()

for col in column:
    plt.figure()
    sns.regplot(data=df, x=col, y="math score").set(title=f'Regression plot of {col}');
    plt.show()

for col in column:
    plt.figure()
    sns.lineplot(data=df, x=col, y="math score").set(title=f'Regression plot of {col}');
    plt.show()



