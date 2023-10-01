# -*- coding: utf-8 -*-

from tensorflow.keras.models import load_model
from tensorflow.keras import Model
from momentum_iterative_method import momentum_iterative_method
from carlini_wagner_l2 import carlini_wagner_l2
import numpy as np
import pandas as pd
import tensorflow as tf
from pandas import DataFrame

X_test = pd.read_csv("E://WorkPlace/black_csv/X_test.csv", index_col=0).values.astype("float32")
X_test_lstm = tf.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

model = load_model("E://WorkPlace/model/lstm_substitute.h5")
logits_model = Model(model.input, model.layers[-1].output)

# MIM Method

mim_params = {"norm": np.inf, "eps": 25, "eps_iter": 1, "nb_iter": 1000, "clip_min": 0.0, "clip_max": 200.0, "sanity_checks": False}
adv_x = momentum_iterative_method(logits_model, X_test_lstm, **mim_params)
adv_pred = model.predict(adv_x)

pd_adv_x = DataFrame(tf.reshape(adv_x, (X_test.shape[0], X_test.shape[1])).numpy())
pd_adv_x.to_csv("E://WorkPlace/black_csv/adv_lstm_mim.csv")

pred = model.predict(X_test_lstm)
count = 0
total = 0
for i in range(len(X_test)):
	if pred[i][0] < 0.5:
		total += 1
		if adv_pred[i][0] > 0.5: 
			count += 1
print("Success rate of MIM: " + str(round(count/(total*0.01), 2)) + "%")

# CW Method

cw_params = {"clip_min": 0.0, "clip_max": 200.0}
adv_x = carlini_wagner_l2(logits_model, X_test_lstm, **cw_params)
adv_pred = model.predict(adv_x)

pd_adv_x = DataFrame(tf.reshape(adv_x, (X_test.shape[0], X_test.shape[1])).numpy())
pd_adv_x.to_csv("E://WorkPlace/black_csv/adv_lstm_cw.csv")

pred = model.predict(X_test_lstm)
count = 0
total = 0
for i in range(len(X_test)):
	if pred[i][0] < 0.5:
		total += 1
		if adv_pred[i][0] > 0.5: 
			count += 1
print("Success rate of CW: " + str(round(count/(total*0.01), 2)) + "%")