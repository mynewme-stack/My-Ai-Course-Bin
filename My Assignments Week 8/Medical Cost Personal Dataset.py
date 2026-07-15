import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('My Assignments Week 8/Datasets_Download/insurance.csv')
df_use = pd.get_dummies(df, columns=['sex','smoker','region'], drop_first=True)

# check
print(df_use.columns)

# studying data

variables = ['age', 'bmi', 'children', 'sex_male','smoker_yes', 'region_northwest', 'region_southeast', 'region_southwest']
for var in variables:
    plt.figure() 
    sns.lineplot(x=var, y='charges', data=df_use).set(title=f'Regression plot of {var}');
    plt.show()

# data is so wide so i start by using rfr

from sklearn.ensemble import RandomForestRegressor
rfr = RandomForestRegressor(n_estimators=210,random_state=15)

X = df_use.drop(columns=['charges']).values
Y = df_use['charges'].values

from sklearn.model_selection import train_test_split

x_train, x_test, y_train , y_test = train_test_split(X,Y, test_size= 0.1, random_state=5)

# train
rfr.fit(x_train,y_train)

# test
result_1 = rfr.predict(x_test)

# rfr result
from  sklearn.model_selection import cross_val_score

rfr_score = cross_val_score(RandomForestRegressor(n_estimators=210,random_state=15),X,Y,cv=10, scoring='r2' )
print('RFR CV R^2: ',rfr_score)
print('RFR Average R^2: ',rfr_score.mean())

# trying somethig NEW

importances = pd.Series(rfr.feature_importances_, index=df_use.drop(columns=['charges']).columns).sort_values(ascending=False)
print(importances)

# trying another model
from sklearn.tree import DecisionTreeRegressor
dtr = DecisionTreeRegressor()

dtr.fit(x_train,y_train)

result_2 = dtr.predict(x_test)

# cross_val again

dtr_score = cross_val_score(DecisionTreeRegressor(random_state=15),X,Y,cv=10, scoring='r2' )
print('DTR CV R^2: ',dtr_score)
print('DTR Average R^2: ',dtr_score.mean())

# trying something else

from sklearn.ensemble import GradientBoostingRegressor
gbr = GradientBoostingRegressor(n_estimators=100,learning_rate=0.05,max_depth=3,random_state=15)

gbr.fit(x_train,y_train)

result_3 = gbr.predict(x_test)

# score

gbr_score = cross_val_score(GradientBoostingRegressor(n_estimators= 100,random_state=15),X,Y,cv=10, scoring='r2' )
print('GBR CV R^2: ',gbr_score)
print('GBR Average R^2: ',gbr_score.mean())

# result csv
comparison = pd.DataFrame({
    'Actual': y_test,
    'RFR_Predicted':result_1,
    'DTA_Predicted': result_2,
    'GBR_Predict':result_3})
comparison.to_csv('My Assignments Week 8/Results/Medical Cost Personal Dataset_result.csv')
print(comparison)