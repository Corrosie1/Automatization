from testing.test import *
from Settings.Settings import *
#
import os
import sys
#
shell = os.system

class FTP:
    def __init__(self, ip, outputDir, port):
        FTP = "/21_FTP"
        self.ip = ip
        self.port = port
        self.outputDir = "{}{}{}".format(outputDir, ip, FTP)
        #
        Test().exist_outputDir(self.outputDir)

        if len(sys.argv) > 2 and sys.argv[2] == str("--batch"):

            # 1 - NMAP - FTP
            Test().continueOrWait()
            self.ftpNmap()

            if enableBrute == str("yes"):
                # 2 - HYDRA - FTP
                Test().continueOrWait()
                self.ftpHydra()

        #############
        ## BATCH ^ ##
        #############

    def ftpNmap(self):
        NMAP = "/NMAP"
        output = "{}{}".format(self.outputDir, NMAP)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- nmap -p {} --script=ftp-anon {} -oN {}/nmap-anon-FTP.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} -sV {} -oN {}/nmap-version-FTP.txt".format(self.port, self.ip, output))

    def ftpHydra(self):
        HYDRA = "/HYDRA"
        output = "{}{}".format(self.outputDir, HYDRA)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- hydra -l {} -P {} ftp://{}:{}/ -o {}/Hydra-Bruteforce-FTP.txt ".format(FTP_name, FTP_Passwords, self.ip, self.port, output))