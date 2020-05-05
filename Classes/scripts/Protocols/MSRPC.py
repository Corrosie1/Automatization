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
        shell("gnome-terminal -q -- nmap -p {} --script=msrpc-enum {} -oN {}/nmap-msrpc.txt".format(self.port, self.ip, output))

    def msrpcInfo(self):
        print("{}[*]{} Try out 1 of the following tools in metasploit : - ".format(green, reset))
        print("{}[+]{} - auxiliary/scanner/dcerpc/endpoint_mapper".format(brightGreen, reset))
        print("{}[+]{} - auxiliary/scanner/dcerpc/hidden".format(brightGreen, reset))
        print("{}[+]{} - auxiliary/scanner/dcerpc/management".format(brightGreen, reset))
        print("{}[+]{} - auxiliary/scanner/dcerpc/tcp_dcerpc_auditor".format(brightGreen, reset))
        print("{}[*]{} Or try out rpcdump.py (impacket) :".format(green, reset))
        print("{}[+]{} - https://github.com/SecureAuthCorp/impacket/blob/master/examples/rpcdump.py".format(brightGreen, reset))
        print("{}[*]{} Explanation on further exploitation can be found here :".format(green, reset, cyan, reset))
        print("{}[+]{} - https://book.hacktricks.xyz/pentesting/135-penstesting-wrpc".format(brightGreen, reset))
