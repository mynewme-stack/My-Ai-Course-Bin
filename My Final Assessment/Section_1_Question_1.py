import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''
Cleaning Data
'''
# file

un_df= pd.read_csv('My Final Assessment\\Datasets_Used\\USA-Hospitals\\Hospitals.csv')

# Missing vals

print('Missing values : ', un_df.isnull().sum())

# cleaning data

un_df = un_df.dropna(subset=["ALT_NAME",'ST_FIPS','OWNER','TTL_STAFF','BEDS','TRAUMA','HELIPAD'])

# Missing vals now

print('\nMiss values now : ', un_df.isnull().sum())

print("_____________________________________")

# Check duplicates 

dupli_row = un_df.duplicated().sum()

print('Duplicate rows : ', dupli_row)

print("_____________________________________")


#--- ids should be unique

dupli_id = un_df.duplicated(subset='ID').sum()

print('Duplicate ids : ',dupli_id)

print("_____________________________________")


# Overview

un_df.info()
print('Statistics: ',un_df.describe())
print('Summary: ',un_df.describe(include='all'))
print('Shape: ',un_df.shape)
print('Columns: ',un_df.columns)

print("_____________________________________")

# making target 

#--- max beds

print('Maximum: ',un_df['BEDS'].max())

#--- min beds

print('Minimum: ',un_df['BEDS'].min())

print('Before Removal -999: ',un_df['BEDS'].mean())

print("__________________________________________")

# -999 a special number which is making just 8% of beds and i dont want to risk model learning so removing

con_beds = un_df.loc[un_df['BEDS'] < 0, 'BEDS'].tolist()
unique = set(con_beds)

if unique == {-999}:
    print('\nOnly -999') 
else:
    print('\n\nOther List: ', con_beds)

#--- percentage

print("_____________________________________")

percentage = (un_df['BEDS'] == -999).mean() * 100
print(f"Percentage of -999: {percentage}%")

#--- remove -999 

un_df = un_df[un_df['BEDS'] >= 0]
print('After Removal of -999: ',un_df['BEDS'].mean())

print("_____________________________________")

#--- classes

un_df['BEDS_CATEGORY'] = pd.cut(un_df['BEDS'], bins=[-1, 99, 499, np.inf], labels=[0,1,2])    # make number sort in

print(un_df) # check

un_df= un_df.drop(columns=['BEDS'])

""" 
According to industry standards (like the Google searches i found):
Small: < 100 beds
Medium: 100 – 499 beds
Large: 500+ beds

"""

# feature engineering

#--- dropping columns

un_df = un_df.drop(columns=['X','Y','OBJECTID','ID','NAME','ADDRESS','CITY','STATE','ZIP','ZIP4','TELEPHONE','COUNTY','COUNTYFIPS','COUNTRY','LATITUDE','LONGITUDE','NAICS_CODE','NAICS_DESC','SOURCE','SOURCEDATE','VAL_METHOD','VAL_DATE','WEBSITE','STATE_ID','ALT_NAME'])

print('Remaining columns: ',un_df.columns)

print("_____________________________________")

#--- graphs to study which columns are useless

column = ['TYPE','STATUS', 'POPULATION', 'ST_FIPS', 'OWNER', 'TTL_STAFF', 'TRAUMA', 'HELIPAD']
col_n = ['TYPE','STATUS', 'POPULATION', 'ST_FIPS', 'OWNER', 'TTL_STAFF', 'TRAUMA', 'HELIPAD']

j=0

'''
Graphical Visualiztion
'''

for i in column:
    sns.set_theme(style='whitegrid')
    sns.histplot(un_df, x=i, hue='BEDS_CATEGORY', multiple='stack',
                            palette=["steelblue", "teal", "salmon"])
    plt.xlabel(col_n[j])
    plt.ylabel('BEDS_CATEGORY')
    plt.xticks(rotation= 90)
    plt.tight_layout()
    plt.show()
    j+=1


#--- proof classification

column = ['TYPE','STATUS', 'ST_FIPS', 'OWNER', 'TTL_STAFF', 'TRAUMA', 'HELIPAD']
col_n = ['TYPE','STATUS', 'ST_FIPS', 'OWNER', 'TTL_STAFF', 'TRAUMA', 'HELIPAD']

j=0

for i in column:
    sns.set_theme(style='whitegrid')
    sns.countplot(
    data=un_df,
    x=i,
    hue='BEDS_CATEGORY')
    plt.xlabel(col_n[j])
    plt.ylabel('BEDS_CATEGORY')
    plt.xticks(rotation= 90)
    plt.tight_layout()
    plt.show()
    j+=1

#----- data analysis using pie chart

print(un_df['BEDS_CATEGORY'].value_counts(normalize=True).sort_index() * 100)    

plt.pie(un_df['BEDS_CATEGORY'].value_counts(), labels=['Small', 'Medium', 'Large'], autopct='%1.1f%%',
        colors=['skyblue', 'lightgreen', 'peachpuff'],
        wedgeprops={'linewidth': 0.2, 'edgecolor': 'grey'})

plt.title('Data Classification')
plt.tight_layout()
plt.show()

#--- enocoding

df = pd.get_dummies(un_df, columns=['TYPE', 'STATUS','OWNER', 'ST_FIPS', 'TRAUMA', 'HELIPAD'], drop_first=True)

#--- check for missing vals

print('Missing values in TTL_STAFF, POPULATION : ', df[['POPULATION','TTL_STAFF']].isnull().sum())

print("_____________________________________")

#--- kfold

from sklearn.model_selection import StratifiedKFold

Kf = StratifiedKFold(
    n_splits=6,
    shuffle=True,
    random_state=20)

# x and y

'''
My target is to find whether a hospital is small, medium or large on the basis of number of beds available
in hospital.

