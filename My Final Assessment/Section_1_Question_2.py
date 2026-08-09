import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# file

unc_df = pd.read_csv('My Final Assessment/Datasets_Used/UCI-Heart-Disease-Dataset/heart_disease_combined.csv')

# target

'''

MY TAGET IS WETHER THE PATIENT HAS HEART DIESEASE OR NOT?
For my this purpose, i used this heart_disease_combined dataset as it has more rows and more hospitals refrences
which make model to recognize pattern and perform well.

'''

# missing values

print('Missing values : ', unc_df.isnull().sum())

print("_____________________________________")

#--- percentage of missing values

print('Percentage of Missing values : ',unc_df.isnull().mean() * 100)

print("_____________________________________")

#--- drop columns

unc_df = unc_df.drop(columns=['thal','ca'])

#--- filling 

#-- zeros

zero_counts = (unc_df[['trestbps','chol']] == 0).sum()

print("Zero value Counts Per Column: ",zero_counts)

#--median

unc_df['trestbps'] = unc_df['trestbps'].replace(0,np.nan)
unc_df['chol'] = unc_df['chol'].replace(0,np.nan)

median_col = ['trestbps','chol','thalach','oldpeak']

for me in median_col: 
    unc_df[me]= unc_df[me].fillna(unc_df[me].median())

#--mode

mode_col = ['fbs','restecg','exang','slope']

for mo in mode_col:
    unc_df[mo]= unc_df[mo].fillna(unc_df[mo].mode()[0])

#-- check again 

print('Missing values : ', unc_df.isnull().sum())

print("_____________________________________")

# checking dulpicate

dupli_row = unc_df.duplicated().sum()

print('Duplicate rows : ', dupli_row)

print("_____________________________________")

#--- dropping dulpicates as they are only 2

unc_df = unc_df.drop_duplicates().reset_index(drop=True)

#-- check

print('Recheck Duplicate rows : ', unc_df.duplicated().sum())

print("_____________________________________")

# Overview

unc_df.info()
print('Shape: ',unc_df.shape)
print('Columns: ',unc_df.columns)
print('Statistics: ',unc_df.describe())
print('Summary: ',unc_df.describe(include='all'))

print("_____________________________________")

# columns

print(unc_df.columns)

#--- proof classification

column = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope']
col_n =  ['Age', 'Sex', 'Cp', 'Trestbps', 'Chol', 'Fbs', 'Restecg', 'Thalach', 'Exang', 'Oldpeak', 'Slope']

j=0


for i in column:
    sns.set_theme(style='whitegrid')
    sns.histplot(unc_df, x=i, hue='target',
                            palette=['pink','purple'])
    plt.xlabel(col_n[j])
    plt.ylabel('Target')
    plt.xticks(rotation= 90)
    plt.tight_layout()
    plt.show()
    j+=1

#--- again proof

j=0

for i in column:
    sns.set_theme(style='whitegrid')
    sns.stripplot(unc_df, x='target',y=i, hue='target',
                            palette=['darkcyan', 'tomato'])
    plt.xlabel(col_n[j])
    plt.ylabel('Target')
    plt.xticks(rotation= 90)
    plt.tight_layout()
    plt.show()
    j+=1


#----- data analysis

print(unc_df['target'].value_counts())

plt.pie(unc_df['target'].value_counts(), labels=[0,1], autopct='%1.1f%%',
        colors=['lightblue','royalblue'],
        wedgeprops={'linewidth': 0.2, 'edgecolor': 'grey'})

plt.title('Visual Analysis')
plt.tight_layout()
plt.show()


# encoding & feature engineering

'''
I asked some Medical students and they advised me to add this column and data to make model prectibility more 
better. 

'''

unc_df['oldpeak_slope'] = unc_df['oldpeak']*unc_df['slope']

'''
RESEARCH WORK:

If number is greater meaning maybe more risk of heart diesease.

'''

unc_df['hr_age_ratio'] = unc_df['thalach'] / unc_df['age'] 

'''
RESEARCH WORK:

If thalach / age == lower number may results in heartdisease and 
if higher it would may result in no heart diesease.

'''

unc_df['bp_chol_prod'] = unc_df['trestbps'] * unc_df['chol']

'''

RESEARCH WORK:

bp is blood pressure while chol is cholestrol. When bp is low and chol is also low than their multiplication will
show a lower risk that means patient have little chances of heart diesease and when bp is high and chol is high
it means the heart would have a little more risk chances of diesease.

'''

df = pd.get_dummies(unc_df, columns=['cp','restecg','slope'], drop_first=True)

print(df.columns)

# x and y 

X = df.drop(columns=['target','source'], errors='ignore').values
Y = df['target'].values

# kfold

from sklearn.model_selection import StratifiedKFold

sKf = StratifiedKFold(n_splits=5, random_state=30 ,shuffle=True)

# scaling

from sklearn.preprocessing import RobustScaler

scale = RobustScaler()

# train_test_split

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X,Y , train_size=0.83, random_state=20, stratify= Y)

# using scale

x_train_s = scale.fit_transform(x_train)
x_test_s = scale.transform(x_test)

# models


