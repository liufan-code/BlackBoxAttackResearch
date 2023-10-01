# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
import tensorflow as tf
from imblearn.over_sampling import SMOTE

# def getData(names):

# 	X = np.empty(shape=(0, 10))
# 	y = []
# 	rows_1 = [2000, 1225, 967, 2000, 2814, 2000, 2000]
# 	rows_2 = [1797, 208, 273, 1725, 598, 1559, 1484]

# 	for i, name in enumerate(names):

# 		if rows_1[i] != 0:
# 			data = pd.read_csv("/root/WorkPlace/ori_csv/ori_" + name + "_lenseq.csv", nrows=rows_1[i], index_col=0)
# 			_X = data.values
# 			X = np.vstack((X, _X))
# 			y += [[1, 0]] * rows_1[i]

# 		if rows_2[i] != 0:
# 			data = pd.read_csv("/root/WorkPlace/tor_csv/tor_" + name + "_lenseq.csv", nrows=rows_2[i], index_col=0)
# 			_X = data.values
# 			X = np.vstack((X, _X))
# 			y += [[0, 1]] * rows_2[i]

# 	X, y = shuffle(X, y)
# 	return X, y

# names = ["browsing", "email", "chat", "streaming", "file", "voip", "p2p"]
# X, y = getData(names)

# model_smote = SMOTE()

X_train = pd.read_csv("/root/WorkPlace/black_plus_csv/X_train_1_.csv", index_col=0).values.astype("float32")
y_train = pd.read_csv("/root/WorkPlace/black_plus_csv/y_train_1_.csv", index_col=0).values.astype("float32")

# X_train_2 = pd.read_csv("/root/WorkPlace/black_csv/X_train_2.csv", index_col=0).values
# y_train_2 = pd.read_csv("/root/WorkPlace/black_csv/y_train_2.csv", index_col=0).values

# X_train_3, y_train_3 = model_smote.fit_sample(X_train_2, y_train_2[...,0])
# y_train_3 = np.concatenate((y_train_3.reshape(len(y_train_3),1), 
# 							np.subtract(np.ones(len(y_train_3)), y_train_3).reshape(len(y_train_3),1)), axis=1)

# X_train = X_train_3
# X_test = pd.read_csv("/root/WorkPlace/black_csv/X_test.csv", index_col=0).values
# y_train = y_train_3
# y_test = pd.read_csv("/root/WorkPlace/black_csv/y_test.csv", index_col=0).values

# # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.1)
# X_train = tf.reshape(X_train, (X_train.shape[0], 10, 1))
X_train = tf.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
# X_test = tf.reshape(X_test, (X_test.shape[0], 10, 1))
# y_train = np.asarray(y_train).astype("float32")
# y_test = np.asarray(y_test).astype("float32")

model = tf.keras.Sequential()

model.add(tf.keras.layers.Conv1D(100, 2, padding='valid', activation='relu', input_shape=(100,1)))
model.add(tf.keras.layers.MaxPool1D(pool_size=2))
model.add(tf.keras.layers.Conv1D(100, 2, padding='valid', activation='relu'))
model.add(tf.keras.layers.MaxPool1D(pool_size=2))
model.add(tf.keras.layers.Dropout(0.25))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(100, activation='relu'))
model.add(tf.keras.layers.Dense(2, activation='softmax'))

model.compile(optimizer="adam",
              loss="binary_crossentropy",
              metrics=["acc"])
# model.summary()

history = model.fit(X_train, y_train, epochs=100, batch_size=20, validation_split=0.2)
# loss_and_metrics = model.evaluate(X_test, y_test)
# print('\n%s: %.2f%%' % (model.metrics_names[1], loss_and_metrics[1]*100))

# print(history.history["loss"])
# print(history.history["acc"])

# print(history.history["val_loss"])
# print(history.history["val_acc"])

model.save("/root/WorkPlace/model/cnn_tran.h5")