# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from pandas import DataFrame

def getData(names):

	X = np.empty(shape=(0, 50))
	y = []
	rows_1 = [2000, 1225, 967, 2000, 2814, 2000, 2000]
	rows_2 = [1797, 208, 273, 1725, 598, 1559, 1484]

	for i, name in enumerate(names):

		if rows_1[i] != 0:
			data = pd.read_csv("/root/WorkPlace/ori_csv/ori_" + name + "_lenseq_50.csv", nrows=rows_1[i], index_col=0)
			_X = data.values
			X = np.vstack((X, _X))
			y += [[1, 0]] * rows_1[i]

		if rows_2[i] != 0:
			data = pd.read_csv("/root/WorkPlace/tor_csv/tor_" + name + "_lenseq_50.csv", nrows=rows_2[i], index_col=0)
			_X = data.values
			X = np.vstack((X, _X))
			y += [[0, 1]] * rows_2[i]

	X, y = shuffle(X, y)
	return X, y

names = ["browsing", "email", "chat", "streaming", "file", "voip", "p2p"]
X, y = getData(names)

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

X_ = getTranMatrix(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=.1)
X_train_1, X_train_2, y_train_1, y_train_2 = train_test_split(X_train, y_train, shuffle=False, test_size=.3)
X_train_, X_test_, y_train_, y_test_ = train_test_split(X_, y, shuffle=False, test_size=.1)
X_train_1_, X_train_2_, y_train_1_, y_train_2_ = train_test_split(X_train_, y_train_, shuffle=False, test_size=.3)

pd_X_train_1 = DataFrame(X_train_1)
pd_X_train_2 = DataFrame(X_train_2)
pd_X_test = DataFrame(X_test)
pd_y_train_1 = DataFrame(y_train_1)
pd_y_train_2 = DataFrame(y_train_2)
pd_y_test = DataFrame(y_test)

pd_X_train_1_ = DataFrame(X_train_1_)
pd_X_train_2_ = DataFrame(X_train_2_)
pd_X_test_ = DataFrame(X_test_)
pd_y_train_1_ = DataFrame(y_train_1_)
pd_y_train_2_ = DataFrame(y_train_2_)
pd_y_test_ = DataFrame(y_test_)

pd_X_train_1.to_csv("/root/WorkPlace/black_plus_csv/X_train_1.csv")
pd_X_train_2.to_csv("/root/WorkPlace/black_plus_csv/X_train_2.csv")
pd_X_test.to_csv("/root/WorkPlace/black_plus_csv/X_test.csv")
pd_y_train_1.to_csv("/root/WorkPlace/black_plus_csv/y_train_1.csv")
pd_y_train_2.to_csv("/root/WorkPlace/black_plus_csv/y_train_2.csv")
pd_y_test.to_csv("/root/WorkPlace/black_plus_csv/y_test.csv")

pd_X_train_1_.to_csv("/root/WorkPlace/black_plus_csv/X_train_1_.csv")
pd_X_train_2_.to_csv("/root/WorkPlace/black_plus_csv/X_train_2_.csv")
pd_X_test_.to_csv("/root/WorkPlace/black_plus_csv/X_test_.csv")
pd_y_train_1_.to_csv("/root/WorkPlace/black_plus_csv/y_train_1_.csv")
pd_y_train_2_.to_csv("/root/WorkPlace/black_plus_csv/y_train_2_.csv")
pd_y_test_.to_csv("/root/WorkPlace/black_plus_csv/y_test_.csv")