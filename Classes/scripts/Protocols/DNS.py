from testing.test import *
from Settings.Settings import *
#
import os
import sys
#
shell = os.system

class DNS:
    def __init__(self, ip, outputDir, port):
        DNS = "/53_DNS"
        self.ip = ip
        self.port = port
        self.outputDir = "{}{}{}".format(outputDir, ip, DNS)
        #
        Test().exist_outputDir(self.outputDir)

        if len(sys.argv) > 2 and sys.argv[2] == str("--batch"):

            # 1 - NMAP - DNS
            Test().continueOrWait()
            self.nmapDnsIp()

            if DNS_DOMAIN_NAME != str(""):
                print("{}[*]{} Current Domain that is being tested on (And is within the settings.py file) : {}".format(green, reset, red, DNS_DOMAIN_NAME, reset))
                print("{}[*]{} Dont forget to make use of the following tools:".format(green, reset))
                print("{}[*]{}      - https://hackking.net/subdomain-takeover-scanner/ (subdomain takeover scanner)".format(green, reset))
                print("{}[*]{}      - https://centralops.net/co/DomainDossier.aspx (deep queries on a DNS server)".format(green, reset))
                print("{}[*]{}      - https://emkei.cz/  (Mail spoofer)".format(green, reset))
                print("{}[*]{}      - https://dnsspy.io/ (General deep scan of DNS)".format(green, reset))
                shell("sleep 2")

                # 1 - DNS-ENUM - DNS
                Test().continueOrWait()
                self.dnsEnumDns()

                # 2 - DNS-Recon - DNS
                Test().continueOrWait()
                self.dnsReconDns()

                # 3 - NMAP - DNS
                Test().continueOrWait()
                self.nmapDnsDomain()

        #############
        ## BATCH ^ ##
        #############

    def nmapDnsIp(self):
        NMAP = "/NMAP-IP"
        output = "{}{}".format(self.outputDir, NMAP)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- nmap -p {} -sV {} -oN {}/nmap-version-DNS.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} {} --script=dns-nsid -oN {}/nmap-dns-nsid.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} {} --script=fcrdns -oN {}/nmap-fcrdns.txt".format(self.port, self.ip, output))

    def dnsEnumDns(self):
        DNS_ENUM = "/DNS_ENUM"
        output = "{}{}".format(self.outputDir, DNS_ENUM)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- bash -c 'dnsenum {} | tee {}/dnsenum.txt'".format(DNS_DOMAIN_NAME, output))

    def dnsReconDns(self):
        DNS_RECON = "/DNS_RECON"
        output = "{}{}".format(self.outputDir, DNS_RECON)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- bash -c 'dnsrecon -d {} --lifetime 300 -a -s -g -b -k -w -z | tee {}/DNS-Recon.txt'".format(DNS_DOMAIN_NAME, output))

    def nmapDnsDomain(self):
        NMAP_2 = "/NMAP-DOMAIN"
        output_2 = "{}{}".format(self.outputDir, NMAP_2)
        #
        Test().exist_outputDir(output_2)
        #
        shell("gnome-terminal -q -- nmap -p {} {} --script=dns-nsec-enum --script-args dns-nsec-enum.domains={} -oN {}/nmap-nsec-enum-domains.txt ".format(self.port, self.ip, DNS_DOMAIN_NAME, output_2))
        shell("gnome-terminal -q -- nmap -p {} {} --script=dns-srv-enum --script-args dns-srv-enum.domain={} -oN {}/nmap-srv-enum.txt".format(self.port, self.ip, DNS_DOMAIN_NAME, output_2))
