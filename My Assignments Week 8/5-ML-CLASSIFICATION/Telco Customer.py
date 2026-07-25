import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold

# file

df_p = pd.read_csv('My Assignments Week 8/Datasets_Download/WA_Fn-UseC_-Telco-Customer-Churn.csv')

# overview

df_p.shape
df_p.info()
df_p.describe()
df_p.head()

# check if totalcharge is str 
# print(df_p['TotalCharges'].mean())

# clean

df_p = df_p.drop(columns=['customerID'])

df_p['TotalCharges'] = pd.to_numeric(df_p['TotalCharges'], errors='coerce')
df_p['TotalCharges'] = df_p['TotalCharges'].fillna(0)

print(df_p['TotalCharges'].mean())    # again if str

dupl = df_p.duplicated().sum()
print(f"Number of dupli rows: {dupl}")
if dupl > 0:
    df_p = df_p.drop_duplicates()

# miss

print("\nMiss Vals: ", df_p.isnull().sum())

df_p['Churn'] = df_p['Churn'].map({'Yes': 1, 'No': 0})
df = pd.get_dummies(df_p, columns=['gender','Partner','Dependents','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod'], drop_first=True)

# kf

kf = KFold(n_splits=5, shuffle=True, random_state=30)

# visualization

column =  ['gender','SeniorCitizen','Partner','Dependents','tenure','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod','MonthlyCharges','TotalCharges','Churn']

'''
for i in column: 
    plt.figure()
    sns.scatterplot(data=df_p, x = i, y = 'Churn', hue='tenure')
    plt.show()

for i in column: 
    sns.set_theme(style='darkgrid')
    sns.barplot(data=df_p, x = i, y = 'Churn')
    plt.xticks(rotation=90)
    plt.show()

for i in column: 
    sns.set_theme(style='darkgrid')
    sns.boxplot(data=df_p, x = i, y = 'Churn')
    plt.xticks(rotation=90)
    plt.show()
'''
# X and Y

X = df.drop(columns=['Churn']).values
Y = df['Churn'].values

# train test

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X,Y , train_size=0.85, random_state=30)

# scale 

from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

x_train_s = scale.fit_transform(x_train)
x_test_s = scale.transform(x_test)

# algor

from sklearn.linear_model import LogisticRegression
from sklearn.tree import  DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from sklearn.metrics import classification_report

# grid search

from sklearn.model_selection import GridSearchCV

# Parameter
param_grid = {
    'C': [0.1, 1, 10, 100],
    'gamma': [0.001, 0.01, 0.1, 1],
    'kernel': ['rbf']
}

# name 

lr = LogisticRegression(class_weight='balanced')
dtc = DecisionTreeClassifier(class_weight='balanced')
rfc = RandomForestClassifier(class_weight='balanced')
xgbc = XGBClassifier(scale_pos_weight=2.7)
knc = KNeighborsClassifier()
svc = SVC(class_weight='balanced')
grid = GridSearchCV(SVC(class_weight='balanced'), param_grid, cv=kf, scoring='f1')

# fit

lr.fit(x_train_s, y_train)
dtc.fit(x_train, y_train)
rfc.fit(x_train, y_train)
xgbc.fit(x_train, y_train)
knc.fit(x_train_s,y_train)
svc.fit(x_train_s, y_train)
grid.fit(x_train_s, y_train)

# predi

lr_pre = lr.predict(x_test_s)
dtc_pre = dtc.predict(x_test)
rfc_pre = rfc.predict(x_test)
xgbc_pre = xgbc.predict(x_test)
knc_pre = knc.predict(x_test_s)
svc_pre = svc.predict(x_test_s)

# pipe

from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline

# pipeline

lr_pipe = make_pipeline(StandardScaler(), LogisticRegression())
knc_pipe = make_pipeline(StandardScaler(), KNeighborsClassifier())
svc_pipe = make_pipeline(StandardScaler(), SVC())

# cvs

lr_cvs = cross_val_score(lr_pipe, X,Y ,cv= kf)
dtc_cvs = cross_val_score(DecisionTreeClassifier(), X,Y ,cv= kf)
rfc_cvs = cross_val_score(RandomForestClassifier(), X,Y ,cv= kf)
xgbc_cvs = cross_val_score(XGBClassifier(), X,Y ,cv= kf)
knc_cvs = cross_val_score(knc_pipe, X,Y ,cv= kf)
svc_cvs = cross_val_score(svc_pipe, X,Y ,cv= kf)

# result 

cvss = [lr_cvs,dtc_cvs,rfc_cvs,xgbc_cvs,knc_cvs,svc_cvs]
cvs_name = ['lr_cvs','dtc_cvs','rfc_cvs','xgbc_cvs','knc_cvs','svc_cvs']

j= 0

for i in cvss:
    print(f"{cvs_name[j]} : {i}")
    j += 1

# result mean

cvss = [lr_cvs,dtc_cvs,rfc_cvs,xgbc_cvs,knc_cvs,svc_cvs]
cvs_name = ['lr_cvs','dtc_cvs','rfc_cvs','xgbc_cvs','knc_cvs','svc_cvs']

j= 0

for i in cvss:
    print(f"{cvs_name[j]} mean : {i.mean()}")
    j += 1

# seprate

print("\nparameters for SVC:", grid.best_params_)
best_svc_pre = grid.best_estimator_.predict(x_test_s)

print("\nTuned SVC :")
print(classification_report(y_test, best_svc_pre))

# repot

print(classification_report(y_test, lr_pre))
print(classification_report(y_test, dtc_pre))
print(classification_report(y_test, rfc_pre))
print(classification_report(y_test, xgbc_pre))
print(classification_report(y_test, knc_pre))
print(classification_report(y_test, svc_pre))

# result csv

comparison = pd.DataFrame({
    'Actual': y_test,
    'LR_Predicted':lr_pre,
    'DTC_Predicted':dtc_pre,
    'RFC_Predicted': rfc_pre,
    'XGBC_Predicted': xgbc_pre,
    'KNC_Predicted':knc_pre,
    'SVC_Predict':svc_pre})
comparison.to_csv('My Assignments Week 8/Results/Telco_Customer_result.csv', index=False)
print(comparison)
