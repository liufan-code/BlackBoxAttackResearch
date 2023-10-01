# -*- coding: utf-8 -*-

from tensorflow.keras.models import load_model
from tensorflow.keras import Model
from momentum_iterative_method import momentum_iterative_method
from carlini_wagner_l2_1 import carlini_wagner_l2
import numpy as np
import pandas as pd
import tensorflow as tf
from pandas import DataFrame

def getTranMatrix(flows):

	data = []
	numRows = 10
	tranMat = np.zeros((numRows,numRows))

	for flow in flows:
		for i in range(1, len(flow)):
			prevPacketSize = min(int(flow[i-1]), numRows-1)
			curPacketSize = min(int(flow[i]), numRows-1)
			tranMat[prevPacketSize,curPacketSize] += 1
			for i in range(numRows):
				if float(np.sum(tranMat[i:i+1])) != 0:
					tranMat[i:i+1] = tranMat[i:i+1]/float(np.sum(tranMat[i:i+1]))

		data.append(list(tranMat.flatten()))

	return data

X_test = pd.read_csv("E://WorkPlace/black_plus_csv/X_test.csv", index_col=0).values.astype("float32")
X_test = tf.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

model = load_model("E://WorkPlace/model/lstm_seq.h5")
logits_model = Model(model.input, model.layers[-1].output)

mim_params = {"norm": np.inf, "eps": 25, "eps_iter": 1, "nb_iter": 1000, "clip_min": 0.0, "clip_max": 200.0, "sanity_checks": False}
adv_x = momentum_iterative_method(logits_model, X_test, **mim_params)
adv_x = tf.reshape(adv_x, (X_test.shape[0], X_test.shape[1])).numpy()
adv_x_tran = getTranMatrix(adv_x) 
pd_adv_x = DataFrame(adv_x_tran)
pd_adv_x.to_csv("E://WorkPlace/black_plus_csv/adv_lstm_mim_tran.csv")