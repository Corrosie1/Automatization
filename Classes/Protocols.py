from Settings.color import *
import os

shell = os.system

protocolArray = ["FTP", "SSH", "TELNET", "SMTP", "DNS", "HTTP",
                 "POP3", "RPCBIND", "MSRPC", "NETBIOS-SSN", "IMAP",
                 "HTTPS", "SMB", "IMAPS", "POP3S", "MYSQL", "HTTP-PROXY"]

class Protocols:
    def __init__(self):
        shell("clear")

        print("{}[*]{} The following protocols are supported for recon by this tool : \n".format(green, reset))
        for protocol in range(len(protocolArray)):
            if protocol %2 == 0:
                print("{}[*]{} Protocol supported : {}{}{}".format(green, reset, red, protocolArray[protocol], reset))
            else:
                print("{}[*]{} Protocol supported : {}{}{}".format(green, reset, yellow, protocolArray[protocol], reset))