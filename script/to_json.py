# -*- coding: utf-8 -*-

import subprocess

def unzip(pre, name, n):

    for i in range(n):
        filename = "/root/WorkPlace/" + pre + "_json/" + pre + "_" + name + "_" + str(i+1) + ".json.gz"
        print(filename)
        subprocess.Popen(["gzip", "-d", filename])

# unzip("ori", "browsing", 9)
# unzip("ori", "email", 4)
# unzip("ori", "chat", 10)
# unzip("ori", "streaming", 8)
# unzip("ori", "file", 3)
# unzip("ori", "voip", 6)
# unzip("ori", "p2p", 4)
# unzip("tor", "browsing", 6)
# unzip("tor", "email", 4)
# unzip("tor", "chat", 10)
# unzip("tor", "streaming", 8)
# unzip("tor", "file", 3)
# unzip("tor", "voip", 6)
# unzip("tor", "p2p", 4)
# unzip("tls", "browsing", 9)
# unzip("tls", "email", 4)
# unzip("tls", "chat", 8)
# unzip("tls", "streaming", 7)
# unzip("tls", "file", 1)
# unzip("tls", "voip", 6)
unzip("tortls", "browsing", 5)
unzip("tortls", "email", 4)
unzip("tortls", "chat", 5)
unzip("tortls", "streaming", 7)
unzip("tortls", "file", 3)
unzip("tortls", "voip", 6)
unzip("tortls", "p2p", 4)