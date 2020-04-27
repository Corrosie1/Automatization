import os
from Settings.color import *
shell = os.system

class Update:
    def __init__(self):
        shell("clear")
        print("{}[*]{} Will start updating all programs used within this script".format(green, reset))
        shell("sleep 1")
        self.updateApt()
        self.updateNmap()
        self.updateNikto()
        self.updateWpScan()
        shell("clear")

    def updatePrint(self, tool):
        shell("clear")
        print("{}[*]{} Updating {}{}{}...".format(green, reset, red, tool, reset))

    def updateDone(self, tool):
        print("{}[*]{} Updating {}{}{} is done!".format(green, reset, red, tool, reset))
        shell("sleep 2")

    def updateApt(self):
        self.updatePrint(str("system with apt-get update -y"))
        shell("apt-get update -y")
        self.updateDone(str("the system"))

    def updateNmap(self):
        self.updatePrint(str("nmap"))
        shell("nmap --script-updatedb")
        self.updateDone(str("nmap"))

    def updateNikto(self):
        self.updatePrint(str("Nikto"))
        shell("nikto --update")
        self.updateDone(str("Nikto"))

    def updateWpScan(self):
        self.updatePrint(str("WPscan"))
        shell("wpscan --update")
        self.updateDone(str("WPscan"))
