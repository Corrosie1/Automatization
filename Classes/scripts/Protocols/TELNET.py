import os
import sys
from testing.test import *
from Settings.Settings import *

shell = os.system

class TELNET:
    def __init__(self, ip, outputDir, port):
        TELNET = "/23_TELNET"
        self.ip = ip
        self.port = port
        self.outputDir = "{}{}{}".format(outputDir, ip, TELNET)
        #
        Test().exist_outputDir(self.outputDir)

        if len(sys.argv) > 2 and sys.argv[2] == str("--batch"):

            # 1 - Nmap - Telnet
            Test().continueOrWait()
            self.telnetNmap()

            if enableBrute == str("yes"):
                # 2 - Hydra - Telnet
                Test().continueOrWait()
                self.telnetHydra()

        #############
        ## BATCH ^ ##
        #############

    def telnetNmap(self):
        NMAP = "/NMAP"
        output = "{}{}".format(self.outputDir, NMAP)
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- nmap -p {} -sV {} -oN {}/nmap-version.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} {} --script=telnet-encryption -oN {}/nmap-encryption.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} {} --script=telnet-ntlm-info -oN {}/nmap-ntlm-info.txt".format(self.port, self.ip, output))

    def telnetHydra(self):
        HYDRA = "/HYDRA"
        output = "{}{}".format(self.outputDir, HYDRA)
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- hydra -l {} -P {} telnet://{}:{}/ -o {}/Hydra-bruteforce.txt".format(Telnet_name, Telnet_Passwords, self.ip, self.port, output))