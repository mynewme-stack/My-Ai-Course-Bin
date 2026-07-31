import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn 
import tensorflow as tf
keras = tf.keras

# file

fashion_mnist = keras.datasets.fashion_mnist

# load data

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# analyze dataset

col = [x_train,y_train,x_test,y_test]
col_n = ['x_train','y_train','x_test','y_test']

j=0

for i in col: 
    print(f'{col_n[j]} shape : {i.shape}')
    j+=1

print('d-type = ', x_train.dtype)
print('d-type = ', y_train.dtype)

# -- min max

print('train x min : ',x_train.min())
print('train y max : ',x_train.max())

# -- unique

print('unique label : ' , np.unique(y_train))

# scale

x_train = x_train.astype('float32')/255.0
x_test = x_test.astype('float32')/255.0

# build nn

model = keras.models.Sequential([
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(64, activation= 'relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation='softmax')
])

# complie

model.compile(optimizer= 'adam',
              loss= 'sparse_categorical_crossentropy',
              metrics= ['accuracy'])

# fit

history = model.fit(x_train,y_train,
                    epochs = 20,
                    batch_size= 64,
                    validation_split= 0.4)

# predict

y_prob = model.predict(x_test)

#-- convert into class

y_pred = np.argmax(y_prob, axis=1)

# print
from sklearn.metrics import classification_report

print('Classification Report: ', classification_report(y_test, y_pred))