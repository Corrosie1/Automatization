from Settings.Settings import *
from Classes.scripts.Nmap import *

class Batch:

    def __init__(self, ip):
        self.outputDir = outputDir
        self.ip = ip
        #------------------------#
        Nmap().nmap_fast(ip, outputDir)

