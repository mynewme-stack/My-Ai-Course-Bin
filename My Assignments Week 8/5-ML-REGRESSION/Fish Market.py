import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('My Assignments Week 8/Fish Market Dataset/Fish.csv')
df_encod = pd.get_dummies(df, columns=['Species'], drop_first=True)  # it males seaparate columns  

# Making graphs to study data

plt.figure()
sns.regplot(data=df,x='Weight', y='Length1')
plt.show()

plt.figure()
sns.regplot(data=df,x='Weight', y='Length2')
plt.show()

plt.figure()
sns.regplot(data=df,x='Weight', y='Length3')
plt.show()

plt.figure()
sns.regplot(data=df,x='Weight', y='Height')
plt.show()

plt.figure()
sns.regplot(data=df,x='Weight', y='Width')
plt.show()

# Encoding

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

df['Species_encoded'] = le.fit_transform(df['Species'])
print("Class labels mapping:", dict(zip(le.classes_, le.transform(le.classes_))))

plt.figure()
sns.regplot(data=df,x='Weight', y='Species_encoded')
plt.show()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# Specifying it 

X=df_encod.drop(columns=["Weight"]).values        # just drop target else every column
y=df_encod["Weight"].values

# selecting model 

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,y, train_size=0.9, random_state=15)  

from sklearn.linear_model import LinearRegression
reg = LinearRegression(copy_X=True)

x_train = scaler.fit_transform(x_train)  
x_test = scaler.transform(x_test)

# training model

reg.fit(x_train,y_train)

# predicting

score = reg.predict(x_test)

# NOW 2ND MODEL ridge

from sklearn.linear_model import Ridge
ridge = Ridge(alpha= 0.1)

# fit

ridge.fit(x_train,y_train)

# predict y

pred_y = ridge.predict(x_test)

# result in csv to study better 

comparison = pd.DataFrame({
    'Actual': y_test,
    'Linear_Predicted': score,
    'Ridge_Predicted': pred_y
})
comparison.to_csv('My Assignments Week 8/Results/fish_result.csv')
print(comparison)

# Calculate percentages

linear = reg.score(x_test, y_test) * 100
ridge_acc = ridge.score(x_test, y_test) * 100

print(f"Linear accuracy: {linear}%")
print(f"Ridge accuracy:  {ridge_acc}%")