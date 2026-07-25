import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# files

df = pd.read_csv('My Assignments Week 8/Datasets_Download/Real_estate.csv')
df_new = df.drop(columns=['No'])

# Graphs 
plt.figure()
sns.regplot(data=df_new, x = 'X1 transaction date',
            y = 'Y house price of unit area')
plt.show()

plt.figure()
sns.regplot(data=df_new, x = 'X2 house age',
            y = 'Y house price of unit area')
plt.show()

plt.figure()
sns.regplot(data=df_new, x = 'X3 distance to the nearest MRT station',
            y = 'Y house price of unit area')
plt.show()

plt.figure()
sns.regplot(data=df_new, x = 'X4 number of convenience stores',
            y = 'Y house price of unit area')
plt.show()

plt.figure()
sns.regplot(data=df_new, x = 'X5 latitude',
            y = 'Y house price of unit area')
plt.show()

plt.figure()
sns.regplot(data=df_new, x = 'X6 longitude',
            y = 'Y house price of unit area')
plt.show()

# OVERALL

plt.figure()
sns.heatmap(df_new.corr(), annot=True)
plt.show()

# long and lat

plt.figure()
sns.scatterplot(data= df_new,x='X5 latitude',y='X6 longitude',hue='Y house price of unit area')
plt.show()

# scales

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# columns
X = df_new.drop(columns=['Y house price of unit area']).values
y = df_new['Y house price of unit area'].values

# separating train and test data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, train_size=0.9, random_state=20)

# algorithm

from sklearn.linear_model import LinearRegression
line = LinearRegression()

# scaling
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# train
line.fit(x_train,y_train)

# test
result1 = line.predict(x_test)

# 2nd algorithm
from sklearn.linear_model import Ridge
ridge = Ridge(alpha= 0.1)

# fit
ridge.fit(x_train,y_train)

# predict y
pred_y = ridge.predict(x_test)

# another moedl
from sklearn.linear_model import Lasso
lass = Lasso()
lass.fit(x_train,y_train)
pred = lass.predict(x_test)

# Basic result
linear = line.score(x_test, y_test) * 100
ridge_acc = ridge.score(x_test, y_test) * 100
lass_acc = lass.score(x_test, y_test) * 100

# print result
print(f"R^2: {linear}%")
print(f"R^2: {ridge_acc}%")
print(f"lass r2: {lass_acc}%")

# cross validation to make better result
from sklearn.model_selection import cross_val_score
scores = cross_val_score(LinearRegression(), X, y, cv=5, scoring='r2')
print("CV R² scores:", scores)
print("Average R²:", scores.mean())

# this result shows that random forest regresor is a better option for this data 
from sklearn.ensemble import RandomForestRegressor
rf_score = cross_val_score(RandomForestRegressor(n_estimators=200,random_state=20),X,y,cv=10, scoring='r2' )
print('RF CV R^2: ',rf_score)
print('RF Average R^2: ',rf_score.mean())

# applied this model
rfr = RandomForestRegressor()
rfr.fit(x_train,y_train)
y_by_rfr = rfr.predict(x_test)

# result
rfr_by_rfr_score = cross_val_score(RandomForestRegressor(n_estimators=210,random_state=15),X,y,cv=7, scoring='r2' )
print('RFR CV R^2: ',rfr_by_rfr_score)
print('RFR Average R^2: ',rfr_by_rfr_score.mean())

# result csv
comparison = pd.DataFrame({
    'Actual': y_test,
    'Linear_Predicted':result1,
    'Ridge_Predicted': pred_y,
    'Lass_Predict':pred,
    'RandomForestRegressor': y_by_rfr
})
comparison.to_csv('My Assignments Week 8/Results/Real Estate Valuation_result.csv')
print(comparison)