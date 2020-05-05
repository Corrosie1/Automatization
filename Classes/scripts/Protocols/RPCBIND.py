import os
import sys
from testing.test import *
from Settings.Settings import *

shell = os.system

class RPCBIND:
    def __init__(self, ip, outputDir, port):
        RPC = "/111_RPC"
        #
        self.ip = ip
        self.port = port
        self.outputDir = "{}{}{}".format(outputDir, ip, RPC)
        #
        Test().exist_outputDir(self.outputDir)
        #
        if len(sys.argv) > 2 and sys.argv[2] == str("--batch"):
            Test().continueOrWait()
            self.rpcInfo()

            Test().continueOrWait()
            self.rpcNmap()

    def rpcInfo(self):
        rpc = "/rpcInfo"
        output = "{}{}".format(self.outputDir, rpc)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- bash -c 'rpcinfo {} > {}/rpcInfo.txt'".format(self.ip, output))
        print("{}[*]{} Checkout the following URL for further exploitaiton on rpcbind : ".format(green, reset, cyan, reset))
        print("{}[+]{} - https://book.hacktricks.xyz/pentesting/pentesting-rpcbind".format(brightGreen, reset))

    def rpcNmap(self):
        nmap = "/nmap"
        output = "{}{}".format(self.outputDir, nmap)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- nmap -sSUC -p 111 {} -oN {}/rpcNmap.txt".format(self.ip, output))
