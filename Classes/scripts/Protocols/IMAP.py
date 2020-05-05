import os
import sys
from testing.test import *
from Settings.Settings import *

shell = os.system

class IMAP:
    def __init__(self, ip, outputDir, port):
        IMAP = "/143_IMAP"
        #
        self.ip = ip
        self.port = port
        self.outputDir = "{}{}{}".format(outputDir, ip, IMAP)
        #
        Test().exist_outputDir(self.outputDir)
        #
        if len(sys.argv) > 2 and sys.argv[2] == str("--batch"):
            # 1 - info
            self.imapInfo()

            # 2 - NMAP - IMAP
            Test().continueOrWait()
            self.imapNmap()

            if enableBrute == str("yes"):
                # 3 - HYDRA - IMAP
                Test().continueOrWait()
                self.imapHydra()

    def imapNmap(self):
        NMAP = "/NMAP"
        output = "{}{}".format(self.outputDir, NMAP)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- nmap -p {} -sV {} -oN {}/nmap-version-IMAP.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} {} --script=imap-capabilities -oN {}/nmap-capabilities.txt".format(self.port, self.ip, output))

    def imapHydra(self):
        HYDRA = "/HYDRA"
        output = "{}{}".format(self.outputDir, HYDRA)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- hydra -l {} -P {} imap://{}:{}/ -o {}/Hydra-Bruteforce-imap.txt".format(IMAP_name, IMAP_Passwords, self.ip, self.port, output))

    def imapInfo(self):
        print("{}[*]{} Don't forget to try and make use of the following tool in {} metasploit {}, they might give you more information".format(green, reset, red, reset))
        print("{}[+]{} - 'auxiliary/scanner/imap/imap_version' ".format(brightGreen, reset))
        print("{}[*]{} if that does not work, try the command : nc -vn <IP> <PORT>".format(green, reset))
        print("{}[+]{} - for example: {}'nc -vn {} {}'{}, this will work on multiple ports".format(brightGreen, reset, cyan, self.ip, self.port, reset))