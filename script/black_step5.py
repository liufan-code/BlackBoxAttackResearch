# -*- coding: utf-8 -*-

from tensorflow.keras.models import load_model
import pandas as pd
import tensorflow as tf
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

adv_mim = pd.read_csv("E://WorkPlace/black_csv/adv_lstm_mim.csv", index_col=0).values.astype("float32")
adv_cw = pd.read_csv("E://WorkPlace/black_csv/adv_lstm_cw.csv", index_col=0).values.astype("float32")

X_train = pd.read_csv("E://WorkPlace/black_csv/X_train_1.csv", index_col=0).values
y_train = pd.read_csv("E://WorkPlace/black_csv/y_train_1.csv", index_col=0).values

model_knn = KNeighborsClassifier().fit(X_train, y_train)
model_randomforest = RandomForestClassifier(n_estimators=10, random_state=0).fit(X_train, y_train)
model_dnn = load_model("E://WorkPlace/model/dnn_black.h5")
model_cnn = load_model("E://WorkPlace/model/cnn_black.h5")
model_lstm = load_model("E://WorkPlace/model/lstm_black.h5")

X_test = pd.read_csv("E://WorkPlace/black_csv/X_test.csv", index_col=0).values.astype("float32")

# KNN

pred = model_knn.predict(X_test)
adv_pred = model_knn.predict(adv_mim)
count = 0
total = 0
for i in range(len(X_test)):
	if pred[i][0] < 0.5:
		total += 1
		if adv_pred[i][0] > 0.5: 
			count += 1
print("Success rate of MIM on KNN: " + str(round(count/(total*0.01), 2)) + "%")

adv_pred = model_knn.predict(adv_cw)
count = 0
total = 0
for i in range(len(X_test)):
	if pred[i][0] < 0.5:
		total += 1
		if adv_pred[i][0] > 0.5: 
			count += 1
print("Success rate of CW on KNN: " + str(round(count/(total*0.01), 2)) + "%")

# Random Forest

pred = model_randomforest.predict(X_test)
adv_pred = model_randomforest.predict(adv_mim)
count = 0
total = 0
for i in range(len(X_test)):
	if pred[i][0] < 0.5:
		total += 1
		if adv_pred[i][0] > 0.5: 
			count += 1
print("Success rate of MIM on Random Forest: " + str(round(count/(total*0.01), 2)) + "%")

adv_pred = model_randomforest.predict(adv_cw)
count = 0
total = 0
for i in range(len(X_test)):
	if pred[i][0] < 0.5:
		total += 1
		if adv_pred[i][0] > 0.5: 
			count += 1
print("Success rate of CW on Random Forest: " + str(round(count/(total*0.01), 2)) + "%")

# DNN

pred = model_dnn.predict(X_test)
adv_pred = model_dnn.predict(adv_mim)
count = 0
total = 0
for i in range(len(X_test)):
	if pred[i][0] < 0.5:
		total += 1
		if adv_pred[i][0] > 0.5: 
			count += 1
print("Success rate of MIM on DNN: " + str(round(count/(total*0.01), 2)) + "%")

adv_pred = model_dnn.predict(adv_cw)
count = 0
total = 0
for i in range(len(X_test)):
	if pred[i][0] < 0.5:
		total += 1
		if adv_pred[i][0] > 0.5: 
			count += 1
print("Success rate of CW on DNN: " + str(round(count/(total*0.01), 2)) + "%")

# CNN

pred = model_cnn.predict(tf.reshape(X_test, (X_test.shape[0], 10, 1)))
adv_mim_ = tf.reshape(adv_mim, (adv_mim.shape[0], 10, 1))
adv_pred = model_cnn.predict(adv_mim_)
count = 0
total = 0
for i in range(len(X_test)):
	if pred[i][0] < 0.5:
		total += 1
		if adv_pred[i][0] > 0.5: 
			count += 1
print("Success rate of MIM on CNN: " + str(round(count/(total*0.01), 2)) + "%")

adv_cw_ = tf.reshape(adv_cw, (adv_cw.shape[0], 10, 1))
adv_pred = model_cnn.predict(adv_cw_)
count = 0
total = 0
for i in range(len(X_test)):
	if pred[i][0] < 0.5:
		total += 1
		if adv_pred[i][0] > 0.5: 
			count += 1
print("Success rate of CW on CNN: " + str(round(count/(total*0.01), 2)) + "%")

# LSTM

pred = model_lstm.predict(tf.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1)))
adv_mim_ = tf.reshape(adv_mim, (adv_mim.shape[0], adv_mim.shape[1], 1))
adv_pred = model_lstm.predict(adv_mim_)
count = 0
total = 0
for i in range(len(X_test)):
	if pred[i][0] < 0.5:
		total += 1
		if adv_pred[i][0] > 0.5: 
			count += 1
print("Success rate of MIM on LSTM: " + str(round(count/(total*0.01), 2)) + "%")

adv_cw_ = tf.reshape(adv_cw, (adv_cw.shape[0], adv_cw.shape[1], 1))
adv_pred = model_lstm.predict(adv_cw_)
count = 0
total = 0
for i in range(len(X_test)):
	if pred[i][0] < 0.5:
		total += 1
		if adv_pred[i][0] > 0.5: 
			count += 1
print("Success rate of CW on LSTM: " + str(round(count/(total*0.01), 2)) + "%")