import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import KFold

# filepath
dff = pd.read_csv('My Assignments Week 8/Datasets_Download/housing.csv')
print("Missing values before:", dff.isnull().sum())           # checks whether values missing 

# remove missing 
df_clean = dff.dropna(subset=['total_bedrooms'])
df = pd.get_dummies(df_clean, columns= ['ocean_proximity'],drop_first= True)

print("\nMissing values after:", df.isnull().sum())

# also shuffle

kf = KFold(n_splits=5,shuffle=True, random_state=10) 

# scale
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# graphs to analyze data
column = ['longitude','latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','ocean_proximity']
 

for col in column:
    plt.figure()
    sns.scatterplot(data=dff, x=col, y="median_house_value").set(title=f'General plot of {col}');
    plt.show()

for col in column:
    plt.figure()
    sns.histplot(data=dff, x=col, y='median_house_value').set(title=f'hisplot plot of {col}');
    plt.show()

# data is not linear still i want to try 1 linear model

from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import HistGradientBoostingRegressor

# naming

l = Lasso()
dtr = DecisionTreeRegressor()
rfr = RandomForestRegressor()
hgbr = HistGradientBoostingRegressor(max_iter=500)

# x AND Y

X = df.drop(columns=['median_house_value']).values
Y = df['median_house_value'].values

# train 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,Y, train_size=0.9)

# scale

x_train_s = scaler.fit_transform(x_train) 
x_test_s = scaler.transform(x_test)

# fit
l.fit(x_train_s,y_train)
dtr.fit(x_train,y_train)
rfr.fit(x_train,y_train)
hgbr.fit(x_train,y_train)

#pred

l_pred = l.predict(x_test_s)
dtr_pred = dtr.predict(x_test)
rfr_pred = rfr.predict(x_test)
hgbr_pred = hgbr.predict(x_test)

# cross val
x_scale = scaler.fit_transform(X)   # for only cvs

from sklearn.model_selection import cross_val_score

l_cvs = cross_val_score(Lasso(), x_scale,Y, cv= kf)
dtr_cvs = cross_val_score(DecisionTreeRegressor(), X, Y, cv= kf)
rfr_cvs = cross_val_score(RandomForestRegressor(), X,Y, cv= kf)
hgbr_cvs = cross_val_score(HistGradientBoostingRegressor(max_iter=500), X, Y, cv= kf)

# result
print("L R^2 : ", l_cvs)
print("DTR R^2 : ", dtr_cvs)
print("RFR R^2 : ", rfr_cvs)
print("HGBR R^2 : ", hgbr_cvs)

# mean
print("L R^2 MEAN : ", l_cvs.mean())
print("DTR R^2 MEAN : ", dtr_cvs.mean())
print("RFR R^2 MEAN : ", rfr_cvs.mean())
print("HGBR R^2 MEAN : ", hgbr_cvs.mean())

# Result
comparison = pd.DataFrame({
    'Actual': y_test,
    'L_Predicted':l_pred,
    'DTR_Predicted': dtr_pred,
    'RFR_Predict':rfr_pred,
    'HGBR_Predict': hgbr_pred})
comparison.to_csv('My Assignments Week 8/Results/California Housing Prices_result.csv')
print(comparison) 