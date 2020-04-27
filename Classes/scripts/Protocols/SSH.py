from testing.test import *
from Settings.Settings import *
#
import os
import sys
#
shell = os.system

class SSH:
    def __init__(self, ip, outputDir, port):
        SSH = "/22_SSH"
        self.ip = ip
        self.port = port
        self.outputDir = "{}{}{}".format(outputDir, ip, SSH)
        #
        Test().exist_outputDir(self.outputDir)

        if len(sys.argv) > 2 and sys.argv[2] == str("--batch"):

            # 1 - NMAP - SSH
            Test().continueOrWait()
            self.sshNmap()

            # 2 - Keyscan - SSH
            Test().continueOrWait()
            self.sshKeyscan()

            if enableBrute == str("yes"):
                # 3 - HYDRA - SSH
                Test().continueOrWait()
                self.sshHydra()

        #############
        ## BATCH ^ ##
        #############

    def sshNmap(self):
        NMAP = "/NMAP"
        output = "{}{}".format(self.outputDir, NMAP)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- nmap -p {} -sV {} -oN {}/nmap-version-SSH.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} {} --script=ssh-auth-methods -oN {}/nmap-authentication-methods.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} {} --script=ssh2-enum-algos -oN {}/nmap-algorithms-allowed.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} {} --script=ssh-publickey-acceptance -oN {}/nmap-publickey-acceptance.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} {} --script=ssh-hostkey -oN {}/nmap-hostkey.txt".format(self.port, self.ip, output))

    def sshHydra(self):
        HYDRA = "/HYDRA"
        output = "{}{}".format(self.outputDir, HYDRA)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- hydra -l {} -P {} ssh://{}:{}/ -o {}/Hydra-Bruteforce-SSH.txt".format(SSH_name, SSH_Passwords, self.ip, self.port, output))

    def sshKeyscan(self):
        KEYSCAN = "/Public-Keys"
        output = "{}{}".format(self.outputDir, KEYSCAN)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- bash -c 'ssh-keyscan {} | tee {}/public-keyscan.txt'".format(self.ip, output))