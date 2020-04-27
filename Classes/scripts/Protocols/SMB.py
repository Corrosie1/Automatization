import os
import sys
from testing.test import *
from Settings.Settings import *

shell = os.system

class SMB:
    def __init__(self, ip, outputDir, port):
        SMB = "/445_SMB"
        self.ip = ip
        self.port = port
        self.outputDir = "{}{}{}".format(outputDir, ip, SMB)
        Test().exist_outputDir(self.outputDir)
        if len(sys.argv) > 2 and sys.argv[2] == str("--batch"):
            Test().continueOrWait()
            print("test SMB")