import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

# file

u_df = pd.read_excel('My Final Assessment\\Datasets_Used\\Top-10-Healthcare-Companies-in-the-USA\\Top 10 Healthcare Companies in the United States.xlsx',
                     sheet_name='CVS Health Corp. (CVS)',
                     skiprows= 4)

print('File: ',u_df)

# Overview

u_df.info()
print('Shape: ',u_df.shape)
print('Columns: ',u_df.columns)
print('Statistics: ',u_df.describe())
print('Summary: ',u_df.describe(include='all'))

#--deep analytics

print(f"Max Stock Price Recorded: {u_df['High'].max()}")
print('Max Trading Volume Peak:' ,u_df['Volume'].max())
print(f"Date of Maximum Market Activity: {u_df.loc[u_df['High'].idxmax(), 'Date']}")

# Cleaning data

#-- handling dates

u_df['Date'] = pd.to_datetime(u_df['Date'].astype(str).str.replace(r'오후|오전', '', regex=True).str.strip(), errors='coerce')    # clean date
u_df = u_df.dropna(subset=['Date']).sort_values('Date').reset_index(drop=True)

# Adding a 7-day Moving Average to help models see trends

u_df['MA7'] = u_df['Close'].rolling(window=7).mean().bfill()

#-- missing values

print('Missing values: ',u_df.isnull().sum())

# visualization

print(u_df.columns)

column = ['Close', 'High', 'Low', 'Volume', 'MA7']
col_n = ['Close', 'High', 'Low', 'Volume','MA7']

j=0

for i in column:
    sns.set_theme(style='darkgrid')
    sns.lineplot(u_df, x='Date' ,y=i, color='darkcyan')
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
    sns.scatterplot(u_df, x=i ,y='Close', color='red')
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

sns.heatmap(u_df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1)

plt.xticks(rotation= 45)

plt.title('Feature Correaltion Heatmap')
plt.tight_layout()
plt.show()

# scaling 

from sklearn.preprocessing import MinMaxScaler

mm_scale = MinMaxScaler()

# Feature array

feature = ['Close', 'High', 'Low', 'Volume','MA7']

data= u_df[feature].values

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
    Dropout(0.2),
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

y_test = np.concatenate([y for x, y in test_ds], axis=0)  # separatE

cnn_pre = model.predict(test_ds)

y_pre = cnn_pre.flatten()

# report

from sklearn.metrics import mean_squared_error, mean_absolute_error


cnn_mse = mean_squared_error(y_test,y_pre)

cnn_mae = mean_absolute_error(y_test,y_pre)

cnn_rmse = np.sqrt(cnn_mse)

# calculate r^2

# r^2

from sklearn.metrics import r2_score

lstm_r2 = r2_score(y_test, lstm_pre.flatten())
gru_r2 = r2_score(y_test, gru_pre.flatten())
srnn_r2 = r2_score(y_test, srnn_pre.flatten())
cnn_r2 = r2_score(y_test, cnn_pre.flatten())

# print result

comparison = pd.DataFrame({
    'Actual': y_test,
    'LSTM_Predicted':lstm_pre.flatten(),
    'GRU_Predicted':gru_pre.flatten(),
    'SRNN_Predicted': srnn_pre.flatten(),
    'CNN_Predicted': cnn_pre.flatten()})
comparison.to_csv('My Final Assessment/Models_Results_Analysis/top_10_healthcare.csv', index=False)

print(comparison)

metrics = pd.DataFrame({
    "Model": ["LSTM", "GRU", "SimpleRNN", "CNN-LSTM"],
    "MSE": [lstm_mse, gru_mse, srnn_mse, cnn_mse],
    "MAE": [lstm_mae, gru_mae, srnn_mae, cnn_mae],
    "RMSE": [lstm_rmse, gru_rmse, srnn_rmse, cnn_rmse],
    "R2": [lstm_r2, gru_r2, srnn_r2, cnn_r2]

})

metrics.to_csv(
    "My Final Assessment/Models_Results_Analysis/model_metrics_for_top10.csv",
    index=False
)

print(metrics)

# DL model comparison graph

plt.figure(figsize=(8,5))

sns.barplot(data=metrics, x='Model', y='R2')

plt.title('DL Models R² Comparison')
plt.xlabel('Deep Learning Model')
plt.ylabel('R² Score')
plt.xticks(rotation=15)
plt.tight_layout()
plt.show() 

# observations

print('Overall, the results demonstrate that hybrid CNN-LSTM was the most effective architecture for this time-series prediction problem.')

print('''
Overall Evaluation: CNN-LSTM gives the best performance with R² = 0.561, 
followed by LSTM (R² = 0.524), while SimpleRNN performed weakest (R² = −2.513).

Best Model: CNN-LSTM is selected as the final model because it combines CNN-based temporal feature extraction
with LSTM sequence learning.

Final Decision: Therefore, CNN-LSTM is the most suitable architecture among the four tested models
for predicting CVS closing prices.

''')