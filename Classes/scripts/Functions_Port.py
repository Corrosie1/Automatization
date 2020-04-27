from Settings.color import *
import os
#
shell = os.system

def portFound(port, protocol):
    print("{}[*]{} {}{} (Port {}){} Service found, executing scripts...".format(green, reset, yellow, protocol.upper(), port, reset))
    os.system("sleep 2")