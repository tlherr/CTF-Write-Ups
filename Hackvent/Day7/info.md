#Day 07: i know ...
## ... what you did last xmas
### We were able to steal a file from santas computer. We are sure, he prepared a gift and there are traces for it in this file. Please help us to recover it:

Given SANTA.FILE
```
SANTA.FILE: Zip archive data, at least v1.0 to extract
```
Which gives us

```
SANTA.IMA: DOS/MBR boot sector, code offset 0x58+2, OEM-ID "WINIMAGE", sectors/cluster 4, root entries 16, sectors 3360 (volumes <=32 MB), sectors/FAT 3, sectors/track 21, serial number 0x2b523d5, label: "           ", FAT (12 bit), followed by FAT
```
Mount it
```
mount /home/tom/Downloads/SANTA.IMA /mnt/santa -t msdos -o loop,fat=12,check=strict,uid=1000,gid=1000,debug
```

Gives us: santa~1.pri 

```
santa~1.pri: MS Windows registry file, NT/2000 or above
```

Found out chntpw has a registry editor which was nice, I ended up just using grep

```

Section containing string HV17!

```
000a6f80: 0300 0000 0100 592a 433a 5c48 6163 6b76  ......Y*C:\Hackv
000a6f90: 656e 745c 4856 3137 2d55 4379 7a2d 3079  ent\HV17-UCyz-0y
000a6fa0: 4555 2d64 3930 4f2d 7653 7153 2d53 6436  EU-d90O-vSqS-Sd6
000a6fb0: 342e 6578 65ee 4b05 e0ff ffff 766b 0400  4.exe.K.....vk..
```

Code: HV17-UCyz-0yEU-d90O-vSqS-Sd64
