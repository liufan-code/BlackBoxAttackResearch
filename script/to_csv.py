# -*- coding: utf-8 -*-

from data_parser import DataParser
from pandas import DataFrame

def getFeatures(pre, name, n):

	# data_tls = []
	# data_dist = []
	# data_len = []
	# data_ipt = []
	# data_metadata = []
	data_iptseq = []

	for i in range(n):
 		filename = "/root/WorkPlace/" + pre + "_json/" + pre + "_" + name + "_" + str(i+1) + ".json"
 		parser = DataParser(filename)
 		# data_tls += parser.getTLSInfo()
 		# data_dist += parser.getByteDistribution()
 		# data_len += parser.getIndividualFlowPacketLengths()
 		# data_ipt += parser.getIndividualFlowIPTs()
 		# data_metadata += parser.getIndividualFlowMetadata()
 		data_lenseq += parser.getIndividualFlowPacketLengths_seq()
 		# data_iptseq += parser.getIndividualFlowIPTs_seq()

 	# print pre + "_" + name
 	# print "tls: [" + str(len(data_tls[0])) + ", " + str(len(data_tls)) + "]"
 	# pd_tls = DataFrame(data_tls)
 	# pd_tls.to_csv("/root/WorkPlace/" + pre + "_csv/" + pre + "_" + name + "_tls.csv")
 	# print "dist: [" + str(len(data_dist[0])) + ", " + str(len(data_dist)) + "]"
 	# pd_dist = DataFrame(data_dist)
 	# pd_dist.to_csv("/root/WorkPlace/" + pre + "_csv/" + pre + "_" + name + "_dist.csv")
 	# print "len: [" + str(len(data_len[0])) + ", " + str(len(data_len)) + "]"
 	# pd_len = DataFrame(data_len)
 	# pd_len.to_csv("/root/WorkPlace/" + pre + "_csv/" + pre + "_" + name + "_len.csv")
 	# print "ipt: [" + str(len(data_ipt[0])) + ", " + str(len(data_ipt)) + "]"
 	# pd_ipt = DataFrame(data_ipt)
 	# pd_ipt.to_csv("/root/WorkPlace/" + pre + "_csv/" + pre + "_" + name + "_ipt.csv")
 	# print "metadata: [" + str(len(data_metadata[0])) + ", " + str(len(data_metadata)) + "]"
 	# pd_metadata = DataFrame(data_metadata)
 	# pd_metadata.to_csv("/root/WorkPlace/" + pre + "_csv/" + pre + "_" + name + "_metadata.csv")
 	print "lenseq: [" + str(len(data_lenseq[0])) + ", " + str(len(data_lenseq)) + "]"
 	pd_lenseq = DataFrame(data_lenseq)
 	pd_lenseq.to_csv("/root/WorkPlace/" + pre + "_csv/" + pre + "_" + name + "_lenseq_50.csv")

getFeatures("ori", "browsing", 9)
getFeatures("ori", "email", 4)
getFeatures("ori", "chat", 10)
getFeatures("ori", "streaming", 8)
getFeatures("ori", "file", 3)
getFeatures("ori", "voip", 6)
getFeatures("ori", "p2p", 4)
getFeatures("tor", "browsing", 6)
getFeatures("tor", "email", 4)
getFeatures("tor", "chat", 10)
getFeatures("tor", "streaming", 8)
getFeatures("tor", "file", 3)
getFeatures("tor", "voip", 6)
getFeatures("tor", "p2p", 4)