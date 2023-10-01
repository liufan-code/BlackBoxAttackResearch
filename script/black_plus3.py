# -*- coding: utf-8 -*-

from tensorflow.keras.models import load_model
import pandas as pd
import tensorflow as tf
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC

adv_mim = pd.read_csv("E://WorkPlace/black_plus_csv/adv_lstm_mim_tran.csv", index_col=0).values.astype("float32")

X_train = pd.read_csv("E://WorkPlace/black_plus_csv/X_train_1_.csv", index_col=0).values.astype("float32")
y_train = pd.read_csv("E://WorkPlace/black_plus_csv/y_train_1_.csv", index_col=0).values.astype("float32")

y_train_svm = y_train[...,0]

model_knn = KNeighborsClassifier().fit(X_train, y_train)
model_randomforest = RandomForestClassifier(n_estimators=10, random_state=0).fit(X_train, y_train)
model_svm = LinearSVC(C=0.1, max_iter=1000, random_state=0).fit(X_train, y_train_svm)
model_dnn = load_model("E://WorkPlace/model/dnn_tran.h5")
model_cnn = load_model("E://WorkPlace/model/cnn_tran.h5")
model_lstm = load_model("E://WorkPlace/model/lstm_tran.h5")

X_test = pd.read_csv("E://WorkPlace/black_plus_csv/X_test_.csv", index_col=0).values.astype("float32")
y_test = pd.read_csv("E://WorkPlace/black_plus_csv/y_test_.csv", index_col=0).values.astype("float32")

# KNN

pred = model_knn.predict(X_test)
adv_pred = model_knn.predict(adv_mim)
count = 0
total = 0
for i in range(len(X_test)):
	if pred[i][0] < 0.5:
		total += 1
		if adv_pred[i][0] > 0.5 and y_test[i][0] < 0.5: 
			count += 1
print("Success rate of MIM on KNN: " + str(round(count/(total*0.01), 2)) + "%")

# Random Forest

pred = model_randomforest.predict(X_test)
adv_pred = model_randomforest.predict(adv_mim)
count = 0
total = 0
for i in range(len(X_test)):
	if pred[i][0] < 0.5:
		total += 1
		if adv_pred[i][0] > 0.5 and y_test[i][0] < 0.5: 
			count += 1
print("Success rate of MIM on Random Forest: " + str(round(count/(total*0.01), 2)) + "%")

# SVM

pred = model_svm.predict(X_test)
adv_pred = model_svm.predict(adv_mim)
count = 0
total = 0
for i in range(len(X_test)):
	if pred[i] < 0.5:
		total += 1
		if adv_pred[i] > 0.5 and y_test[i][0] < 0.5: 
			count += 1
print("Success rate of MIM on SVM: " + str(round(count/(total*0.01), 2)) + "%")

# DNN

pred = model_dnn.predict(X_test)
adv_pred = model_dnn.predict(adv_mim)
count = 0
total = 0
for i in range(len(X_test)):
	if pred[i][0] < 0.5:
		total += 1
		if adv_pred[i][0] > 0.5 and y_test[i][0] < 0.5: 
			count += 1
print("Success rate of MIM on DNN: " + str(round(count/(total*0.01), 2)) + "%")

# CNN

pred = model_cnn.predict(tf.reshape(X_test, (X_test.shape[0], 100, 1)))
adv_mim_ = tf.reshape(adv_mim, (adv_mim.shape[0], 100, 1))
adv_pred = model_cnn.predict(adv_mim_)
count = 0
total = 0
for i in range(len(X_test)):
	if pred[i][0] < 0.5:
		total += 1
		if adv_pred[i][0] > 0.5 and y_test[i][0] < 0.5: 
			count += 1
print("Success rate of MIM on CNN: " + str(round(count/(total*0.01), 2)) + "%")

# LSTM

pred = model_lstm.predict(tf.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1)))
adv_mim_ = tf.reshape(adv_mim, (adv_mim.shape[0], adv_mim.shape[1], 1))
adv_pred = model_lstm.predict(adv_mim_)
count = 0
total = 0
for i in range(len(X_test)):
	if y_test[i][0] < 0.5:
		total += 1
		if adv_pred[i][0] > 0.5: 
			count += 1
print("Success rate of MIM on LSTM: " + str(round(count/(total*0.01), 2)) + "%")