'''

X=  df.drop(columns=['BEDS_CATEGORY','TTL_STAFF']).values

X_ts = df.drop(columns=['BEDS_CATEGORY']).values

'''
After Analyzing first time, i decided to remove ttl_staff because ttl_staff has a very strong relationship with
hospital size. Therefore, I evaluated models both with and without TTL_STAFF to determine 
whether the classification task was genuinely learning or not. Because Decision Tree Classifier doing best
so i m training data with total staff with only this model.

'''

Y= df['BEDS_CATEGORY'].astype(int)

# train_test_split

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X,Y , train_size=0.80, random_state=20, stratify= Y)

#-- with ttl _ staff

x_train_ts, x_test_ts, y_train_ts, y_test_ts = train_test_split(X_ts,Y 
                            , train_size=0.80, random_state=20, stratify= Y)

# scaling

from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()

x_train_s = scaler.fit_transform(x_train)
x_test_s = scaler.transform(x_test)

# algorithm 

from sklearn.linear_model import LogisticRegression
from sklearn.tree import  DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

# name 

lr = LogisticRegression(max_iter=1000,class_weight='balanced')
dtc = DecisionTreeClassifier(class_weight='balanced')
dtc_ts = DecisionTreeClassifier(class_weight='balanced')
rfc = RandomForestClassifier(class_weight='balanced')
xgbc = XGBClassifier(eval_metric= 'mlogloss')
knc = KNeighborsClassifier()

# fit

lr.fit(x_train_s, y_train)
dtc.fit(x_train, y_train)
dtc_ts.fit(x_train_ts, y_train_ts)
rfc.fit(x_train, y_train)
xgbc.fit(x_train, y_train)
knc.fit(x_train_s,y_train)

# predict

lr_pre = lr.predict(x_test_s)
dtc_pre = dtc.predict(x_test)
dtc_pre_ts = dtc_ts.predict(x_test_ts)
rfc_pre = rfc.predict(x_test)
xgbc_pre = xgbc.predict(x_test)
knc_pre = knc.predict(x_test_s)

# pipe lines

from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline

# pipeline

lr_pipe = make_pipeline(RobustScaler(), LogisticRegression(max_iter=1000, class_weight='balanced'))
knc_pipe = make_pipeline(RobustScaler(), KNeighborsClassifier())

# cvs

lr_cvs = cross_val_score(lr_pipe, X,Y ,cv= Kf)
dtc_cvs = cross_val_score(DecisionTreeClassifier(class_weight='balanced'), X,Y ,cv= Kf)
dtc_cvs_ts = cross_val_score(DecisionTreeClassifier(class_weight='balanced'), X_ts,Y ,cv= Kf)
rfc_cvs = cross_val_score(RandomForestClassifier(class_weight='balanced'), X,Y ,cv= Kf)
xgbc_cvs = cross_val_score(XGBClassifier(eval_metric= 'mlogloss'), X,Y ,cv= Kf)
knc_cvs = cross_val_score(knc_pipe, X,Y ,cv= Kf)


# result 

cvss = [lr_cvs,dtc_cvs,dtc_cvs_ts,rfc_cvs,xgbc_cvs,knc_cvs]
cvs_name = ['lr_cvs','dtc_cvs','dtc_cvs_ts','rfc_cvs','xgbc_cvs','knc_cvs']

j= 0

for i in cvss:
    print(f"{cvs_name[j]} : {i}")
    j += 1

print("____________________________________________________________________________")

# result mean

cvss = [lr_cvs,dtc_cvs,dtc_cvs_ts,rfc_cvs,xgbc_cvs,knc_cvs]
cvs_name = ['lr_cvs','dtc_cvs','dtc_cvs_ts','rfc_cvs','xgbc_cvs','knc_cvs']

j= 0

for i in cvss:
    print(f"{cvs_name[j]} mean : {i.mean()}")
    j += 1

print("__________________________________________________________________________")

# report

print(classification_report(y_test, lr_pre))
print(classification_report(y_test, dtc_pre))
print(classification_report(y_test_ts, dtc_pre_ts))
print(classification_report(y_test, rfc_pre))
print(classification_report(y_test, xgbc_pre))
print(classification_report(y_test, knc_pre))

print("______________________________________________________________________________________")

# observations

'''

