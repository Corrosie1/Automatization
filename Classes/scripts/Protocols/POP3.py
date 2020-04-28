import os
import sys
from testing.test import *
from Settings.Settings import *

shell = os.system

class POP3:
    def __init__(self, ip, outputDir, port):
        POP = "/110_POP"
        #
        self.ip = ip
        self.port = port
        self.outputDir = "{}{}{}".format(outputDir, ip, POP)
        #
        Test().exist_outputDir(self.outputDir)
        #
        if len(sys.argv) > 2 and sys.argv[2] == str("--batch"):
            # 1 - info
            self.popInfo()

            # 2 - NMAP - POP3
            Test().continueOrWait()
            self.popNmap()

            if enableBrute == str("yes"):
                # 3 - HYDRA - POP3
                Test().continueOrWait()
                self.popHydra()

    def popNmap(self):
        NMAP = "/NMAP"
        output = "{}{}".format(self.outputDir, NMAP)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- nmap -p {} -sV {} -oN {}/nmap-version-POP3.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} {} --script=pop3-capabilities -oN {}/nmap-capabilities.txt".format(self.port, self.ip, output))

    def popHydra(self):
        HYDRA = "/HYDRA"
        output = "{}{}".format(self.outputDir, HYDRA)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- hydra -l {} -P {} pop3://{}:{}/ -o {}/Hydra-Bruteforce-POP3.txt".format(POP_name, POP_Passwords, self.ip, self.port, output))

    def popInfo(self):
        print("{}[*]{} Don't forget to try and make use of the following tools in {} metasploit {}, they might give you more information".format(green, reset, red, reset))
        print("{}[*]{}      - 'auxiliary/scanner/pop3/pop3_login' ".format(green, reset))
        print("{}[*]{}      - 'auxiliary/scanner/pop3/pop3_version' ".format(green, reset))
        print("{}[*]{} This might also come in handy :)".format(green, reset))
        print("{}[*]{}      - 'https://book.hacktricks.xyz/pentesting/pentesting-pop' ".format(green, reset))

