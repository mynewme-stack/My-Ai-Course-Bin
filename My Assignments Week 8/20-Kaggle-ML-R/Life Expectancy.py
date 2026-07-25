import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd

# file
dff = pd.read_csv('My Assignments Week 8/Datasets_Download/Life Expectancy Data.csv')

# data cleaning process
print(f"\nMissing : {dff.isnull().mean()*100}")

# - first miss val

df_clean = dff.dropna(subset=['Life expectancy','Schooling','Income composition of resources','Polio','thinness  1-19 years','thinness 5-9 years','BMI', 'Diphtheria']).copy()

# - sec median

df_clean['Population'] = df_clean['Population'].fillna(df_clean['Population'].median())
df_clean['GDP'] = df_clean['GDP'].fillna(df_clean['GDP'].median())
df_clean['Total expenditure'] = df_clean['Total expenditure'].fillna(df_clean['Total expenditure'].median())
df_clean['Hepatitis B'] = df_clean['Hepatitis B'].fillna(df_clean['Hepatitis B'].median())
df_clean['Alcohol'] = df_clean['Alcohol'].fillna(df_clean['Alcohol'].median())

# checking 

print(f"\nMissing now: {df_clean.isnull().mean()*100}")

# - thrd ecoding

df = pd.get_dummies(df_clean,columns=['Country', 'Status'], drop_first=True)

# kfold

from sklearn.model_selection import KFold
kf = KFold(n_splits=5, shuffle= True, random_state= 30)

# graph

print(df.columns)

column = ['Year', 'Adult Mortality', 'infant deaths' ,'Alcohol', 'percentage expenditure', 'Hepatitis B', 'Measles', 'under-five deaths', 'BMI','Country_United Arab Emirates', 'Status_Developing']

# x and y

X = df.drop(columns=['Life expectancy']).values
Y = df['Life expectancy'].values
 
'''
for col in column:
    plt.figure()
    sns.lineplot(data=df, x=col, y="Life expectancy").set(title=f'line plot of {col}');
    plt.show()

for col in column:
    plt.figure()
    sns.regplot(data=df, x=col, y='Life expectancy').set(title=f'regplot plot of {col}');
    plt.show()
'''

# models 

from sklearn.linear_model import Lasso

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

# naming

l = Lasso()
dtr = DecisionTreeRegressor()
rfr = RandomForestRegressor()
xgbr = XGBRegressor()

# train test
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size= 0.9, random_state=30)

# scale
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

x_train_s = scale.fit_transform(x_train)
x_test_s = scale.transform(x_test)

# fit

l.fit(x_train_s,y_train)
dtr.fit(x_train,y_train)
rfr.fit(x_train,y_train)
xgbr.fit(x_train,y_train)

# pre

l_pre = l.predict(x_test_s)
dtr_pre = dtr.predict(x_test)
rfr_pre = rfr.predict(x_test)
xgbr_pre = xgbr.predict(x_test)

# cross val
from sklearn.model_selection import cross_val_score

# pipeline
from sklearn.pipeline import make_pipeline

l_p = make_pipeline(StandardScaler(), Lasso())

# cvs

l_cvs = cross_val_score(l_p,X,Y,cv= kf)
dtr_cvs = cross_val_score(DecisionTreeRegressor(), X,Y, cv= kf)
rfr_cvs = cross_val_score(RandomForestRegressor(), X,Y,cv=kf)
xgbr_cvs = cross_val_score(XGBRegressor(), X,Y,cv=kf)

# result print

cvss = [l_cvs,dtr_cvs,rfr_cvs,xgbr_cvs]
cvs_n = ['l_cvs','dtr_cvs','rfr_cvs','xgbr_cvs']

j = 0

for i in cvss:
    print(f'{cvs_n[j]} : {i}')
    j +=1


# result mean

cvss = [l_cvs,dtr_cvs,rfr_cvs,xgbr_cvs]
cvs_n = ['l_cvs','dtr_cvs','rfr_cvs','xgbr_cvs']

j = 0

for i in cvss:
    print(f'{cvs_n[j]} : {i.mean()}%')
    j +=1

# result

comparison = pd.DataFrame({
    'Actual': list(y_test),
    'L_Predicted': list(l_pre),
    'DTR_Predicted': list(dtr_pre),
    'RFR_Predict': list(rfr_pre),
    'XGBR_Predict': list(xgbr_pre)
})

comparison.to_csv('My Assignments Week 8/Results/Life expectancy_result.csv', index=False)
print(comparison)