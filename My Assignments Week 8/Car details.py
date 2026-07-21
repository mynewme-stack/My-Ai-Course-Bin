import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold

# file path
dff = pd.read_csv('My Assignments Week 8\Datasets_Download\Car details v3.csv')

df_clean = dff.copy()

# prepare csv for ml algor
df_clean['brand'] = df_clean['name'].str.split().str[0]

df_clean = df_clean.drop(columns=['name','torque']) # complexity

# astype float

df_clean['mileage'] = df_clean['mileage'].str.extract(r'(\d+\.?\d*)').astype(float)

df_clean['engine'] = df_clean['engine'].str.extract(r'(\d+\.?\d*)').astype(float)

df_clean['max_power'] = df_clean['max_power'].str.extract(r'(\d+\.?\d*)').astype(float)

# missin values
print(f"\nMissing : {df_clean.isnull().mean()*100}")

# dropna

df_clean = df_clean.dropna(subset=['mileage','engine','max_power','seats'])

df = pd.get_dummies(df_clean, columns=['fuel','seller_type','transmission','owner', 'brand'], drop_first= True)

# kf fold
kf = KFold(n_splits=5, shuffle= True, random_state= 30)

# graphs

print(df.columns)

column = ['year', 'selling_price', 'km_driven', 'mileage', 'engine', 'max_power', 'seats', 'fuel_Diesel', 'seller_type_Trustmark Dealer', 'transmission_Manual', 'owner_Fourth & Above Owner', 'brand_Ashok']
'''
for col in column:
    plt.figure()
    sns.lineplot(data=df, x=col, y="selling_price").set(title=f'line plot of {col}');
    plt.show()

for col in column:
    plt.figure()
    sns.regplot(data=df, x=col, y='selling_price').set(title=f'regplot plot of {col}');
    plt.show()

'''

# linear models
from sklearn.linear_model import Ridge

# tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

# naming 
r = Ridge()
dtr = DecisionTreeRegressor()
rfr = RandomForestRegressor()
xgbr = XGBRegressor()

# x,y

X = df.drop(columns=['selling_price']).values
Y = df['selling_price'].values

# train test
from sklearn.model_selection import train_test_split
x_train_ns, x_test_ns, y_train, y_test  = train_test_split(X,Y, train_size= 0.9, random_state= 30)

# standard scale 
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

x_train = scale.fit_transform(x_train_ns)
x_test = scale.transform(x_test_ns)

# fit

r.fit(x_train,y_train)
dtr.fit(x_train_ns,y_train)
rfr.fit(x_train_ns,y_train)
xgbr.fit(x_train_ns,y_train)

# pred

r_pre = r.predict(x_test)
dtr_pre = dtr.predict(x_test_ns)
rfr_pre = rfr.predict(x_test_ns)
xgbr_pre = xgbr.predict(x_test_ns)

# cross
from sklearn.model_selection import cross_val_score

# pipeline
from sklearn.pipeline import make_pipeline

r_p = make_pipeline(StandardScaler(),Ridge())

# cvs

r_cvs = cross_val_score(r_p, X,Y,cv=kf)
dtr_cvs = cross_val_score(DecisionTreeRegressor(), X,Y,cv=kf)
rfr_cvs = cross_val_score(RandomForestRegressor(), X,Y,cv=kf)
xgbr_cvs = cross_val_score(XGBRegressor(), X,Y,cv=kf)

# result print

cvss = [r_cvs,dtr_cvs,rfr_cvs,xgbr_cvs]
cvss_n = ["r_cvs",'dtr_cvs',"rfr_cvs",'xgbr_cvs']
j = 0

for i in cvss:
    print(f'{cvss_n[j]} : {i}')
    j += 1

# mean  result print

cvss = [r_cvs,dtr_cvs,rfr_cvs,xgbr_cvs]
cvss_n = ["r_cvs",'dtr_cvs',"rfr_cvs",'xgbr_cvs']
j = 0

for i in cvss:
    print(f'{cvss_n[j]} : {i.mean()}')
    j += 1

# result
comparison = pd.DataFrame({
    'Actual': y_test,
    'R_Predicted':r_pre,
    'DTR_Predicted': dtr_pre,
    'RFR_Predict':rfr_pre,
    'XGBR_Predict': xgbr_pre})
comparison.to_csv('My Assignments Week 8/Results/Car details v3_result.csv')
print(comparison) 

