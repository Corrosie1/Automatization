import os
import sys
from testing.test import *
from Settings.Settings import *
import requests

shell = os.system

class HTTP:
    def __init__(self, ip, outputDir, port):
        HTTP = "/80_HTTP"
        self.ip = ip
        self.port = port
        self.outputDir = "{}{}{}".format(outputDir, ip, HTTP)
        #
        Test().exist_outputDir(self.outputDir)

        if len(sys.argv) > 2 and sys.argv[2] == str("--batch"):

            # 1 - requests - HTTP
            Test().continueOrWait()
            self.requests()

            # 2 - WPscan - HTTP
            Test().continueOrWait()
            self.wpScan()

            # 3 - Nikto - HTTP
            Test().continueOrWait()
            self.niktoWebScanner()

            # 4 - nmap script scans - HTTP
            Test().continueOrWait()
            self.nmapHttp()

            # 5 – Dirb - HTTP
            Test().continueOrWait()
            self.dirb()

    def wordpressNmap(self, nmapOutput):
        print("{}[*]{} Executing Wordpress enum-users script scan...".format(green, reset))
        shell("sleep 2")
        shell("gnome-terminal -q -- nmap -p {} --script=http-wordpress-users {} -oN {}/nmap-wordpress-enum-users.txt".format(self.port, self.ip, nmapOutput))

    def wordpressFound(self):
        wordpress = "/Wordpress"
        output = "{}{}".format(self.outputDir, wordpress)
        #
        Test().exist_outputDir(output)
        #
        print("{}[*]{} Wordpress is running on target host!".format(green, reset))
        shell("mv /tmp/testWpScan.txt {}".format(output))
        shell("mv {}/testWpScan.txt {}/WPscan.txt".format(output, output))
        self.wordpressNmap(output)

    def wpScan(self):
        print("{}[*]{} Checking if the server is running Wordpress on {}http://{}:{}/{}...This might take a moment!".format(green, reset, cyan, self.ip, self.port, reset))
        shell("wpscan --url http://{}:{}/{} > /tmp/testWpScan.txt".format(self.ip, self.port, wpScanUriPath))
        output_1 = subprocess.check_output("cat /tmp/testWpScan.txt | grep -i 'Scan Aborted' | cut -d : -f 1", shell=True, universal_newlines=True)
        if len(output_1) > 0:
            print("{}[*]{} {}Scan aborted{} on URI {}http://{}:{}/{},{} checking if target is running wordpress on {}http://www.{}/{}{}".format(green, reset, red, reset, cyan, self.ip, self.port, reset, wpScanUriPath, cyan, self.ip, reset, wpScanUriPath))
            shell("wpscan --url http://www.{}:{}/{} > /tmp/testWpScan.txt".format(self.ip, self.port, wpScanUriPath))
            output_2 = subprocess.check_output("cat /tmp/testWpScan.txt | grep -i 'Scan Aborted' | cut -d : -f 1", shell=True, universal_newlines=True)
            if len(output_2) > 0:
                print("{}[*]{} {}Scan Aborted{}, Wordpress does not seem to be running on target {}http://www.{}:{}/{}{}".format(green, reset, red, reset, cyan, self.ip, self.port, reset, wpScanUriPath))
                shell("rm -rf /tmp/testWpScan.txt")
                shell("sleep 2")
            else:
                self.wordpressFound()
        else:
            self.wordpressFound()

    def niktoWebScanner(self):
        nikto = "/Nikto"
        output = "{}{}".format(self.outputDir, nikto)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- nikto -h http://{}:{}/ -o {}/Nikto.txt ".format(self.ip, self.port, output))

    def nmapHttp(self):
        NMAP = "/NMAP"
        output = "{}{}".format(self.outputDir, NMAP)
        #
        Test().exist_outputDir(output)
        #
        shell("gnome-terminal -q -- nmap -p {} --script=http-comments-displayer {} -oN {}/nmap-comments-displayer.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} --script=http-date {} -oN {}/nmap-date.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} --script=http-grep {} -oN {}/nmap-grep.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} --script=http-passwd {} -oN {}/nmap-traversal.txt".format(self.port, self.ip, output))
        shell("gnome-terminal -q -- nmap -p {} --script=http-shellshock {} -oN {}/nmap-shellshock.txt".format(self.port, self.ip, output))

    def dirb(self):
        Dirb = "/Dirb"
        output = "{}{}".format(self.outputDir, Dirb)
        #
        Test().exist_outputDir(output)
        # Recursive
        shell("gnome-terminal -q -- dirb http://{}:{} {} -o {}/Recursive.txt".format(self.ip, self.port, Dirb_Brute_List, output))
        # Non Recursive
        shell("gnome-terminal -q -- dirb http://{}:{} {} -r -o {}/No-recursive.txt".format(self.ip, self.port, Dirb_Brute_List, output))
        # Extensions Recursive
        shell("gnome-terminal -q -- dirb http://{}:{} {} -o {}/recursive-Extensions.txt -X .pl, .sh, .exe, .ps, .py".format(self.ip, self.port, Dirb_Brute_List, output))

    def requests(self):
        # Robots.txt
        requestRobot = requests.get('http://{}:{}/robots.txt'.format(self.ip, self.port))
        print("{}[*]{} {}http://{}:{}/robots.txt{} returned status code : {}{}{} ".format(green, reset, cyan, self.ip, self.port, reset, red, requestRobot.status_code, reset))
        # Admin
        requestAdmin = requests.get('http://{}:{}/admin'.format(self.ip, self.port))
        print("{}[*]{} {}http://{}:{}/admin{} returned status code : {}{}{} ".format(green, reset, cyan, self.ip, self.port, reset, red, requestAdmin.status_code, reset))
        # .htpasswd
        if requestAdmin.status_code == 200:
            print("{}[*]{} Dont forget to try some standard default username/password combinations :".format(green, reset))
            print("{}[*]{} \t - admin:admin".format(green, reset))
            print("{}[*]{} \t - admin:password".format(green, reset))
            print("{}[*]{} \t - admin:passwd".format(green, reset))
            print("{}[*]{} \t - admin:123456".format(green, reset))
            #
        requestPasswd = requests.get('http://{}:{}/.htpasswd'.format(self.ip, self.port))
        print("{}[*]{} {}http://{}:{}/.htpasswd{} returned status code : {}{}{} ".format(green, reset, cyan, self.ip, self.port, reset, red, requestPasswd.status_code, reset))
        # .htaccess
        requestAccess = requests.get('http://{}:{}/.htaccess'.format(self.ip, self.port))
        print("{}[*]{} {}http://{}:{}/.htaccess{} returned status code : {}{}{} ".format(green, reset, cyan, self.ip, self.port, reset, red, requestAccess.status_code, reset))
