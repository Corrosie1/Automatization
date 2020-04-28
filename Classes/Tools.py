import colorama
from colorama import Fore, Style
import os
import sys
from Classes.Protocols import *
#Variabelen
shell = os.system
green = Fore.GREEN
reset = Style.RESET_ALL

class Tools:
    def __init__(self):
        shell("clear")
        self.userProtocol = sys.argv[2]
        print("{}[*]{} The following tools are available for the protocol : {}{}{}".format(green, reset, red, self.userProtocol.upper(), reset))
        print("{}[*]{} If nothing pops up, please check with {}python3 {} --protocols{} if your protocol is supported".format(green, reset, red, sys.argv[0], reset))
        for protocol in range(len(protocolArray)):
            if str(self.userProtocol).upper() == protocolArray[protocol].upper():
                if self.userProtocol.upper() == str("FTP"):
                    self.protocolArt()
                    print("{}[+]{} NMAP".format(yellow, reset))
                    print("{}[+]{} HYDRA".format(yellow, reset))
                if self.userProtocol.upper() == str("SSH"):
                    self.protocolArt()
                    print("{}[+]{} NMAP".format(yellow, reset))
                    print("{}[+]{} HYDRA".format(yellow, reset))
                    print("{}[+]{} KEYSCAN (Scans for public keys on host)".format(yellow, reset))
                if self.userProtocol.upper() == str("TELNET"):
                    self.protocolArt()
                    print("{}[+]{} NMAP".format(yellow, reset))
                    print("{}[+]{} HYDRA".format(yellow, reset))
                if self.userProtocol.upper() == str("SMTP"):
                    self.protocolArt()
                    print("{}[+]{} NMAP".format(yellow, reset))
                    print("{}[+]{} SMTP-USER-ENUM".format(yellow, reset))
                    print("{}[+]{} HYDRA".format(yellow, reset))
                if self.userProtocol.upper() == str("DNS"):
                    self.protocolArt()
                    print("{}[+]{} NMAP".format(yellow, reset))
                    print("{}[+]{} DNS-ENUM".format(yellow, reset))
                    print("{}[+]{} DNS-RECON".format(yellow, reset))
                if self.userProtocol.upper() == str("HTTP"):
                    self.protocolArt()
                    print("{}[+]{} WPSCAN".format(yellow, reset))
                    print("{}[+]{} NIKTO".format(yellow, reset))
                    print("{}[+]{} DIRB".format(yellow, reset))
                    print("{}[+]{} NMAP".format(yellow, reset))
                if self.userProtocol.upper() == str("POP3"):
                    self.protocolArt()
                    print("{}[+]{} NMAP".format(yellow, reset))
                    print("{}[+]{} HYDRA".format(yellow, reset))
                if self.userProtocol.upper() == str("RPCBIND"):
                    self.protocolArt()
                    print("{}[+]{} NMAP".format(yellow, reset))
                    print("{}[+]{} RPCINFO".format(yellow, reset))
                if self.userProtocol.upper() == str("MSRPC"):
                    self.protocolArt()
                if self.userProtocol.upper() == str("NETBIOS-SSN"):
                    self.protocolArt()
                if self.userProtocol.upper() == str("IMAP"):
                    self.protocolArt()
                    print("{}[+]{} NMAP".format(yellow, reset))
                    print("{}[+]{} HYDRA".format(yellow, reset))
                if self.userProtocol.upper() == str("HTTPS"):
                    self.protocolArt()
                if self.userProtocol.upper() == str("SMB"):
                    self.protocolArt()
                if self.userProtocol.upper() == str("IMAPS"):
                    self.protocolArt()
                if self.userProtocol.upper() == str("POP3S"):
                    self.protocolArt()
                if self.userProtocol.upper() == str("MYSQL"):
                    self.protocolArt()
                if self.userProtocol.upper() == str("HTTP-PROXY"):
                    self.protocolArt()

    def protocolArt(self):
            shell("figlet -f slant {}".format(self.userProtocol.upper()))