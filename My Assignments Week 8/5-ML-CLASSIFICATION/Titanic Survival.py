import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from sklearn.model_selection import KFold

# file 

df_n = pd.read_csv('My Assignments Week 8/Datasets_Download/Titanic/train.csv')

# overview

df_n.shape
df_n.info()
df_n.describe()
df_n.head()

# miss

df_n['Deck'] = df_n['Cabin'].str[0].fillna('U')

print("\nMiss Vals: ", df_n.isnull().sum())

df_n['Age'] = df_n['Age'].fillna(df_n.groupby(['Pclass', 'Sex'])['Age'].transform('median'))

# encod

df_n = df_n.drop(columns=['PassengerId','Name','Ticket','Cabin'])
df_n = pd.get_dummies(df_n, columns=['Sex','Embarked','Deck'], drop_first=True)

# missin per

print("\nMiss Vals: ", df_n.isnull().sum())

# graph

df = df_n.copy()

print(df.columns)

column =  ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex_male', 'Embarked_Q', 'Deck_B'] 

'''
for i in column: 
    plt.figure()
    sns.scatterplot(data=df, x = i, y = 'Survived', hue='Age')
    plt.show()

for i in column: 
    sns.set_theme(style='darkgrid')
    sns.barplot(data=df, x = i, y = 'Survived')
    plt.xticks(rotation=90)
    plt.show()

for i in column: 
    sns.set_theme(style='darkgrid')
    sns.boxplot(data=df, x = i, y = 'Survived')
    plt.xticks(rotation=90)
    plt.show()
'''
    
# kfold

kf = KFold(n_splits=5, shuffle= True, random_state= 50)

# outlier

df['Fare'] = np.log1p(df['Fare'])

# x an y

X = df.drop(columns= ['Survived']).values 
Y = df['Survived'].values

# train test

from sklearn.model_selection import train_test_split

x_train_n, x_test_n, y_train, y_test = train_test_split(X,Y, train_size= 0.85, random_state= 50)

# models

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

lr = LogisticRegression()
dtc = DecisionTreeClassifier()
rfc = RandomForestClassifier()
xgbc = XGBClassifier()
knc = KNeighborsClassifier()
svc = SVC()
grid = GridSearchCV(SVC(), param_grid, cv=kf, scoring='accuracy')

# scale

from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

x_train = scale.fit_transform(x_train_n)
x_test = scale.transform(x_test_n)

# fit

lr.fit(x_train, y_train)
dtc.fit(x_train_n, y_train)
rfc.fit(x_train_n, y_train)
xgbc.fit(x_train_n, y_train)
knc.fit(x_train,y_train)
svc.fit(x_train, y_train)
grid.fit(x_train, y_train)

# predi

lr_pre = lr.predict(x_test)
dtc_pre = dtc.predict(x_test_n)
rfc_pre = rfc.predict(x_test_n)
xgbc_pre = xgbc.predict(x_test_n)
knc_pre = knc.predict(x_test)
svc_pre = svc.predict(x_test)

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

# repot

print(classification_report(y_test, lr_pre))
print(classification_report(y_test, dtc_pre))
print(classification_report(y_test, rfc_pre))
print(classification_report(y_test, xgbc_pre))
print(classification_report(y_test, knc_pre))
print(classification_report(y_test, svc_pre))

# seprate

print("\nBest Parameters for SVC:", grid.best_params_)
best_svc_pre = grid.best_estimator_.predict(x_test)

print("\nTuned SVC Performance:")
print(classification_report(y_test, best_svc_pre))

# result csv

comparison = pd.DataFrame({
    'Actual': y_test,
    'LR_Predicted':lr_pre,
    'DTC_Predicted':dtc_pre,
    'RFC_Predicted': rfc_pre,
    'XGBC_Predicted': xgbc_pre,
    'KNC_Predicted':knc_pre,
    'SVC_Predict':svc_pre})
comparison.to_csv('My Assignments Week 8/Results/Titanic_result.csv', index=False)
print(comparison)

'''
# competition

kag_t = pd.read_csv('My Assignments Week 8/Datasets_Download/Titanic/test (1).csv')

pas_id = kag_t['PassengerId']

kag_t['Deck'] = kag_t['Cabin'].str[0].fillna('U')

kag_t['Age'] = kag_t['Age'].fillna(kag_t.groupby(['Pclass', 'Sex'])['Age'].transform('median'))
kag_t['Fare'] = kag_t['Fare'].fillna(kag_t['Fare'].median())

kag_t = kag_t.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'])

kag_t_enc = pd.get_dummies(kag_t, columns=['Sex', 'Embarked', 'Deck'], drop_first=True)

train_col = df_n.drop(columns=['Survived']).columns

kag_t_enc = kag_t_enc.reindex(columns=train_col, fill_value=0)

X_kag_t = kag_t_enc.values

X_kag_t_s = scale.transform(X_kag_t)

final_predictions = xgbc.predict(X_kag_t)

submission = pd.DataFrame({
    'PassengerId': pas_id,
    'Survived': final_predictions
})

# save

submission.to_csv('My Assignments Week 8/Results/Kaggle_Submission.csv', index=False)
print("\nSub")
'''