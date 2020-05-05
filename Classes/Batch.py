from Settings.color import *
from Settings.Settings import *
from Classes.scripts.Nmap import *
#
from datetime import datetime
import os
#
dt = datetime.now()
shell = os.system

class Batch:

    def __init__(self, ip):
        self.outputDir = outputDir
        self.ip = ip
        #------------------------#
        shell("clear")
        print("{}[*]{} Scan starting at {}{}/{}/{}, {}:{}:{}{}".format(green, reset, brightYellow, dt.year, dt.month,
                                                                       dt.day, dt.hour, dt.minute, dt.second, reset))
        shell("sleep 2")
        Nmap().nmap_fast(ip, outputDir)
