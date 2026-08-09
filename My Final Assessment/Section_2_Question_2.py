import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# file

d_df = pd.read_excel('My Final Assessment\\Datasets_Used\\Top-10-Healthcare-Companies-in-the-USA\\Top 10 Healthcare Companies in the United States.xlsx',
                     sheet_name='Elevance Health (ELV)',
                     skiprows= 4)

print('File: ',d_df)

# Overview

d_df.info()
print('Shape: ',d_df.shape)
print('Columns: ',d_df.columns)
print('Statistics: ',d_df.describe())
print('Summary: ',d_df.describe(include='all'))

# deeper analysis 

print(f"Elevance health (ELV) Peak Price: {d_df['High'].max()}")
print(f"Max daily Trading Volume: {d_df['Volume'].max()}")
print(f"Date of Peak Market activity: {d_df.loc[d_df['High'].idxmax(),'Date'] if 'Date' in d_df.columns else 'N/A'}") 

# Missing values

print('Missing values: ',d_df.isnull().sum())

print('Percentage of Missing values : ',d_df.isnull().mean() * 100)

# feature

d_df['MA7'] = d_df['Close'].rolling(window=10).mean().bfill()   # 10 days moving average

# checking: 

'''
un_df = d_df.dropna(subset=['',''])
'''

# checking dulpicate

dupli_row = d_df.duplicated().sum()

print('Duplicate rows : ', dupli_row)

# Overview

d_df.info()
print('Statistics: ',d_df.describe())
print('Summary: ',d_df.describe(include='all'))
print('Shape: ',d_df.shape)
print('Columns: ',d_df.columns)

print("_____________________________________")


# data cleaning

#-- handling dates

d_df['Date'] = pd.to_datetime(d_df['Date'].astype(str).str.replace(r'오후|오전', '', regex=True).str.strip(), errors='coerce')    # clean dates
d_df = d_df.dropna(subset=['Date']).sort_values('Date').reset_index(drop=True)

#-- missing values

print('Missing values: ',d_df.isnull().sum())

# visualization

print(d_df.columns)

column = ['Close', 'High', 'Low', 'Volume', 'MA7']
col_n = ['Close', 'High', 'Low', 'Volume', 'MA7']

j=0

for i in column:
    sns.set_theme(style='darkgrid')
    sns.lineplot(d_df, x='Date' ,y=i, color='darkcyan')
    plt.xlabel('Date')
    plt.ylabel(col_n[j])
    plt.xticks(rotation= 45)
    plt.title('Proof of Time Series Problem')
    plt.tight_layout()
    plt.show()

    j+=1

#-- now relation with target

column = ['High', 'Low', 'Volume', 'MA7']

for i in column:
    sns.set_theme(style='whitegrid')
    sns.scatterplot(d_df, x=i ,y='Close', color='red')
    plt.xlabel(i)
    plt.ylabel('Close')
    plt.xticks(rotation= 45)
    plt.title('Data Analysis')
    plt.tight_layout()
    plt.show()

    j+=1

#-- analyzing data

sns.set_theme(style='white')

plt.figure(figsize=(7,5))

sns.heatmap(d_df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1)

plt.xticks(rotation= 45)

plt.title('Feature Correaltion Heatmap')
plt.tight_layout()
plt.show()

# scaling 

from sklearn.preprocessing import MinMaxScaler

mm_scale = MinMaxScaler()

# Feature array

feature = ['Close', 'High', 'Low', 'Volume', 'MA7']

data= d_df[feature].values

df= mm_scale.fit_transform(data)
 
# train_test

split_idx= int(len(df)* 0.83)
train_df= df[:split_idx]
test_df= df[split_idx:]

#-- train test separate x and y 

from tensorflow.keras.utils import timeseries_dataset_from_array

train_ds = timeseries_dataset_from_array(train_df[:-30], targets= train_df[30:,0], sequence_length= 30, batch_size= 40)
test_ds = timeseries_dataset_from_array(test_df[:-30], targets= test_df[30:,0], sequence_length= 30, batch_size= 40)

# model

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import tensorflow as tf

#-- lstm

model = Sequential([

    LSTM(units= 128, return_sequences= True, input_shape= (30,5)),
    Dropout(0.4),
    LSTM(units= 64, return_sequences= False),
    Dropout(0.2),
    Dense(units=16, activation='relu'),
    Dense(units=1, activation='linear')
])

