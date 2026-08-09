# This is my latest ml model implementation on dataset after learning from my past work

import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold

# path 

cre_df = pd.read_csv('My Assignments Week 8/Datasets_Download/credit_record.csv').copy()
app_df = pd.read_csv('My Assignments Week 8/Datasets_Download/application_record.csv').copy()

# miss

print('Miss val : ', cre_df.isnull().sum())
print('Miss val : ', app_df.isnull().sum())

# only occup has miss

app_df['OCCUPATION_TYPE'] = app_df['OCCUPATION_TYPE'].fillna('Unknown')
print('Miss val : ', app_df.isnull().sum())

# target clean

print("Check if col : ",cre_df['STATUS'].value_counts())     

mapp = {'C': 0, '0': 0, 'X': 0, '1': 1 , '5': 1 , '2':1 ,'3':1 , '4': 1}
cre_df['STATUS'] = cre_df['STATUS'].map(mapp).astype(int)

print(cre_df['STATUS'])

# dupli 

dupli_app = app_df.duplicated().sum()
dupli_app_id = app_df.duplicated(subset='ID').sum()
dupli_cre = cre_df.duplicated().sum()

print('app_df : ',dupli_app)
print('app_df_ids : ',dupli_app_id)
print('cre_df : ',dupli_cre)

# i got 47 duplicate ids

app_df = app_df.drop_duplicates(subset='ID',keep = 'first')
print('after remove dulpi app_df only ids : ',app_df.duplicated(subset='ID').sum())

# dirty dat

print(app_df['DAYS_EMPLOYED'].describe()) 

# days employ issue

app_df['UNEMPLOYED'] = (app_df['DAYS_EMPLOYED'] == 365243).astype(int)  

app_df['EMPLOYED'] = (app_df['DAYS_EMPLOYED']).replace(365243 , 0)      

# get dummies 

app_df = pd.get_dummies(app_df, columns= ['CODE_GENDER','FLAG_OWN_CAR','FLAG_OWN_REALTY'
                    ,'NAME_INCOME_TYPE','NAME_EDUCATION_TYPE','NAME_FAMILY_STATUS',
                    'NAME_HOUSING_TYPE','OCCUPATION_TYPE'], drop_first= True)

# solving id

cre_df_a = cre_df.groupby('ID')['STATUS'].max().reset_index()

# ONE DATASET

df = pd.merge(app_df,cre_df_a, on='ID', how= 'inner')

# kf

Kf = KFold(n_splits=5, shuffle=True, random_state= 10)

# x and y

df = df.set_index('ID')

X = df.drop(columns=['STATUS']).values
Y = df['STATUS'].values 

# graph

print(df.columns)

column= ['CNT_CHILDREN', 'AMT_INCOME_TOTAL', 'DAYS_BIRTH', 'DAYS_EMPLOYED', 'FLAG_MOBIL', 'FLAG_WORK_PHONE', 'FLAG_PHONE', 'FLAG_EMAIL', 'CNT_FAM_MEMBERS', 'UNEMPLOYED', 'EMPLOYED', 'CODE_GENDER_M', 'FLAG_OWN_CAR_Y', 'FLAG_OWN_REALTY_Y','NAME_INCOME_TYPE_Working', 'NAME_EDUCATION_TYPE_Higher education', 'NAME_FAMILY_STATUS_Married','NAME_HOUSING_TYPE_House / apartment','OCCUPATION_TYPE_Unknown']


for i in column: 
    plt.figure()
    sns.scatterplot(data=df, x = i, y = 'STATUS', hue='DAYS_EMPLOYED')
    plt.show()

for i in column: 
    sns.set_theme(style='darkgrid')
    sns.barplot(data=df, x = i, y = 'STATUS')
    plt.xticks(rotation=90)
    plt.show()

for i in column: 
    sns.set_theme(style='darkgrid')
    sns.boxplot(data=df, x = i, y = 'STATUS')
    plt.xticks(rotation=90)
    plt.show()


# train test

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X,Y , train_size=0.90, random_state=30)

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


from sklearn.metrics import classification_report

# name 

lr = LogisticRegression(class_weight='balanced')
dtc = DecisionTreeClassifier(class_weight='balanced')
rfc = RandomForestClassifier(class_weight='balanced')
xgbc = XGBClassifier(scale_pos_weight=2.7)
knc = KNeighborsClassifier()

# fit

lr.fit(x_train_s, y_train)
dtc.fit(x_train, y_train)
rfc.fit(x_train, y_train)
xgbc.fit(x_train, y_train)
knc.fit(x_train_s,y_train)


# predi

lr_pre = lr.predict(x_test_s)
dtc_pre = dtc.predict(x_test)
rfc_pre = rfc.predict(x_test)
xgbc_pre = xgbc.predict(x_test)
knc_pre = knc.predict(x_test_s)



# pipe

from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline

# pipeline

lr_pipe = make_pipeline(StandardScaler(), LogisticRegression())
knc_pipe = make_pipeline(StandardScaler(), KNeighborsClassifier())


# cvs

lr_cvs = cross_val_score(lr_pipe, X,Y ,cv= Kf)
dtc_cvs = cross_val_score(DecisionTreeClassifier(), X,Y ,cv= Kf)
rfc_cvs = cross_val_score(RandomForestClassifier(), X,Y ,cv= Kf)
xgbc_cvs = cross_val_score(XGBClassifier(), X,Y ,cv= Kf)
knc_cvs = cross_val_score(knc_pipe, X,Y ,cv= Kf)


# result 

cvss = [lr_cvs,dtc_cvs,rfc_cvs,xgbc_cvs,knc_cvs]
cvs_name = ['lr_cvs','dtc_cvs','rfc_cvs','xgbc_cvs','knc_cvs']

j= 0

for i in cvss:
    print(f"{cvs_name[j]} : {i}")
    j += 1

# result mean

cvss = [lr_cvs,dtc_cvs,rfc_cvs,xgbc_cvs,knc_cvs]
cvs_name = ['lr_cvs','dtc_cvs','rfc_cvs','xgbc_cvs','knc_cvs']

j= 0

for i in cvss:
    print(f"{cvs_name[j]} mean : {i.mean()}")
    j += 1

# repot

print(classification_report(y_test, lr_pre))
print(classification_report(y_test, dtc_pre))
print(classification_report(y_test, rfc_pre))
print(classification_report(y_test, xgbc_pre))
print(classification_report(y_test, knc_pre))

# result csv

comparison = pd.DataFrame({
    'Actual': y_test,
    'LR_Predicted':lr_pre,
    'DTC_Predicted':dtc_pre,
    'RFC_Predicted': rfc_pre,
    'XGBC_Predicted': xgbc_pre,
    'KNC_Predicted':knc_pre})
comparison.to_csv('My Assignments Week 8/Results/creditcard_result.csv', index=False)
print(comparison)
