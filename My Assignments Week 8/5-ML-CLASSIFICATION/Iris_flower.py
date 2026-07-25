import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold

# path

df_n = pd.read_csv('My Assignments Week 8/Datasets_Download/Iris.csv')

# basic 

df_n.shape
df_n.info()
df_n.describe()
df_n.head()

# graphs

column = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']


for i in column: 
    plt.figure()
    sns.scatterplot(data=df, x = i, y = 'Species', hue='Id')
    plt.show()

for i in column: 
    sns.set_theme(style='darkgrid')
    sns.barplot(data=df, x = i, y = 'Species')
    plt.show()

for i in column: 
    sns.set_theme(style='darkgrid')
    sns.boxplot(data=df, x = i, y = 'Species')
    plt.show()


# handle outlier 

df = df_n.copy()
Q1, Q3 = df['SepalWidthCm'].quantile([0.25, 0.75])
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

# outlier

df['SepalWidthCm'] = df['SepalWidthCm'].clip(lower=lower_limit, upper=upper_limit)

# x and y

X = df.drop(columns=['Id','Species']).values

# encoding 

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

Y = le.fit_transform(df['Species'].values)

# kfold

kf = KFold(n_splits=5, shuffle=True, random_state=50)

# traintest

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X, Y, train_size= 0.8, random_state= 50)

# models 

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# naming

lr = LogisticRegression()
dtc = DecisionTreeClassifier()
rfc = RandomForestClassifier()
knc = KNeighborsClassifier()
svc = SVC()

# scale

from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

x_train_s = scale.fit_transform(x_train)
x_test_s = scale.transform(x_test)

# fit

lr.fit(x_train_s,y_train)
dtc.fit(x_train,y_train)
rfc.fit(x_train,y_train)
knc.fit(x_train_s,y_train)
svc.fit(x_train_s,y_train)

# pre

lr_pre = lr.predict(x_test_s)
dtc_pre = dtc.predict(x_test)
rfc_pre = rfc.predict(x_test)
knc_pre = knc.predict(x_test_s)
svc_pre = svc.predict(x_test_s)

# cvs and pipe

from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline

# piplines

lr_pipe = make_pipeline(StandardScaler(),LogisticRegression())
knc_pipe = make_pipeline(StandardScaler(), KNeighborsClassifier())
svc_pipe = make_pipeline(StandardScaler(), SVC())

# cvs

lr_cvs = cross_val_score(lr_pipe, X,Y, cv=kf)
dtc_cvs = cross_val_score(DecisionTreeClassifier(), X,Y, cv=kf)
rfc_cvs = cross_val_score(RandomForestClassifier(), X,Y, cv=kf)
knc_cvs = cross_val_score(knc_pipe, X,Y, cv=kf)
svc_cvs = cross_val_score(svc_pipe, X,Y, cv=kf)

# result 

cvss = [lr_cvs,dtc_cvs,rfc_cvs,knc_cvs,svc_cvs]
cvs_name = ['lr_cvs','dtc_cvs','rfc_cvs','knc_cvs','svc_cvs']

j= 0

for i in cvss:
    print(f"{cvs_name[j]} : {i}")
    j += 1

# result mean

cvss = [lr_cvs,dtc_cvs,rfc_cvs,knc_cvs,svc_cvs]
cvs_name = ['lr_cvs','dtc_cvs','rfc_cvs','knc_cvs','svc_cvs']

j= 0

for i in cvss:
    print(f"{cvs_name[j]} mean : {i.mean()}")
    j += 1

# repot

from sklearn.metrics import classification_report

print(classification_report(y_test, lr_pre))
print(classification_report(y_test, dtc_pre))
print(classification_report(y_test, rfc_pre))
print(classification_report(y_test, knc_pre))
print(classification_report(y_test, svc_pre))

# result csv

comparison = pd.DataFrame({
    'Actual': y_test,
    'LR_Predicted':lr_pre,
    'DTC_Predicted':dtc_pre,
    'RFC_Predicted': rfc_pre,
    'KNC_Predicted':knc_pre,
    'SVC_Predict':svc_pre})
comparison.to_csv('My Assignments Week 8/Results/Iris_result.csv')
print(comparison)