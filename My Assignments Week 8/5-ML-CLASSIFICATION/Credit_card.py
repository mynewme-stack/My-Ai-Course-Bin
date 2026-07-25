import seaborn as sns 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.model_selection import KFold

# path

app_dff = pd.read_csv('My Assignments Week 8/Datasets_Download/application_record.csv')
cre_dff = pd.read_csv('My Assignments Week 8/Datasets_Download/credit_record.csv')

# making target

cre_dff['is_delinquent'] = cre_dff['STATUS'].isin(['2', '3', '4', '5']).astype(int)

user = cre_dff.groupby('ID')['is_delinquent'].max().reset_index()

user['approval_status'] = user['is_delinquent'].apply(lambda x: 0 if x == 1 else 1)

target_df = user[['ID', 'approval_status']]

app_dff = app_dff.drop_duplicates(subset='ID', keep='first')
final_df = pd.merge(app_dff, target_df, on='ID', how='inner')

print(final_df['approval_status'].value_counts())

# overveiw

app_dff.shape
app_dff.info()
app_dff.describe()
app_dff.head()

cre_dff.shape
cre_dff.info()
cre_dff.describe()
cre_dff.head()

# miss

print("\nMiss Vals: ", cre_dff.isnull().sum())
print("\nMiss Vals: ", app_dff.isnull().sum())

# fil

final_df['OCCUPATION_TYPE'] = final_df['OCCUPATION_TYPE'].fillna('Unknown')

print("\nMiss Vals: ", final_df.isnull().sum()) #check

# dupli

app_dff = app_dff.drop_duplicates(subset='ID', keep='first')
# dupli

app_dff = app_dff.drop_duplicates(subset='ID', keep='first')

final_df['UNEMPLOYED'] = (final_df['DAYS_EMPLOYED'] == 365243).astype(int)
final_df['DAYS_EMPLOYED'] = final_df['DAYS_EMPLOYED'].replace(365243, 0)

final_df['AGE'] = abs(final_df['DAYS_BIRTH']) / 365.25
final_df['YEARS_EMPLOYED'] = abs(final_df['DAYS_EMPLOYED']) / 365.25

final_df = final_df.drop(columns=['DAYS_BIRTH', 'DAYS_EMPLOYED'])
print(final_df[['AGE', 'YEARS_EMPLOYED', 'UNEMPLOYED']].head())

# encod

df = pd.get_dummies(final_df, columns=[
    'CODE_GENDER', 
    'FLAG_OWN_CAR', 
    'FLAG_OWN_REALTY', 
    'NAME_INCOME_TYPE', 
    'NAME_EDUCATION_TYPE', 
    'NAME_FAMILY_STATUS', 
    'NAME_HOUSING_TYPE', 
    'OCCUPATION_TYPE'], drop_first=True)

# kf

from sklearn.model_selection import KFold
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# x and y

X = df.drop(columns=['ID','approval_status']).values
Y = df['approval_status'].values

# graph

column= ['']

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

lr_cvs = cross_val_score(lr_pipe, X,Y ,cv= kf)
dtc_cvs = cross_val_score(DecisionTreeClassifier(), X,Y ,cv= kf)
rfc_cvs = cross_val_score(RandomForestClassifier(), X,Y ,cv= kf)
xgbc_cvs = cross_val_score(XGBClassifier(), X,Y ,cv= kf)
knc_cvs = cross_val_score(knc_pipe, X,Y ,cv= kf)


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
comparison.to_csv('My Assignments Week 8/Results/Telco_Customer_result.csv', index=False)
print(comparison)
