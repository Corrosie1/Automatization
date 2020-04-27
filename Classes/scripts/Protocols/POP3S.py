import os
import sys
from testing.test import *
from Settings.Settings import *

shell = os.system

class POP3S:
    def __init__(self, ip, outputDir, port):
        POP3S = "/995_POP3S"
        self.ip = ip
        self.port = port
        self.outputDir = "{}{}{}".format(outputDir, ip, POP3S)
        Test().exist_outputDir(self.outputDir)
        if len(sys.argv) > 2 and sys.argv[2] == str("--batch"):
            Test().continueOrWait()
            print("test POP3S")