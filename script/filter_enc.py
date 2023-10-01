# -*- coding: utf-8 -*-

import pandas as pd

def del_unenc_records(name):

	data_dist = pd.read_csv("/root/WorkPlace/ori_csv/ori_" + name + "_dist.csv", index_col=0)
	data_dist_enc = data_dist
	data_dist_unenc = data_dist
	data_ipt_unenc = pd.read_csv("/root/WorkPlace/ori_csv/ori_" + name + "_ipt.csv", index_col=0)
	data_len_unenc = pd.read_csv("/root/WorkPlace/ori_csv/ori_" + name + "_len.csv", index_col=0)
	# data_ipt = pd.read_csv("/root/WorkPlace/ori_csv/ori_" + name + "_ipt.csv", index_col=0)
	# data_len = pd.read_csv("/root/WorkPlace/ori_csv/ori_" + name + "_len.csv", index_col=0)

	for i in range(data_dist.shape[0]):

		dist = data_dist.loc[i]

		x = 1
		for j in range(len(dist)):
			x *= 1000*dist[j]
			if x == 0:
				data_dist_enc = data_dist_enc.drop(index=i)
				# data_ipt = data_ipt.drop(index=i)
				# data_len = data_len.drop(index=i)
				break
		if x != 0:
			data_dist_unenc = data_dist_unenc.drop(index=i)
			data_ipt_unenc = data_ipt_unenc.drop(index=i)
			data_len_unenc = data_len_unenc.drop(index=i)
			print("Enc " + name + "'s " + str(i))

	# data_ipt.to_csv("/root/WorkPlace/enc_csv/enc_" + name + "_ipt.csv")
	# data_len.to_csv("/root/WorkPlace/enc_csv/enc_" + name + "_len.csv")
	data_dist_enc.to_csv("/root/WorkPlace/enc_csv/enc_" + name + "_dist.csv")
	data_dist_unenc.to_csv("/root/WorkPlace/unenc_csv/unenc_" + name + "_dist.csv")
	data_ipt_unenc.to_csv("/root/WorkPlace/unenc_csv/unenc_" + name + "_ipt.csv")
	data_len_unenc.to_csv("/root/WorkPlace/unenc_csv/unenc_" + name + "_len.csv")

names = ["browsing", "email", "chat", "streaming", "file", "voip", "p2p"]
for name in names:
	print(name)
	del_unenc_records(name)