#!/usr/bin/python3
from Classes.Specific import *
from Classes.Multiple import *
from Classes.Batch import *
from Classes.Tools import *
from Classes.Update import *
from Classes.Protocols import *
from Settings.color import *
#
import os
import sys
#
shell = os.system
# Code main
class Main:

    def __init__(self):
        if len(sys.argv) == 2 and sys.argv[1] == str("--update"):
            Update()
        elif len(sys.argv) == 2 and sys.argv[1] == str("--protocols"):
            Protocols()
        elif len(sys.argv) < 3:
            self.help()
        elif len(sys.argv) == 3:
            if sys.argv[2] == str("--update"):
                Update()
            elif sys.argv[2] == str("--help"):
                self.help()
            elif sys.argv[1] == str("--tools"):
                Tools()
            elif sys.argv[2] == str("--batch"):
                ip = sys.argv[1];
                Batch(ip)
            elif sys.argv[2] == str("--specific"):
                ip = sys.argv[1];
                Specific(ip)
            elif sys.argv[2] == str("--multiple"):
                ip = sys.argv[1];
                Multiple(ip)
            else:
                self.help()

    def help(self):
        shell("clear")
        print("{}[*]{}  Usage : python3 {} 192.168.0.1 <PARAMETER> \n".format(green, reset, sys.argv[0]))

        print("{}[*]{}  --help                                          |   print this help menu".format(green, reset))
        print("{}[*]{}  --update                                        |   updates all tools that are used within this script".format(green, reset))
        print("{}[*]{}  --protocols                                     |   shows all the protocols that are supported in this script".format(green, reset))
        print("{}[*]{}  --tools <protocol>                              |   shows a list of all available tools used within this script ".format(green, reset))
        print("{}[*]{}  --batch                                         |   run all tools (based on open ports) within this script against a target host".format(green, reset))
        print("{}[*]{}  --specific --protocol <toolname>                |   run a specific tool against a target host".format(green, reset))
        print("{}[*]{}  --multiple --protocol <toolname1> <toolname2>   |   run multiple scripts from a specific protocol against a target host.".format(green, reset))


main = Main()