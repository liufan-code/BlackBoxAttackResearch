# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from pandas import DataFrame

def getData(names):

	X = np.empty(shape=(0, 10))
	y = []
	rows_1 = [2000, 1225, 967, 2000, 2814, 2000, 2000]
	rows_2 = [1797, 208, 273, 1725, 598, 1559, 1484]

	for i, name in enumerate(names):

		if rows_1[i] != 0:
			data = pd.read_csv("/root/WorkPlace/ori_csv/ori_" + name + "_lenseq.csv", nrows=rows_1[i], index_col=0)
			_X = data.values
			X = np.vstack((X, _X))
			y += [[1, 0]] * rows_1[i]

		if rows_2[i] != 0:
			data = pd.read_csv("/root/WorkPlace/tor_csv/tor_" + name + "_lenseq.csv", nrows=rows_2[i], index_col=0)
			_X = data.values
			X = np.vstack((X, _X))
			y += [[0, 1]] * rows_2[i]

	X, y = shuffle(X, y)
	return X, y

names = ["browsing", "email", "chat", "streaming", "file", "voip", "p2p"]
X, y = getData(names)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.1)
X_train_1, X_train_2, y_train_1, y_train_2 = train_test_split(X_train, y_train, test_size=.3)

pd_X_train_1 = DataFrame(X_train_1)
pd_X_train_2 = DataFrame(X_train_2)
pd_X_test = DataFrame(X_test)

pd_y_train_1 = DataFrame(y_train_1)
pd_y_train_2 = DataFrame(y_train_2)
pd_y_test = DataFrame(y_test)

pd_X_train_1.to_csv("/root/WorkPlace/black_csv/X_train_1.csv")
pd_X_train_2.to_csv("/root/WorkPlace/black_csv/X_train_2.csv")
pd_X_test.to_csv("/root/WorkPlace/black_csv/X_test.csv")

pd_y_train_1.to_csv("/root/WorkPlace/black_csv/y_train_1.csv")
pd_y_train_2.to_csv("/root/WorkPlace/black_csv/y_train_2.csv")
pd_y_test.to_csv("/root/WorkPlace/black_csv/y_test.csv")