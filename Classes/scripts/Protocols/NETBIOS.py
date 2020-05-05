import sys
from testing.test import *
from Settings.Settings import *

shell = os.system

class NETBIOS:
    def __init__(self, ip, outputDir, port):
        NETBIOS = "/139_NETBIOS"
        #
        self.ip = ip
        self.port = port
        self.outputDir = "{}{}{}".format(outputDir, ip, NETBIOS)
        #
        Test().exist_outputDir(self.outputDir)
        #
        if len(sys.argv) > 2 and sys.argv[2] == str("--batch"):

            # 1 - nbtscan
            Test().continueOrWait()
            self.nbtScan()

            # 2 - nmap
            Test().continueOrWait()
            self.netbiosNmap()

            # 3 - info
            Test().continueOrWait()
            self.info()

    def nbtScan(self):
        nbt = "/nbtscan"
        output = "{}{}".format(self.outputDir, nbt)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- bash -c 'nbtscan -r {} | tee {}/nbtscan.txt'".format(self.ip, output))

    def netbiosNmap(self):
        nmap = "/nmap"
        output = "{}{}".format(self.outputDir, nmap)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- nmap -p {} --script=broadcast-netbios-master-browser.nse {} -oN {}/broadcast-netbios-master-browser.txt".format(self.port, self.ip, output))

    def info(self):
        print("{}[*]{} For recon, you could try the following Metasploit tool:".format(green, reset))
        print("{}[+]{} - auxiliary/scanner/smb/smb_version".format(brightGreen, reset))
        print("{}[*]{} For ideas on further exploitation, try the following URL:".format(green, reset))
        print("{}[+]{} - https://book.hacktricks.xyz/pentesting/pentesting-smb".format(brightGreen, reset))