import os
import sys
from testing.test import *
from Settings.Settings import *

shell = os.system

class HTTP_PROXY:
    def __init__(self, ip, outputDir, port):
        HTTP_PROXY = "/8080_HTTP_PROXY"
        self.ip = ip
        self.port = port
        self.outputDir = "{}{}{}".format(outputDir, ip, HTTP_PROXY)
        Test().exist_outputDir(self.outputDir)
        if len(sys.argv) > 2 and sys.argv[2] == str("--batch"):
            Test().continueOrWait()
            print("test HTTP_PROXY")