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

column = ['reading score', 'writing score', 'gender_male', 'race/ethnicity_group B', 'parental level of education_bachelor\'s degree','lunch_standard']
'''
for col in column:
    plt.figure()
    sns.scatterplot(data=df, x=col, y="math score").set(title=f'General plot of {col}');
    plt.show()

for col in column:
    plt.figure()
    sns.histplot(data=df, x=col, y="math score").set(title=f'Hist plot of {col}');
    plt.show()

for col in column:
    plt.figure()
    sns.regplot(data=df, x=col, y="math score").set(title=f'Regplot of {col}');
    plt.show()

for col in column:
    plt.figure()
    sns.lineplot(data=df, x=col, y="math score").set(title=f'lineplot of {col}');
    plt.show()
'''
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

x_scale = scaler.fit_transform(X)

# models 
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor

lr = LinearRegression()
l = Lasso()
rfr = RandomForestRegressor(max_depth=5, min_samples_leaf=5, random_state=42)       

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x_scale,Y, train_size=0.9 ,random_state=15, shuffle= True)

# training
lr.fit(x_train,y_train)
l.fit(x_train,y_train)
rfr.fit(x_train,y_train)

# testing
lr_score = lr.predict(x_test)
l_score = l.predict(x_test)
rfr_score = rfr.predict(x_test)

# cross_ val
from sklearn.model_selection import cross_val_score

lr_cvs = cross_val_score(LinearRegression(), x_scale, Y, cv= 15)
l_cvs = cross_val_score(Lasso(), x_scale, Y, cv= 15)
rfr_cvs = cross_val_score(RandomForestRegressor(), x_scale,Y, cv=15)

print('LR Accuracy: ', lr_cvs)
print('L Accuracy: ',l_cvs)
print('RFR Accuracy: ',rfr_cvs)

# mean
print('LR Accuracy Mean: ', lr_cvs.mean())
print('L Accuracy Mean: ',l_cvs.mean())
print('RFR Accuracy Mean: ',rfr_cvs.mean())

#Lr has the most accuracy so trying ridge reg

from sklearn.linear_model import Ridge
r= Ridge()

r.fit(x_train,y_train)

r_score = r.predict(x_test)

# crossval
r_cvs = cross_val_score(Ridge(), x_scale,Y, cv=15)

print('R Accuracy: ',r_cvs)
print('R Accuracy Mean: ', r_cvs.mean())

#result csv
comparison = pd.DataFrame({
    'Actual': y_test,
    'LR_Predicted':lr_score,
    'L_Predicted':l_score,
    'R_Predicted':r_score,
    'RFR_Predicted':rfr_score})
comparison.to_csv('My Assignments Week 8/Results/Student Performance_result.csv')
print(comparison)

