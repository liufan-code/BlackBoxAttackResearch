# -*- coding: utf-8 -*-

import subprocess

def tshark(name, n):

	for i in range(n):
		readfile = "/root/WorkPlace/ori_dataset/ori_" + name + "_" + str(i+1) + ".pcap"
		print(readfile)
		outfile = "/root/WorkPlace/tls_dataset/tls_" + name + "_" + str(i+1) + ".pcap"
		subprocess.Popen(["tshark", "-r", readfile, "-Y", "tls", "-w", outfile])

tshark("browsing", 1)
tshark("email", 4)
tshark("chat", 10)
tshark("streaming", 1)
tshark("file", 3)
tshark("voip", 2)