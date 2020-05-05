from Art.bashArt import *
from testing.test import *
from Classes.scripts.Port import *
from Settings.color import *
#
import os
import sys
#
shell = os.system

class Nmap:

    def nmap_fast(self, ip, outputDir):
        # Variables
        self.ip = ip
        self.path = "{}{}".format(outputDir, ip)
        #
        Test().exist_outputDir(self.path)
        print("{}[*]{} Starting up fast nmap port scan, host = {}, outputdir = {}".format(green, reset, self.ip, self.path))
        print("{}[*]{} This may take a little moment".format(green, reset))
        manPc()
        shell("nmap -sS {} -oN {}/NMAP_BASIC.txt > /dev/null".format(self.ip, self.path))
        print("{}[*]{} Basic port scan finished, full Nmap scan starting...".format(green, reset))
        shell("sleep 2")
        shell("clear")
        #
        if sys.argv[2] == str("--batch"):
            self.nmap_full(self.ip, outputDir)
            Port().checkPorts(self.ip, outputDir)

    def nmap_full(self, ip, outputDir):
        # Variables
        self.ip = ip
        self.path = "{}{}".format(outputDir, ip)
        #
        shell("clear")
        Test().exist_outputDir(self.path)
        print("{}[*]{} Starting up NMAP full port scan, host = {}, outputdir = {}".format(green, reset, self.ip, self.path))
        print("{}[*]{} Another scripts will run in the background".format(green, reset))
        shell("gnome-terminal -q -- nmap -A -oN {}/NMAP_FULL.txt -sV -sC -p 1-65535 -sS {}".format(self.path, self.ip))
        shell("sleep 2")
        shell("clear")
