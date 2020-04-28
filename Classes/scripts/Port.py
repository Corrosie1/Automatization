from Classes.scripts.Protocols.FTP import *
from Classes.scripts.Protocols.SSH import *
from Classes.scripts.Protocols.TELNET import *
from Classes.scripts.Protocols.SMTP import *
from Classes.scripts.Protocols.DNS import *
from Classes.scripts.Protocols.HTTP import *
from Classes.scripts.Protocols.POP3 import *
from Classes.scripts.Protocols.RPCBIND import *
from Classes.scripts.Protocols.MSRPC import *
from Classes.scripts.Protocols.NETBIOS import *
from Classes.scripts.Protocols.IMAP import *
from Classes.scripts.Protocols.HTTPS import *
from Classes.scripts.Protocols.SMB import *
from Classes.scripts.Protocols.IMAPS import *
from Classes.scripts.Protocols.POP3S import *
from Classes.scripts.Protocols.MYSQL import *
from Classes.scripts.Protocols.RDP import *
from Classes.scripts.Protocols.VNC import *
from Classes.scripts.Protocols.HTTP_PROXY import *
#
import os
import re
from itertools import islice
from Classes.scripts.Functions_Port import *
import subprocess
#
shell = os.system

class Port:
    def checkPorts(self, ip, outputDir):
        # Array
        self.protocolArray = ["ftp", "ssh", "telnet", "smtp", "domain", "http", "pop3", "rpcbind", "msrpc", "netbios-ssn", "imap", "https", "microsoft-ds", "imaps", "pop3s", "mysql", "http-proxy"]
        # variables
        nmapBasic = "/NMAP_BASIC.txt"
        self.outputDir = outputDir
        self.ip = ip
        self.path = "{}{}".format(outputDir, ip)
        #
        shell("clear")
        outputServices = subprocess.check_output("cat {}{} | grep -e /tcp -e /udp | awk '{{print$3}}'".format(self.path, nmapBasic), shell=True, universal_newlines=True)
        outputPorts = subprocess.check_output("cat {}{} | grep -e /tcp -e /udp | awk '{{print$1}}'".format(self.path, nmapBasic), shell=True, universal_newlines=True)
        servicesFound = outputServices.split("\n")
        self.portsFoundDirty = outputPorts.split("/tcp")
        #
        servicesClean = servicesFound;
        portsClean = []
        self.executePorts(servicesClean, portsClean)

    def executePorts(self, servicesClean, portsClean):

        for i in range(len(self.portsFoundDirty)):
            split = self.portsFoundDirty[i].split("\n")
            for j in range(len(split)):
                txt = split[j]
                result = re.search("^[0-9]", txt)
                if result:
                    portsClean.append(txt)

        for i in range(len(servicesClean)):
            for j in range(len(self.protocolArray)):
                if servicesClean[i] == self.protocolArray[j]:
                    portFound(portsClean[i], servicesClean[i])
                    # if servicesClean[i] == str("ftp"):
                    #     FTP(self.ip, self.outputDir, portsClean[i])
                    # if servicesClean[i] == str("ssh"):
                    #     SSH(self.ip, self.outputDir, portsClean[i])
                    # if servicesClean[i] == str("telnet"):
                    #     TELNET(self.ip, self.outputDir, portsClean[i])
                    # if servicesClean[i] == str("smtp"):
                    #     SMTP(self.ip, self.outputDir, portsClean[i])
                    # if servicesClean[i] == str("domain"):
                    #     DNS(self.ip, self.outputDir, portsClean[i])
                    # if servicesClean[i] == str("http"):
                    #     HTTP(self.ip, self.outputDir, portsClean[i])
                    # if servicesClean[i] == str("pop3"):
                    #     POP3(self.ip, self.outputDir, portsClean[i])
                    if servicesClean[i] == str("rpcbind"):
                        RPCBIND(self.ip, self.outputDir, portsClean[i])
                    if servicesClean[i] == str("msrpc"):
                        MSRPC(self.ip, self.outputDir, portsClean[i])
                    if servicesClean[i] == str("netbios-ssn"):
                        NETBIOS(self.ip, self.outputDir, portsClean[i])
                    if servicesClean[i] == str("imap"):
                        IMAP(self.ip, self.outputDir, portsClean[i])
                    if servicesClean[i] == str("https"):
                        HTTPS(self.ip, self.outputDir, portsClean[i])
                    if servicesClean[i] == str("microsoft-ds"):
                        SMB(self.ip, self.outputDir, portsClean[i])
                    if servicesClean[i] == str("imaps"):
                        IMAPS(self.ip, self.outputDir, portsClean[i])
                    if servicesClean[i] == str("pop3s"):
                        POP3S(self.ip, self.outputDir, portsClean[i])
                    if servicesClean[i] == str("mysql"):
                        MYSQL(self.ip, self.outputDir, portsClean[i])
                    if servicesClean[i] == str("http-proxy"):
                        HTTP_PROXY(self.ip, self.outputDir, portsClean[i])

        print("{}[*]{} Scan finished, note that {}some programs may still be running!{}".format(green, reset, red, reset))
        print("{}[*]{} The output of your scan can be found in {}{}{}{}".format(green, reset, yellow, outputDir, self.ip, reset))

