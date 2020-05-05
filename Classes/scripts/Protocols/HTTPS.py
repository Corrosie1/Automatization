import sys
from testing.test import *
from Settings.Settings import *
import requests

shell = os.system

class HTTPS:
    def __init__(self, ip, outputDir, port):
        HTTPS = "/443_HTTPS"
        self.ip = ip
        self.port = port
        self.outputDir = "{}{}{}".format(outputDir, ip, HTTPS)
        #
        Test().exist_outputDir(self.outputDir)

        if len(sys.argv) > 2 and sys.argv[2] == str("--batch"):

            # 1 - requests - HTTPS
            Test().continueOrWait()
            self.requests()

            # 2 - WPscan - HTTPS
            Test().continueOrWait()
            self.wpScan()

            # 3 - Nikto - HTTPS
            Test().continueOrWait()
            self.niktoWebScanner()

            # 4 - nmap script scans - HTTPS
            Test().continueOrWait()
            self.nmapHttps()

            # 5 – Dirb - HTTPS
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
        print("{}[*]{} Checking if the server is running Wordpress on {}https://{}:{}/{}...This might take a moment!".format(green, reset, cyan, self.ip, self.port, reset))
        shell("wpscan --url https://{}:{}/{} > /tmp/testWpScan.txt".format(self.ip, self.port, wpScanUriPath))
        output_1 = subprocess.check_output("cat /tmp/testWpScan.txt | grep -i 'Scan Aborted' | cut -d : -f 1", shell=True, universal_newlines=True)
        if len(output_1) > 0:
            print("{}[*]{} {}Scan aborted{} on URI {}https://{}:{}/{},{} checking if target is running wordpress on {}https://www.{}:{}/{}{}".format(green, reset, red, reset, cyan, self.ip, self.port, wpScanUriPath, reset, cyan, self.ip, self.port, wpScanUriPath, reset))
            shell("wpscan --url https://www.{}:{}/{} > /tmp/testWpScan.txt".format(self.ip, self.port, wpScanUriPath))
            output_2 = subprocess.check_output("cat /tmp/testWpScan.txt | grep -i 'Scan Aborted' | cut -d : -f 1", shell=True, universal_newlines=True)
            if len(output_2) > 0:
                print("{}[*]{} {}Scan Aborted{}, Wordpress does not seem to be running on target {}https://www.{}:{}/{}{}".format(green, reset, red, reset, cyan, self.ip, self.port, reset, wpScanUriPath))
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
        shell("gnome-terminal -q -- nikto -h https://{}:{}/ -o {}/Nikto.txt ".format(self.ip, self.port, output))

    def nmapHttps(self):
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
        shell("gnome-terminal -q -- dirb -f https://{}:{} {} -o {}/Recursive.txt".format(self.ip, self.port, Dirb_Brute_List, output))
        # Non Recursive
        shell("gnome-terminal -q -- dirb -f https://{}:{} {} -r -o {}/No-recursive.txt".format(self.ip, self.port, Dirb_Brute_List, output))
        # Extensions Recursive
        shell("gnome-terminal -q -- dirb -f https://{}:{} {} -o {}/recursive-Extensions.txt -X .pl, .sh, .exe, .ps, .py, .php, .cgi, .log, .sql, .xml, .aspx, .asp".format(self.ip, self.port, Dirb_Brute_List, output))

    def requests(self):
        # Robots.txt
        requestRobot = requests.get('https://{}:{}/robots.txt'.format(self.ip, self.port))
        print("{}[+]{} https://{}:{}/{}robots.txt{} returned status code : {}{}{} ".format(brightGreen, reset, self.ip, self.port, red, reset, red, requestRobot.status_code, reset))
        # Admin
        try:
            requestAdmin = requests.get('https://{}:{}/admin'.format(self.ip, self.port))
            print("{}[+]{} https://{}:{}/{}admin{} returned status code : {}{}{} ".format(brightGreen, reset, self.ip,
                                                                                         self.port, red, reset, red,
                                                                                         requestAdmin.status_code,
                                                                                         reset))
            if requestAdmin.status_code == 200:
                print("{}[*]{} Dont forget to try some standard default username/password combinations :".format(green,
                                                                                                                 reset))
                print("{}[+]{} - admin:admin".format(brightGreen, reset))
                print("{}[+]{} - admin:password".format(brightGreen, reset))
                print("{}[+]{} - admin:passwd".format(brightGreen, reset))
                print("{}[+]{} - admin:123456".format(brightGreen, reset))
                #
        except:
            pass
        # .htpasswd
        requestPasswd = requests.get('https://{}:{}/.htpasswd'.format(self.ip, self.port))
        print("{}[+]{} https://{}:{}/{}.htpasswd{} returned status code : {}{}{} ".format(brightGreen, reset, self.ip, self.port, red, reset, red, requestPasswd.status_code, reset))
        # .htaccess
        requestAccess = requests.get('https://{}:{}/.htaccess'.format(self.ip, self.port))
        print("{}[+]{} https://{}:{}/{}.htaccess{} returned status code : {}{}{} ".format(brightGreen, reset, self.ip, self.port, red, reset, red, requestAccess.status_code, reset))
