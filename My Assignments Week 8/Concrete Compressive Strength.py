import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from sklearn.model_selection import KFold

# file path

df = pd.read_csv('My Assignments Week 8/Datasets_Download/Concrete Compressive Strength.csv')

# specify target
 
X = df.drop(columns=['Concrete compressive strength ']).values
Y = df['Concrete compressive strength '].values

# standard scaler

from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

# kfold
kf = KFold(n_splits=5,shuffle=True, random_state=10) # we need shuffling as data has hidden patterns

# graph
column = ['Cement',"Blast Furnace Slag",'Fly Ash','Water','Superplasticizer','Coarse Aggregate','Fine Aggregate','Age (day)']

for col in column:
    plt.figure()
    sns.scatterplot(data=df, x=col, y="Concrete compressive strength ").set(title=f'General plot of {col}');
    plt.show()

for col in column:
    plt.figure()
    sns.histplot(data=df, x=col, y='Concrete compressive strength ').set(title=f'hisplot plot of {col}');
    plt.show()

for col in column:
    plt.figure()
    sns.regplot(data=df, x=col, y='Concrete compressive strength ').set(title=f'Regression plot of {col}');
    plt.show()

for col in column:
    plt.figure()
    sns.lineplot(data=df, x=col, y='Concrete compressive strength ').set(title=f'line plot of {col}');
    plt.show()


# First model
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor

# Fit in variable
r = Ridge()
l = Lasso()
rfr = RandomForestRegressor(n_jobs=-1)

# traintest
from sklearn.model_selection import train_test_split
x_train_ns,x_test_ns,y_train,y_test = train_test_split(X,Y,train_size=0.9,random_state=25)

# scaling data now to avoid any leakage
x_train = scale.fit_transform(x_train_ns)
x_test = scale.transform(x_test_ns)

# fitting 
r.fit(x_train,y_train)
l.fit(x_train,y_train)
rfr.fit(x_train,y_train)

# predict
r_test = r.predict(x_test)
l_test =  l.predict(x_test)
rfr_test = rfr.predict(x_test)

# crossvalscore
from sklearn.model_selection import cross_val_score

X_scaled_for_cv = scale.fit_transform(X)

r_cvs = cross_val_score(Ridge(), X_scaled_for_cv, Y, cv= kf) 
l_cvs = cross_val_score(Lasso(),X_scaled_for_cv,Y,cv= kf)
rfr_cvs = cross_val_score(RandomForestRegressor(),X,Y, cv= kf) # not for cvs

# resultcard
print(f"R R^2: {r_cvs}\n"
      f'L R^2: {l_cvs}\n'
      f'RFR R^2: {rfr_cvs}\n')

# result_mean
print('\n\tR R^2 Mean: ', r_cvs.mean())
print('\n\tL R^2 Mean: ',l_cvs.mean())
print('\n\tRFR R^2 Mean: ',rfr_cvs.mean())

# xgboost
import xgboost as xgb

xgb = xgb.XGBRegressor()
xgb.fit(x_train, y_train)
xgb_test = xgb.predict(x_test)
xgb_cvs = cross_val_score(xgb, X,Y, cv= kf)

print (f'XGB R^2: {xgb_cvs}')
print('\n\tXGB R^2 Mean: ',xgb_cvs.mean())

# result csv
comparison = pd.DataFrame({
    'Actual': y_test,
    'R_Predicted':r_test,
    'L_Predicted': l_test,
    'RFR_Predict':rfr_test,
    'XGB_Predict': xgb_test})
comparison.to_csv('My Assignments Week 8/Results/Concrete Compressive Strength_result.csv')
print(comparison)