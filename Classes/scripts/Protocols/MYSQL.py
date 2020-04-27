import os
import sys
from testing.test import *
from Settings.Settings import *

shell = os.system

class MYSQL:
    def __init__(self, ip, outputDir, port):
        MYSQL = "/3306_MYSQL"
        self.ip = ip
        self.port = port
        self.outputDir = "{}{}{}".format(outputDir, ip, MYSQL)
        Test().exist_outputDir(self.outputDir)
        if len(sys.argv) > 2 and sys.argv[2] == str("--batch"):
            Test().continueOrWait()
            print("test MYSQL")