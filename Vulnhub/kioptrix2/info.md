# kioptrix 2

[link](https://www.vulnhub.com/entry/kioptrix-level-11-2,23/)

Starting Nmap 7.60 ( https://nmap.org ) at 2017-11-24 13:06 EST
Nmap scan report for 172.16.8.1
Host is up (0.00025s latency).
All 1000 scanned ports on 172.16.8.1 are closed
MAC Address: 00:50:56:C0:00:01 (VMware)

Nmap scan report for 172.16.8.134
Host is up (0.00033s latency).
Not shown: 994 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
111/tcp  open  rpcbind
443/tcp  open  https
631/tcp  open  ipp
3306/tcp open  mysql
MAC Address: 00:0C:29:71:C3:B8 (VMware)

Nmap scan report for 172.16.8.254
Host is up (-0.088s latency).
All 1000 scanned ports on 172.16.8.254 are filtered
MAC Address: 00:50:56:E9:32:62 (VMware)

Nmap scan report for 172.16.8.129
Host is up (0.000012s latency).
All 1000 scanned ports on 172.16.8.129 are closed

Nmap done: 256 IP addresses (4 hosts up) scanned in 81.10 seconds



Starting Nmap 7.60 ( https://nmap.org ) at 2017-11-24 13:08 EST
Nmap scan report for 172.16.8.134
Host is up (0.00036s latency).
Not shown: 994 closed ports
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 3.9p1 (protocol 1.99)
| ssh-hostkey: 
|   1024 8f:3e:8b:1e:58:63:fe:cf:27:a3:18:09:3b:52:cf:72 (RSA1)
|   1024 34:6b:45:3d:ba:ce:ca:b2:53:55:ef:1e:43:70:38:36 (DSA)
|_  1024 68:4d:8c:bb:b6:5a:bd:79:71:b8:71:47:ea:00:42:61 (RSA)
|_sshv1: Server supports SSHv1
80/tcp   open  http     Apache httpd 2.0.52 ((CentOS))
|_http-server-header: Apache/2.0.52 (CentOS)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
111/tcp  open  rpcbind  2 (RPC #100000)
| rpcinfo: 
|   program version   port/proto  service
|   100000  2            111/tcp  rpcbind
|   100000  2            111/udp  rpcbind
|   100024  1            690/udp  status
|_  100024  1            693/tcp  status
443/tcp  open  ssl/http Apache httpd 2.0.52 ((CentOS))
|_http-server-header: Apache/2.0.52 (CentOS)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
| ssl-cert: Subject: commonName=localhost.localdomain/organizationName=SomeOrganization/stateOrProvinceName=SomeState/countryName=--
| Not valid before: 2009-10-08T00:10:47
|_Not valid after:  2010-10-08T00:10:47
|_ssl-date: 2017-11-24T15:59:21+00:00; -2h09m45s from scanner time.
| sslv2: 
|   SSLv2 supported
|   ciphers: 
|     SSL2_RC2_128_CBC_WITH_MD5
|     SSL2_RC4_128_EXPORT40_WITH_MD5
|     SSL2_RC4_128_WITH_MD5
|     SSL2_RC2_128_CBC_EXPORT40_WITH_MD5
|     SSL2_DES_192_EDE3_CBC_WITH_MD5
|     SSL2_RC4_64_WITH_MD5
|_    SSL2_DES_64_CBC_WITH_MD5
631/tcp  open  ipp      CUPS 1.1
| http-methods: 
|_  Potentially risky methods: PUT
|_http-server-header: CUPS/1.1
|_http-title: 403 Forbidden
3306/tcp open  mysql    MySQL (unauthorized)
MAC Address: 00:0C:29:71:C3:B8 (VMware)
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6
OS details: Linux 2.6.9 - 2.6.30
Network Distance: 1 hop

Host script results:
|_clock-skew: mean: -2h09m45s, deviation: 0s, median: -2h09m45s

TRACEROUTE
HOP RTT     ADDRESS
1   0.36 ms 172.16.8.134

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 31.98 seconds