#-- compile

model.compile(optimizer='adam',
              loss= 'mean_squared_error', metrics= ['mean_absolute_error'])

# train

#-- early stopping to prevent overfitting

from tensorflow.keras.callbacks import ModelCheckpoint

checkpoint= ModelCheckpoint(
    'best_model.h5',
    monitor='val_loss',
    save_best_only=True,
    mode='min'
)

# fit 

history= model.fit(train_ds, epochs= 30,
                   validation_data= test_ds,callbacks=[checkpoint],
                     verbose= 1)

# predict

y_test = np.concatenate([y for x, y in test_ds], axis=0)  # separate y

lstm_pre = model.predict(test_ds)

y_pre = lstm_pre.flatten()

# report

from sklearn.metrics import mean_squared_error, mean_absolute_error

lstm_mse = mean_squared_error(y_test,y_pre)
lstm_mae = mean_absolute_error(y_test,y_pre)
lstm_rmse = np.sqrt(lstm_mse)

#-- cnn-lstm


from tensorflow.keras.layers import Conv1D, MaxPooling1D

model = Sequential([
    Conv1D(64, kernel_size=3, activation= 'relu',input_shape= (30,5)),
    MaxPooling1D(pool_size= 2),
    LSTM(64),
    Dense(16, activation='relu'),
    Dropout(0.2),
    Dense(1)
])

#-- compile

model.compile(optimizer='adam',
              loss= 'mean_squared_error', metrics= ['mean_absolute_error'])

# train

#-- early stopping to prevent overfitting

from tensorflow.keras.callbacks import ModelCheckpoint

checkpoint= ModelCheckpoint(
    'best_model.keras',
    monitor='val_loss',
    save_best_only=True,
    mode='min'
)

# fit 

history= model.fit(train_ds, epochs= 30,
                   validation_data= test_ds,callbacks=[checkpoint],
                verbose= 1)

# predict

y_test = np.concatenate([y for x, y in test_ds], axis=0)  # separate

cnn_pre = model.predict(test_ds)

y_pre = cnn_pre.flatten()

# report

from sklearn.metrics import mean_squared_error, mean_absolute_error


cnn_mse = mean_squared_error(y_test,y_pre)

cnn_mae = mean_absolute_error(y_test,y_pre)

cnn_rmse = np.sqrt(cnn_mse)


#-- blstm
from tensorflow.keras.layers import Bidirectional

model = Sequential([

    Bidirectional(LSTM(units= 128, return_sequences= True, input_shape= (30,5))),
    Dropout(0.2),
    Bidirectional(LSTM(units= 64, return_sequences= False)),
    Dropout(0.2),
    Dense(units=16, activation='relu'),
    Dense(units=1, activation='linear')
])

#-- compile

model.compile(optimizer='adam',
              loss= 'mean_squared_error', metrics= ['mean_absolute_error'])

# train

#-- early stopping to prevent overfitting

from tensorflow.keras.callbacks import ModelCheckpoint

checkpoint= ModelCheckpoint(
    'best_model.h5',
    monitor='val_loss',
    save_best_only=True,
    mode='min'
)

# fit 

history= model.fit(train_ds, epochs= 30,
                   validation_data= test_ds,callbacks=[checkpoint],
                     verbose= 1)

# predict

y_test = np.concatenate([y for x, y in test_ds], axis=0)  # separate y

blstm_pre = model.predict(test_ds)

y_pre = blstm_pre.flatten()

# report

from sklearn.metrics import mean_squared_error, mean_absolute_error

blstm_mse = mean_squared_error(y_test,y_pre)
blstm_mae = mean_absolute_error(y_test,y_pre)
blstm_rmse = np.sqrt(blstm_mse)

#-- GRU

from tensorflow.keras.layers import GRU

model = Sequential([

    GRU(128, return_sequences= True, input_shape= (30,5)),
    Dropout(0.4),
    GRU(64),
    Dropout(0.4),
    Dense(16, activation='relu'),
    Dropout(0.2),
    Dense(1)
])

#-- compile

model.compile(optimizer='adam',
              loss= 'mean_squared_error', metrics= ['mean_absolute_error'])

# train

#-- early stopping to prevent overfitting

from tensorflow.keras.callbacks import ModelCheckpoint

