# -*- coding: utf-8 -*-

import subprocess
import os

os.chdir("/root/joy/")

def joy(pre, name, n):

	options = ["dist=1", "entropy=1", "tls=1", "dns=1", "http=1"]

	for i in range(n):
		filename = "/root/WorkPlace/" + pre + "_dataset/" + pre + "_" + name + "_" + str(i+1) + ".pcap"
		print(filename)
		output = "output=../WorkPlace/" + pre + "_json/" + pre + "_" + name + "_" + str(i+1) + ".json.gz"
		subprocess.Popen(["bin/joy"] + options + [output, filename])

# joy("ori", "browsing", 9)
# joy("ori", "email", 4)
# joy("ori", "chat", 10)
# joy("ori", "streaming", 8)
# joy("ori", "file", 3)
# joy("ori", "voip", 6)
# joy("ori", "p2p", 4)
# joy("tor", "browsing", 6)
# joy("tor", "email", 4)
# joy("tor", "chat", 10)
# joy("tor", "streaming", 8)
# joy("tor", "file", 3)
# joy("tor", "voip", 6)
# joy("tor", "p2p", 4)
# joy("tls", "browsing", 9)
# joy("tls", "email", 4)
# joy("tls", "chat", 8)
# joy("tls", "streaming", 7)
# joy("tls", "file", 1)
# joy("tls", "voip", 6)
joy("tortls", "browsing", 5)
joy("tortls", "email", 4)
joy("tortls", "chat", 5)
joy("tortls", "streaming", 7)
joy("tortls", "file", 3)
joy("tortls", "voip", 6)
joy("tortls", "p2p", 4)