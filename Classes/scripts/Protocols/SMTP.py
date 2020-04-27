from testing.test import *
from Settings.Settings import *
#
import os
import sys
#
shell = os.system

class SMTP:
    def __init__(self, ip, outputDir, port):
        SMTP = "/25_SMTP"
        self.ip = ip
        self.port = port
        self.outputDir = "{}{}{}".format(outputDir, ip, SMTP)
        #
        Test().exist_outputDir(self.outputDir)

        if len(sys.argv) > 2 and sys.argv[2] == str("--batch"):

            # 1 - NMAP - SMTP
            Test().continueOrWait()
            self.smtpNmap()

            if enableBrute == str("yes"):
                # 2 - SMTP-USER-ENUM - SMTP
                Test().continueOrWait()
                self.smtpUserEnum()

                # 3 - HYDRA - SMTP
                Test().continueOrWait()
                self.smtpHydra()

        #############
        ## BATCH ^ ##
        #############

    def smtpNmap(self):
        NMAP = "/NMAP"
        output = "{}{}".format(self.outputDir, NMAP)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- nmap -p {} -sV {} -oN {}/smtp-version.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} {} --script=smtp-commands -oN {}/smtp-commands.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} {} --script=smtp-enum-users -oN {}/smtp-enum-users.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} {} --script=smtp-ntlm-info -oN {}/smtp-ntlm-info.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} {} --script=smtp-open-relay -oN {}/smtp-open-relay.txt".format(self.port, self.ip, output))

    def smtpHydra(self):
        HYDRA = "/HYDRA"
        output = "{}{}".format(self.outputDir, HYDRA)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- hydra -l {} -P {} smtp://{}:{}/ -o {}/smtp-bruteforce.txt".format(SMTP_name, SMTP_Passwords, self.ip, self.port, output))

    def smtpUserEnum(self):
        SMTP_USER_ENUM = "/SMTP_USER_ENUM"
        output = "{}{}".format(self.outputDir, SMTP_USER_ENUM)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- bash -c 'smtp-user-enum -M VRFY -U {} -t {} | tee {}/smtp-user-enum-vrfy.txt'".format(SMTP_name_list, self.ip, output))
        shell("gnome-terminal -q -- bash -c 'smtp-user-enum -M EXPN -U {} -t {} | tee {}/smtp-user-enum-expn.txt'".format(SMTP_name_list, self.ip, output))
