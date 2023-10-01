# -*- coding: utf-8 -*-

from tensorflow.keras.models import load_model
from tensorflow.keras import Model
from momentum_iterative_method_1 import momentum_iterative_method
import numpy as np
import pandas as pd
import tensorflow as tf

# X_test = np.empty(shape=(0, 10))
# names = ["browsing", "email", "chat", "streaming", "file", "voip", "p2p"]

# for name in names:
    
#     data = pd.read_csv("E://WorkPlace/tor_csv/tor_" + name + "_lenseq.csv", nrows=100, index_col=0)
#     _X_test = data.values
#     X_test = np.vstack((X_test, _X_test)).astype("float32")

# X_test = tf.reshape(X_test, (X_test.shape[0], 10, 1))
# X_test = tf.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

X_test = pd.read_csv("E://WorkPlace/black_csv/X_test.csv", index_col=0).values.astype("float32")
X_test = tf.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

model = load_model("E://WorkPlace/model/lstm_black.h5")
logits_model = Model(model.input, model.layers[-1].output)

eps = range(25, 26)
for e in eps:
	mim_params = {"norm": np.inf, "eps": e, "eps_iter": 21, "nb_iter": 1000, "clip_min": 0.0, "clip_max": 200.0, "sanity_checks": False}
	adv_x = momentum_iterative_method(logits_model, X_test, **mim_params)
	adv_pred = model.predict(adv_x)
	pred = model.predict(X_test)
	count = 0
	total = 0
	for i in range(len(X_test)):
		if pred[i][0] < 0.5:
			total += 1
			if adv_pred[i][0] > 0.5: 
				count += 1
	print("EPS: " + str(e))
	print("Success rate: " + str(round(count/(total*0.01), 2)) + "%")