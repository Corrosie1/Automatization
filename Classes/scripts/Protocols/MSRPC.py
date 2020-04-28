import os
import sys
from testing.test import *
from Settings.Settings import *

shell = os.system

class MSRPC:
    def __init__(self, ip, outputDir, port):
        MSRPC = "/135_MSRPC"
        #
        self.ip = ip
        self.port = port
        self.outputDir = "{}{}{}".format(outputDir, ip, MSRPC)
        #
        Test().exist_outputDir(self.outputDir)
        #

        if len(sys.argv) > 2 and sys.argv[2] == str("--batch"):
            #
            self.msrpcInfo()

            # 1 - nmap - MSRPC
            Test().continueOrWait()
            self.nmapMsrpc()

    def nmapMsrpc(self):
        nmap = "/nmap"
        output = "{}{}".format(self.outputDir, nmap)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- nmap -p {} --script=msrpc-enum {}".format(self.port, self.ip))

    def msrpcInfo(self):
        print("{}[*]{} Checkout the following URL for further exploitation on MSRPC : {}https://book.hacktricks.xyz/pentesting/135-penstesting-wrpc{}".format(green, reset, cyan, reset))