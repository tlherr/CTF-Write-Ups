# Day 03: Strange Logcat Entry

## Hint: Lost in messages
## Description: I found those strange entries in my Android logcat, but I don't know what it's all about... I just want to read my messages!

File: https://hackvent.hacking-lab.com/logcat.txt

logcat.txt: ASCII text, with very long lines
230K file with 3315 lines

Appears to be log from Genymotion android emulator

Guessing there is either a key hidden in some resource, noticing URLs (34 in total) or hidden as a hash or something?

Line 2749 is interesting:

11-13 20:40:24.044	137	  137  DEBUG: I 07914400000000F001000B913173317331F300003AC7F79B0C52BEC52190F37D07D1C3EB32888E2E838CECF05907425A63B7161D1D9BB7D2F337BB459E8FD12D188CDD6E85CFE931

We know we are looking for a 24 character key (29 including dashes). The above string is 145 characters and looks like a really long hash or something?

Lets try the urls

First one is: https://acdn.adnxs.com/as/1h/pages/wieistmeineip.js which according to the log is an "AST Library". Big file but there could be something burried in there. If we go to the actual https://www.wieistmeineip.ch/ website we can see the AST library loading so it appears fairly innocent at first glance.

Second URL is a log warning about unsafe javascript attempt, the url provided is: https://cdn1.smartadserver.com/diff/251/divscripte/c.html?ref=https://www.wieistmeineip.ch

script is pretty short but does appear to set some cookies, not seeing anything yet.

Next few are google tag manager scripts

The remainder are google ads that seem to go nowhere.

Another interesting segment of the log is the stack dump from an exception raised by libcore when it was unable to kill a process? What can we do with a stack trace? There is also a section of assembly

```assembly
eax ffffffe0  ebx 00000001  ecx bfd5925c  edx 0000004a
esi bfd5925c  edi bfd5925c
xcs 00000073  xds 0000007b  xes 0000007b  xfs 00000000  xss 0000007b
eip b7720406  ebp 00000001  esp bfd59210  flags 00000286
```

I have no idea if this is of any significance, being new to assembly I recognize registers and the 8 digits of hex making 32 bits.

Lost in messages
Found strange entries in my Android logcat, i just want to read my messages

What could the clue refer to:
	* Messages could refer to SMS, email or application messages
	* Some entries related to email, exchange
	* Messages could refer to RAW PDU MESSAGE

Checking SMS PDU: https://www.diafaan.com/sms-tutorials/gsm-modem-tutorial/online-sms-pdu-decoder/


BOOM IT WORKS


```
Text message
To:	
+13371337133
Message:	
Good Job! Now take the Flag: HV17-th1s-isol-dsch-00lm-agic
 
Additional information
PDU type:	
SMS-SUBMIT
Reference:	
0
SMSC:	
+44000000000
Val. format:	
None
Data coding:	
SMS Default Alphabet
 
Original Encoded PDU fields
SMSC:	
07914400000000F0
PDU header:	
01
TP-MTI:	
01
TP-RD:	
00
TP-VPF:	
00
TP-SRR:	
00
TP-UDHI:	
00
TP-RP:	
00
TP-MR:	
00
TP-DA:	
0B913173317331F3
TP-PID:	
00
TP-DCS:	
00
TP-UDL:	
3A
TP-UD:	
C7F79B0C52BEC52190F37D07D1C3EB32888E2E838CECF05907425A63
```