checkpoint= ModelCheckpoint(
    'best_model.keras',
    monitor='val_loss',
    save_best_only=True,
    mode='min'
)

# fit 

history= model.fit(train_ds, epochs= 30,
                   validation_data= test_ds,callbacks=[checkpoint],
                verbose= 1)

# predict

y_test = np.concatenate([y for x, y in test_ds], axis=0)  # separatE

gru_pre = model.predict(test_ds)

y_pre = gru_pre.flatten()

# report

from sklearn.metrics import mean_squared_error, mean_absolute_error


gru_mse = mean_squared_error(y_test,y_pre)

gru_mae = mean_absolute_error(y_test,y_pre)

gru_rmse = np.sqrt(gru_mse)

#-- simple rnn

from tensorflow.keras.layers import SimpleRNN

model = Sequential([

    SimpleRNN(128, return_sequences= True, input_shape= (30,5)),
    Dropout(0.2),
    SimpleRNN(64),
    Dropout(0.4),
    Dense(16, activation='relu'),
    Dropout(0.2),
    Dense(1)
])

#-- compile

model.compile(optimizer='adam',
              loss= 'mean_squared_error', metrics= ['mean_absolute_error'])

# train

#-- early stopping to prevent overfitting

from tensorflow.keras.callbacks import ModelCheckpoint

checkpoint= ModelCheckpoint(
    'best_model.keras',
    monitor='val_loss',
    save_best_only=True,
    mode='min'
)

# fit 

history= model.fit(train_ds, epochs= 30,
                   validation_data= test_ds,callbacks=[checkpoint],
                verbose= 1)

# predict

y_test = np.concatenate([y for x, y in test_ds], axis=0)  # separatE

srnn_pre = model.predict(test_ds)

y_pre = srnn_pre.flatten()

# report

from sklearn.metrics import mean_squared_error, mean_absolute_error


srnn_mse = mean_squared_error(y_test,y_pre)

srnn_mae = mean_absolute_error(y_test,y_pre)

srnn_rmse = np.sqrt(srnn_mse)

# calculate r^2

# r^2

from sklearn.metrics import r2_score

lstm_r2 = r2_score(y_test, lstm_pre.flatten())
gru_r2 = r2_score(y_test, gru_pre.flatten())
srnn_r2 = r2_score(y_test, srnn_pre.flatten())
cnn_r2 = r2_score(y_test, cnn_pre.flatten())
blstm_r2 = r2_score(y_test, blstm_pre.flatten())

# print result

comparison = pd.DataFrame({
    'Actual': y_test,
    'LSTM_Predicted':lstm_pre.flatten(),
    'GRU_Predicted':gru_pre.flatten(),
    'SRNN_Predicted': srnn_pre.flatten(),
    'CNN_Predicted': cnn_pre.flatten(),
    'BLSTM': blstm_pre.flatten()
    })
comparison.to_csv('My Final Assessment/Models_Results_Analysis/top_10_2_healthcare.csv', index=False)

print(comparison)

#  csv

metrics = pd.DataFrame({
    "Model": ["LSTM","BLSTM", "GRU", "SimpleRNN", "CNN-LSTM"],
    "MSE": [lstm_mse,blstm_mse, gru_mse, srnn_mse, cnn_mse],
    "MAE": [lstm_mae,blstm_mae, gru_mae, srnn_mae, cnn_mae],
    "RMSE": [lstm_rmse,blstm_rmse, gru_rmse, srnn_rmse, cnn_rmse],
    "R2": [lstm_r2,blstm_r2, gru_r2, srnn_r2, cnn_r2]

})

metrics.to_csv(
    "My Final Assessment/Models_Results_Analysis/model_metrics_for_top10_2.csv",
    index=False
)

print(metrics)

# final report



print(f"Model Performance: The best performing model was {metrics.loc[metrics['R2'].idxmax(), 'Model']}.")

print("Healthcare Context: Accurate prediction of Elevance Health's stock volatility allows for better ")

print("capital management, ensuring the organization remains robust for delivering cost-effective patient care.")

print('I changed the model settings (like the number of neurons) and added a Bidirectional LSTM just for the Elevance Health data to catch its special changes.')
 


# Metric Graph

plt.figure(figsize=(8,4))
sns.barplot(data=metrics, x='Model', y='R2', palette='viridis')
plt.title('Elevance Health (ELV): Model R² Comparison')
plt.show()
