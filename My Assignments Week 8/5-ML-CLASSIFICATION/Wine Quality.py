''' Trying another methosd to download datset
from datasets import load_dataset
dataset = load_dataset('codesignal/wine-quality')

import pandas as pd
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt

# making dataframes
red_df = pd.DataFrame(dataset['red'])
white_df = pd.DataFrame(dataset['white'])

# gives both specified values
red_df['wine_type'] = 'red'
white_df['wine_type'] = 'white'

# Make both one 
df = pd.concat([red_df, white_df], ignore_index=True)
# turn it into csv
df.to_csv('wine_quality_all.csv', index=False) '''

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

df = pd.read_csv('My Assignments Week 8/Datasets_Download/wine_quality_all.csv')
df_use = pd.get_dummies(df, columns=['wine_type'], drop_first=True)

# graphs to study

print(df_use.columns)

column = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'wine_type']

# General
for col in column:
    plt.figure()
    sns.scatterplot(data=df_use, x=col, y='quality').set(title=f'General plot of {col}');
    plt.show()

# classification
for col in column:
    plt.figure()
    sns.histplot(data=df_use, x=col, y='quality').set(title=f'Regression plot of {col}');
    plt.show()

# classifying data

X= df_use.drop(columns=['quality']).values
Y= df_use['quality'].values

# TRYING FIRST ALGORITHM
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()

# scale
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# train
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,Y,train_size=0.9,random_state= 10)

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

lr.fit(x_train,y_train)

result_lr =lr.predict(x_test)

# result

from sklearn.metrics import classification_report
print(classification_report(y_test, result_lr))

# cross validation

from sklearn.model_selection import cross_val_score

# scale whole x
X_scaled = scaler.fit_transform(X)

lr_score = cross_val_score(LogisticRegression(max_iter=1000), X_scaled, Y, cv=10, scoring='accuracy')
print('Accuracy LR: ',lr_score)
print('Mean Accuracy LR: ', lr_score.mean())

# second model
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(random_state=10)

rfc.fit(x_train,y_train)

result_rfc = rfc.predict(x_test)

# we are shuffling so for better testing

print(classification_report(y_test, result_rfc))

from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=10)

rfc_score = cross_val_score(RandomForestClassifier(random_state=10), X_scaled, Y, cv=skf, scoring='accuracy')

print('Accuracy RFC (Shuffled): ', rfc_score)
print('Mean Accuracy RFC: ', rfc_score.mean())

# trying a new aalgorithm

import xgboost as xgb

# convert in binary so less pressure
Y_binary = (df_use['quality'] >= 7).astype(int)

x_train,x_test, y_train,y_test = train_test_split(X,Y_binary, train_size=0.9,random_state=15)

xgb_model = xgb.XGBClassifier(random_state=10)
xgb_model.fit(x_train, y_train)

xgb_result = xgb_model.predict(x_test)

# cross val score

xgb_score = cross_val_score(xgb_model, X_scaled, Y_binary, cv=10, scoring='accuracy')
print('Accuracy XGB: ',xgb_score)
print('Mean Accuracy XGB: ', xgb_score.mean())

# result csv
comparison = pd.DataFrame({
    'Actual': y_test,
    'LR_Predicted':result_lr,
    'RFC_Predicted': result_rfc,
    'XGB_Predict':xgb_result})
comparison.to_csv('My Assignments Week 8/Results/Wine Quality_result.csv')
print(comparison)