from sklearn.linear_model import LogisticRegression
from sklearn.tree import  DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from catboost import CatBoostClassifier

from sklearn.metrics import classification_report

# name 

lr = LogisticRegression(max_iter=1000,class_weight='balanced')
dtc = DecisionTreeClassifier(class_weight='balanced')
rfc = RandomForestClassifier(class_weight='balanced')
xgbc = XGBClassifier(eval_metric='logloss', random_state=42)
knc = KNeighborsClassifier()
svc = SVC(decision_function_shape='ovr', class_weight='balanced')
cbc = CatBoostClassifier()

# fit

lr.fit(x_train_s, y_train)
dtc.fit(x_train, y_train)
rfc.fit(x_train, y_train)
xgbc.fit(x_train, y_train)
knc.fit(x_train_s,y_train)
svc.fit(x_train_s, y_train)
cbc.fit(x_train,y_train)

# predict

lr_pre = lr.predict(x_test_s)
dtc_pre = dtc.predict(x_test)
rfc_pre = rfc.predict(x_test)
xgbc_pre = xgbc.predict(x_test)
knc_pre = knc.predict(x_test_s)
svc_pre = svc.predict(x_test_s)
cbc_pre = cbc.predict(x_test)

# pipe lines

from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline

# pipeline

lr_pipe = make_pipeline(RobustScaler(), LogisticRegression(max_iter=1000, class_weight='balanced'))
knc_pipe = make_pipeline(RobustScaler(), KNeighborsClassifier())
svc_pipe = make_pipeline(RobustScaler(), SVC(decision_function_shape='ovr', class_weight='balanced'))

# cvs

lr_cvs = cross_val_score(lr_pipe, X,Y ,cv= sKf)
dtc_cvs = cross_val_score(DecisionTreeClassifier(class_weight='balanced'), X,Y ,cv= sKf)
rfc_cvs = cross_val_score(RandomForestClassifier(class_weight='balanced'), X,Y ,cv= sKf)
xgbc_cvs = cross_val_score(XGBClassifier(eval_metric='logloss', random_state=42), X,Y ,cv= sKf)
knc_cvs = cross_val_score(knc_pipe, X,Y ,cv= sKf)
svc_cvs= cross_val_score(svc_pipe, X,Y ,cv= sKf)
cbc_cvs = cross_val_score(CatBoostClassifier(), X,Y, cv= sKf)
# result 

cvss = [lr_cvs,dtc_cvs,rfc_cvs,xgbc_cvs,knc_cvs,svc_cvs, cbc_cvs]
cvs_name = ['lr_cvs','dtc_cvs','rfc_cvs','xgbc_cvs','knc_cvs','svc_cvs','cbc_cvs']

j= 0

for i in cvss:
    print(f"{cvs_name[j]} : {i}")
    j += 1

print("________________________________________________________")

# result mean

cvss = [lr_cvs,dtc_cvs,rfc_cvs,xgbc_cvs,knc_cvs,svc_cvs, cbc_cvs]
cvs_name = ['lr_cvs','dtc_cvs','rfc_cvs','xgbc_cvs','knc_cvs','svc_cvs','cbc_cvs']

j= 0

for i in cvss:
    print(f"{cvs_name[j]} mean : {i.mean()}")
    j += 1

print("____________________________________________________________")

# repot

print(classification_report(y_test, lr_pre))
print(classification_report(y_test, dtc_pre))
print(classification_report(y_test, rfc_pre))
print(classification_report(y_test, xgbc_pre))
print(classification_report(y_test, knc_pre))
print(classification_report(y_test, svc_pre))
print(classification_report(y_test, cbc_pre))

print("_________________________________________________________")

# graphical analysis of models

plt.barh(cvs_name, [i.mean() for i in cvss], color= ['skyblue', 'lightcoral', 'lightgreen', 'khaki', 'plum', 'powderblue', 'orange'])
plt.title('Models CV mean comparison'); plt.xlabel('Mean Results')
plt.tight_layout()
plt.show()

# result csv

comparison = pd.DataFrame({
    'Actual': y_test,
    'LR_Predicted':lr_pre,
    'DTC_Predicted':dtc_pre,
    'RFC_Predicted': rfc_pre,
    'XGBC_Predicted': xgbc_pre,
    'KNC_Predicted':knc_pre,
    'SVC_Predicted': svc_pre,
    'CBC_Predicted': cbc_pre})
comparison.to_csv('My Final Assessment/Models_Results_Analysis/heart_diesease_result.csv', index=False)
print(comparison)


# confusion matrix

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

cm = confusion_matrix(y_test, cbc_pre)

ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=['No Disease', 'Disease']
).plot()

plt.title('CatBoost Confusion Matrix')
plt.tight_layout()
plt.show()

# next graph

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, rfc_pre)

sns.heatmap(cm, annot=True, fmt='d', cmap='viridis',
            xticklabels=['No Disease', 'Disease'],
            yticklabels=['No Disease', 'Disease'])

plt.title('Random Forest Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.tight_layout()
plt.show()

# final report

print('\n\t\tCatBoost achieved the highest CV accuracy (80.08%) on this Dataset.')