import numpy as np

X = np.random.rand(100, 5)
y = np.random.randint(0, 2, 100)

# no clean or encode cz simple array

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf

keras = tf.keras

# build model 

model = keras.models.Sequential([
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(16, activation='relu'),
        keras.layers.Dropout(0.4),
        keras.layers.Dense(1, activation='sigmoid')   
])

# compile

model.compile(optimizer= 'adam',loss= 'binary_crossentropy', metrics= ['accuracy'])

# train test split

from sklearn.model_selection import train_test_split

x_train, x_test,y_train , y_test = train_test_split(X,y , train_size= 0.8, random_state=50)

# fit

history= model.fit(x_train, y_train, epochs= 10, batch_size= 10, validation_split= 0.1)

# predict

y_prob = model.predict(x_test)

y_pre = (y_prob>= 0.5).astype(int)

# evaluation

from sklearn.metrics import classification_report

# print

print('Classification Report : ', classification_report(y_test, y_pre) )