from Settings.Settings import *
from Settings.color import *
#
import os
import os.path
import subprocess
#
shell = os.system

class Test:

    def exist_outputDir(self, directory):
        isdir = os.path.isdir(directory)
        if isdir:
            pass
        else:
            print("{}[*]{} The following directory was made {}".format(green, reset, directory))
            os.system("sleep 2")
            os.system("mkdir -p {}".format(directory))

    def countTerminals(self):
        output = subprocess.check_output("ls /dev/pts/ | wc -l", shell=True, universal_newlines=True)
        return int(output)

    def networkMon(self):
        shell("timeout 2s ifstat -T > /tmp/networkMon.txt")
        output = 0

        test = subprocess.check_output("cat /tmp/networkMon.txt | grep -w -e [0-9].* | wc -w", shell=True,
                                       universal_newlines=True)
        if int(test) == 4:
            output = subprocess.check_output("cat /tmp/networkMon.txt | grep -w -e [0-9].* | awk '{print$4}'", shell=True,
                                             universal_newlines=True)
        elif int(test) == 6:
            output = subprocess.check_output("cat /tmp/networkMon.txt | grep -w -e [0-9].* | awk '{print$6}'", shell=True,
                                             universal_newlines=True)
        elif int(test) == 8:
            output = subprocess.check_output("cat /tmp/networkMon.txt | grep -w -e [0-9].* | awk '{print$8}'", shell=True,
                                             universal_newlines=True)
        elif int(test) == 10:
            output = subprocess.check_output("cat /tmp/networkMon.txt | grep -w -e [0-9].* | awk '{print$10}'", shell=True,
                                             universal_newlines=True)
        else:
            print("{}[*]{} To many interfaces are currently online, a max of 4 interfaces is allowed!".format(green,
                                                                                                              reset))
            shell("sleep 2")
            shell("exit 0")
        shell("rm -rf /tmp/networkMon.txt")
        return float(output)

    def continueOrWait(self):
            traffic = self.networkMon()
            #
            if traffic > maxOutgoingTraffic and self.countTerminals() > maxTerminalsOpen:
                print("{}[*]{} Waiting.... terminals opened : {}{}{}, open terminals allowed : {}{}{}".format(green, reset, red, self.countTerminals(), reset, red, maxTerminalsOpen, reset))
                print("{}[*]{} Outgoing traffic : {}{} KB/s{}, outgoing traffic allowed : {}{} KB/s{}".format(green, reset, red, traffic, reset, red, maxOutgoingTraffic, reset))
                os.system("sleep 10")
                self.continueOrWait()
            else:
                pass