As, ttl_staff and population depends very directly to the hospital is small, medium and large.
So, If these two features are available, model can predict size of hospital very precisely. 
A Decision Tree using TTL_STAFF got the highest score of 99.68% accuracy. 
A standard Decision Tree got 99.67% accuracy. 
The tiny difference means both models work almost the same way here.

'''

# graphical analysis of models

i = 0

plt.barh(cvs_name, [i.mean() for i in cvss], color= ['skyblue', 'lightcoral', 'lightgreen', 'khaki', 'plum', 'pink'])
plt.title('6 Fold Cross Validation Performance')
plt.xlabel('Mean Cross Validation Accuracy')
plt.tight_layout()
plt.show()

# result csv

comparison = pd.DataFrame({
    'Actual': y_test,
    'LR_Predicted':lr_pre,
    'DTC_Predicted':dtc_pre,
    'DTC_TS_Predicted': dtc_pre_ts,
    'RFC_Predicted': rfc_pre,
    'XGBC_Predicted': xgbc_pre,
    'KNC_Predicted':knc_pre})
comparison.to_csv('My Final Assessment/Models_Results_Analysis/hospital_beds_result.csv', index=False)
print(comparison)


# confusion Matrix - Best Model

cm = confusion_matrix(y_test_ts, dtc_pre_ts)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=['Small', 'Medium', 'Large']
)


disp.plot()
plt.title('Decision Tree Confusion Matrix')
plt.tight_layout()
plt.show()

# final report

print('\n\t\tDecision Tree with TTL_STAFF achieved the highest CV accuracy (99.68%).')