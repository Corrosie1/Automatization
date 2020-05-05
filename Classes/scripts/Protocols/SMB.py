import os
import sys
from testing.test import *
from Settings.Settings import *

shell = os.system

class SMB:
    def __init__(self, ip, outputDir, port):
        #
        SMB = "/445_SMB"
        #
        self.ip = ip
        self.port = port
        self.outputDir = "{}{}{}".format(outputDir, ip, SMB)
        #
        Test().exist_outputDir(self.outputDir)
        #
        if len(sys.argv) > 2 and sys.argv[2] == str("--batch"):
            #
            Test().continueOrWait()
            self.nmapSmb()
            #
            Test().continueOrWait()
            self.smbInfo()

    def nmapSmb(self):
        nmap = "/nmap"
        output = "{}{}".format(self.outputDir, nmap)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- nmap -p {} --script=smb-enum-* {} -oN {}/nmap-smb-enum.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} --script=smb-os-discovery -oN {}/nmap-os-discovery.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} --script=smb-p* -oN {}/nmap-protocols-print.txt".format(self.port, self.ip, output))
        shell("gnome-temrinal -q -- nmap -p {} --script=smb-s* -oN {}/nmap-system-server-security.txt".format(self.port, self.ip, output))

    def smbInfo(self):
        print("{}[*]{} Checkout the following URL for further explanation on pentesting SMB".format(green, reset))
        print("{}[+]{} - https://book.hacktricks.xyz/pentesting/pentesting-smb".format(brightGreen, reset))
        print("{}[*]{} Try one or more of the following modules in metasploit if nmap results are false".format(green, reset))
        print("{}[+]{} - auxiliary/scanner/smb/smb_enumshares".format(brightGreen, reset))
        print("{}[+]{} - auxiliary/scanner/smb/smb_enumusers".format(brightGreen, reset))
        print("{}[+]{} - auxiliary/scanner/smb/smb_enumusers_domain".format(brightGreen, reset))
        print("{}[+]{} - auxiliary/scanner/smb/smb_lookupsid".format(brightGreen, reset))
        print("{}[+]{} - auxiliary/scanner/smb/smb_version".format(brightGreen, reset))