import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold

# file
dfff = pd.read_csv('My Assignments Week 8/Datasets_Download/Automobile_data.csv')

# data has to be cleaned

dff = dfff.replace('?', np.nan)
print("\nAfter removing ?: ", dff.isnull().sum())

# missing perc

miss_per = dff.isnull().mean() * 100
print(miss_per[miss_per > 0])

#remove price rows

df_clean = dff.dropna(subset=['price']).copy()   # copy to prevent warn

# CLEANING  

drop_cols = ['bore', 'stroke', 'num-of-doors', 'horsepower', 'peak-rpm']
df_clean = df_clean.dropna(subset=drop_cols)

# encoding 

cols = ['normalized-losses', 'bore', 'stroke', 'horsepower', 'peak-rpm', 'price']

df_clean[cols] = df_clean[cols].apply(pd.to_numeric)          # python treat it as object so converted in num

# FILLING WITH MEDIAN

df_clean['normalized-losses'] = df_clean['normalized-losses'].fillna(df_clean['normalized-losses'].median())

df_final = pd.get_dummies(df_clean, columns=['make','fuel-type','aspiration','num-of-doors','body-style','drive-wheels','engine-location','engine-type','num-of-cylinders','fuel-system'], drop_first= True)  


# shuffle

kf = KFold(n_splits= 5, shuffle= True, random_state= 10)

# graph

column = df_final.columns

print(df_final.columns)


for col in column:
    plt.figure()
    sns.scatterplot(data=df_final, x=col, y="price").set(title=f'General plot of {col}');
    plt.show()

for col in column:
    plt.figure()
    sns.histplot(data=df_final, x=col, y='price').set(title=f'hisplot plot of {col}');
    plt.show()

for col in column:
    plt.figure()
    sns.regplot(data=df_final, x=col, y='price').set(title=f'Regression plot of {col}');
    plt.show()

for col in column:
    plt.figure()
    sns.lineplot(data=df_final, x=col, y='price').set(title=f'line plot of {col}');
    plt.show()

# scale
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

# x,y

X = df_final.drop(columns=['price']).values
Y = df_final['price'].values

# models

from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

# names

l = Lasso()
en = ElasticNet()
rfr = RandomForestRegressor()
svr = SVR(kernel='linear', C=1000)

# train test

from sklearn.model_selection import train_test_split
x_train_ns, x_test_ns, y_train, y_test = train_test_split(X,Y, train_size= 0.9, random_state=10)

# apply scale

x_train = scale.fit_transform(x_train_ns)
x_test = scale.transform(x_test_ns)

# fit

l.fit(x_train,y_train)
en.fit(x_train,y_train)
rfr.fit(x_train_ns,y_train)
svr.fit(x_train,y_train)

# pred

l_pre = l.predict(x_test)
en_pre = en.predict(x_test)
rfr_pre = rfr.predict(x_test_ns)
svr_pre = svr.predict(x_test)

# making pipline prevent data leak

from sklearn.pipeline import make_pipeline

l_pipe = make_pipeline(StandardScaler(), Lasso())
en_pipe = make_pipeline(StandardScaler(), ElasticNet())
svr_pipe = make_pipeline(StandardScaler(), SVR(kernel='linear', C=1000))

# cross val

from sklearn.model_selection import cross_val_score

l_cvs = cross_val_score(l_pipe, X,Y, cv=kf )
en_cvs = cross_val_score(en_pipe, X,Y, cv=kf )
rfr_cvs = cross_val_score(RandomForestRegressor(), X,Y, cv=kf )
svr_cvs = cross_val_score(svr_pipe,X,Y, cv=kf )

# print

cvss = [l_cvs,en_cvs,rfr_cvs,svr_cvs]
cvs_name = ['L R^2','EN R^2','RFR R^2','SVR R^2']
j= 0
for i in cvss:
    print(f"{cvs_name[j]} : {i}")
    j += 1

# mean print

cvss = [l_cvs,en_cvs,rfr_cvs,svr_cvs]
cvs_name = ['L R^2','EN R^2','RFR R^2','SVR R^2']
j = 0
for i in cvss:
    print(f"{cvs_name[j]} : {i.mean()}")
    j += 1

# Result
comparison = pd.DataFrame({
    'Actual': y_test,
    'L_Predicted':l_pre,
    'EN_Predicted': en_pre,
    'RFR_Predict':rfr_pre,
    'SVR_Predict': svr_pre})
comparison.to_csv('My Assignments Week 8/Results/automobile price_result.csv')
print(comparison) 