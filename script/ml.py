# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import cross_val_predict
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

def getData(names, seq_len):

	X = np.empty(shape=(0, seq_len))
	y = []
	rows_0 = [1797, 1725, 1484]
	rows_1 = [2000, 1225, 967, 2000, 2814, 2000, 2000]
	rows_2 = [1797, 208, 273, 1725, 598, 1559, 1484]

	for i, name in enumerate(names):

		# if rows_0[i] != 0:
		# 	data = pd.read_csv("/root/WorkPlace/tor_csv/tor_" + name + "_lenseq_50.csv", nrows=rows_0[i], usecols=range(seq_len+1), index_col=0)
		# 	_X = data.values
		# 	X = np.vstack((X, _X))
		# 	y += [i] * rows_0[i]

		if rows_1[i] != 0:
			data = pd.read_csv("/root/WorkPlace/ori_csv/ori_" + name + "_lenseq_50.csv", nrows=rows_1[i], usecols=range(seq_len+1), index_col=0)
			_X = data.values
			X = np.vstack((X, _X))
			y += [1] * rows_1[i]

		if rows_2[i] != 0:
			data = pd.read_csv("/root/WorkPlace/tor_csv/tor_" + name + "_lenseq_50.csv", nrows=rows_2[i], usecols=range(seq_len+1), index_col=0)
			_X = data.values
			X = np.vstack((X, _X))
			y += [0] * rows_2[i]

	# model_smote = SMOTE()
	# X, y = model_smote.fit_sample(X, y)
	X, y = shuffle(X, y)
	return X, y

# names = ["browsing", "streaming", "p2p"]
names = ["browsing", "email", "chat", "streaming", "file", "voip", "p2p"]
# X, y = getData(names)

model_1 = GaussianNB()
model_2 = KNeighborsClassifier()
model_3 = tree.DecisionTreeClassifier()
model_4 = RandomForestClassifier(n_estimators=10, random_state=0)
model_5 = LinearSVC(C=0.1, max_iter=1000, random_state=0)

models = [model_2, model_4]

# for model in models:
# 	y_pred = cross_val_predict(model, X, y, cv=10)
# 	print("accuracy: " + str(accuracy_score(y, y_pred)))
	# print("metrics: ")
	# print(confusion_matrix(y, y_pred))
	# print("precision: " + str(precision_score(y, y_pred)))
	# print("recall: " + str(recall_score(y, y_pred)))
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 25, 50]
for l in ls:
	seq_len = l
	print("seq_len: " + str(seq_len))
	X, y = getData(names, seq_len)
	for model in models:
		y_pred = cross_val_predict(model, X, y, cv=10)
		print("accuracy: " + str(accuracy_score(y, y_pred)))