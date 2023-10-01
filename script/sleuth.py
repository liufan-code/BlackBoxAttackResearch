# -*- coding: utf-8 -*-

import subprocess
import json
import os

os.chdir("/root/joy/")

def getNum(pre, name, n):
    
    bytes_out = 0
    num_pkts_out = 0

    for i in range(n):
        filename =  "/root/WorkPlace/" + pre + "_json/" + pre + "_" + name + "_" + str(i+1) + ".json.gz"
        args = "bytes_out,num_pkts_out"
        print(filename)
        sleuth = subprocess.Popen(["./sleuth", filename, "--select", args, "--sum", args], stdout=subprocess.PIPE)
        result = sleuth.stdout.readline().strip()
        result = json.loads(result.decode("utf-8"))
        bytes_out += result["bytes_out"]
        num_pkts_out += result["num_pkts_out"]

    return bytes_out,num_pkts_out

bytes_out,num_pkts_out = getNum("ori", "browsing", 9)
print(bytes_out)
print(num_pkts_out)
bytes_out,num_pkts_out = getNum("ori", "email", 4)
print(bytes_out)
print(num_pkts_out)
bytes_out,num_pkts_out = getNum("ori", "chat", 10)
print(bytes_out)
print(num_pkts_out)
bytes_out,num_pkts_out = getNum("ori", "streaming", 8)
print(bytes_out)
print(num_pkts_out)
bytes_out,num_pkts_out = getNum("ori", "file", 3)
print(bytes_out)
print(num_pkts_out)
bytes_out,num_pkts_out = getNum("ori", "voip", 6)
print(bytes_out)
print(num_pkts_out)
bytes_out,num_pkts_out = getNum("ori", "p2p", 4)
print(bytes_out)
print(num_pkts_out)
bytes_out,num_pkts_out = getNum("tor", "browsing", 6)
print(bytes_out)
print(num_pkts_out)
bytes_out,num_pkts_out = getNum("tor", "email", 4)
print(bytes_out)
print(num_pkts_out)
bytes_out,num_pkts_out = getNum("tor", "chat", 10)
print(bytes_out)
print(num_pkts_out)
bytes_out,num_pkts_out = getNum("tor", "streaming", 8)
print(bytes_out)
print(num_pkts_out)
bytes_out,num_pkts_out = getNum("tor", "file", 3)
print(bytes_out)
print(num_pkts_out)
bytes_out,num_pkts_out = getNum("tor", "voip", 6)
print(bytes_out)
print(num_pkts_out)
bytes_out,num_pkts_out = getNum("tor", "p2p", 4)
print(bytes_out)
print(num_pkts_out)