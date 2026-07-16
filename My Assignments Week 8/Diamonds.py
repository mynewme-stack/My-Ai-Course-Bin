import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold

# file

dff = pd.read_csv('My Assignments Week 8\Datasets_Download\diamonds.csv')
df = pd.get_dummies(dff, columns=["cut","color","clarity"], drop_first=True)
df.drop(df.columns[0], axis=1, inplace=True)
print(df.columns)

# specify
X = df.drop(columns=['price']).values
Y = df['price'].values

# shufffle

kf = KFold(n_splits=5, shuffle=True, random_state=10)

# graphs
column = ['carat', 'depth', 'table', 'x', 'y', 'z', 'cut_Premium', 'color_E', 'clarity_IF']

'''
for col in column:
    plt.figure()
    sns.scatterplot(data=df, x=col, y="price").set(title=f'General plot of {col}');
    plt.show()

for col in column:
    plt.figure()
    sns.histplot(data=df, x=col, y="price").set(title=f'Regression plot of {col}');
    plt.show()

for col in column:
    plt.figure()
    sns.regplot(data=df, x=col, y="price").set(title=f'Regression plot of {col}');
    plt.show()

for col in column:
    plt.figure()
    sns.lineplot(data=df, x=col, y="price").set(title=f'Regression plot of {col}');
    plt.show()
'''

# standardsclaer
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()

x_scale = ss.fit_transform(X)

# 1st model (just trying)
from sklearn.linear_model import LinearRegression
lr = LinearRegression()

# Train test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_scale,Y, random_state= 10)

# train and predict

lr.fit(x_train,y_train)
lr_score_y = lr.predict(x_test)

# cross val score
from sklearn.model_selection import cross_val_score

lr_score = cross_val_score(LinearRegression(),x_scale,Y, cv= kf)
print('LR Accuracy: ',lr_score)
print('LR Accuracy mean: ',lr_score.mean())

# the real model we should apply as the data has so many curves

from sklearn.ensemble import RandomForestRegressor

# save time
rfr = RandomForestRegressor(n_estimators=100, max_features='sqrt', random_state=10)

x_train, x_test, y_train, y_test = train_test_split(x_scale,Y, random_state= 10)

rfr.fit(x_train,y_train)
rfr_score_y = rfr.predict(x_test)

# cross val score

rfr_score = cross_val_score(RandomForestRegressor(),x_scale,Y, cv= kf)
print('RFR Accuracy: ',rfr_score)
print('RFR Accuracy mean: ',rfr_score.mean())

# making csv
comparison = pd.DataFrame({
    'Actual': y_test,
    'LR_Predicted':rfr_score_y,
    'RFR_Predicted':lr_score_y})
comparison.to_csv('My Assignments Week 8/Results/Diamonds_result.csv')
print(comparison)
