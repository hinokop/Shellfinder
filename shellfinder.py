#!/usr/bin/python3
import requests
import sys


def banner():
    sys.stdout.write("\033[0;36m")
    print("""
       _____ _          _ _   ______ _           _
      / ____| |        | | | |  ____(_)         | |
     | (___ | |__   ___| | | | |__   _ _ __   __| | ___ _ __
      \___ \| '_ \ / _ \ | | |  __| | | '_ \ / _` |/ _ \ '__|
      ____) | | | |  __/ | | | |    | | | | | (_| |  __/ |
     |_____/|_| |_|\___|_|_| |_|    |_|_| |_|\__,_|\___|_|  -xDevil """)
    sys.stdout.write("\033[0;0m")


def clearing():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


banner()
shells = ['/madspot.php','/mad.php','/404.php','/anon.php','/pirates.php','/c99.php','/anonymous.php','/shell.php','/sh3ll.php','/madspotshell.php','/b374k.php','/c100.php','/priv8.php','/private.php','/cp.php','/cpbrute.php','/ironshell.php','/themes/404/404.php','/templates/atomic/index.php','/templates/beez5/index.php','/hacked.php','/r57.php','/wso.php','/Kurama.php','/wso24.php','/wso26.php','/wso404.php','/sym.php','/symsa2.php','/sym3.php','/whmcs.php','/whmcskiller.php','/cracker.php','/1.php','/2.php','/sql.php','/gaza.php','/database.php','/a.php','/dz.php','/cpanel.php','/system.php','/um3r.php','/zone-h.php','/c22.php','/root.php','/r00t.php','/doom.php','/dam.php','/killer.php','/user.php','/wp-content/plugins/disqus-comment-system/disqus.php','/cpn.php','/shelled.php','/uploader.php','/up.php','/xd.php','/d00.php','/h4xor.php','/tmp/mad.php','/tmp/1.php','/wp-content/plugins/akismet/akismet.php','/images/stories/w.php','/w.php','/downloads/dom.php','/templates/ja-helio-farsi/index.php','/wp-admin/m4d.php','/d.php', '/Pirates.php','/rootshell.php','/php-backdoor.php','/psyc0.php','/haxor.php','/antichat.php','/antichatshell.php','/udp.php','/tcp.php']

sys.stdout.write("\033[0;36m")
website = "http://" + input("      http://")
print()

try:
    r = requests.get(website)
except Exception as e:
    sys.stdout.write("\033[1;31m")
    print("Failed to establish a new connection")
    exit(1)

for i in range(0, len(shells)):
    r = requests.get(website + shells[i])
    if str(r.status_code)[0] == "2":
        sys.stdout.write("\033[1;32m")
    elif str(r.status_code)[0] == "3":
        sys.stdout.write("\033[1;94m")
    elif str(r.status_code)[0] == "4":
        sys.stdout.write("\033[1;31m")
    elif str(r.status_code)[0] == "5":
        sys.stdout.write("\033[1;35m")
    print(r.status_code, shells[i])
    sys.stdout.write("\033[0;0m")
    percent = ((i+1)/(len(shells)))*100
    print("["+str(int(percent))+"%]", end="\r")

exit()
