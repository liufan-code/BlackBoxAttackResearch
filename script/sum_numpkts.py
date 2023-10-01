# -*- coding: utf-8 -*-

import json

def sum_numpkts(pre, name, n):

	total = 0
	for i in range(n):
		filename = "E://WorkPlace/" + pre + "_json/" + pre + "_" + name + "_" + str(i+1) + ".json"
		print(filename)
		with open(filename, "r") as f:
			f.readline()
			while True:
				try:
					line = f.readline()
					if not line:
						break
					d = json.loads(json.loads(json.dumps(line)))
					num_pkts = d["num_pkts_out"]
					total += num_pkts
				except:
					pass
		f.close()
	print(str(total))

sum_numpkts("ori", "browsing", 9)
sum_numpkts("ori", "email", 4)
sum_numpkts("ori", "chat", 10)
sum_numpkts("ori", "streaming", 8)
sum_numpkts("ori", "file", 3)
sum_numpkts("ori", "voip", 6)
sum_numpkts("ori", "p2p", 4)
sum_numpkts("tor", "browsing", 6)
sum_numpkts("tor", "email", 4)
sum_numpkts("tor", "chat", 10)
sum_numpkts("tor", "streaming", 8)
sum_numpkts("tor", "file", 3)
sum_numpkts("tor", "voip", 6)
sum_numpkts("tor", "p2p", 4)