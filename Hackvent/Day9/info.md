#Day 09: JSONion
### ... is not really an onion. Peel it and find the flag.

[tom@devbox Day9]$ file JSONion.zip 
JSONion.zip: Zip archive data, at least v2.0 to extract

Unzipping give us a file:

[tom@devbox Day9]$ file jsonion.json 
jsonion.json: ASCII text, with very long lines, with no line terminators

Get some pretty ugly JSON back (first few lines):

[
    {
        "op": "map",
        "mapTo": "[{\"op:gzi,cnteH4sIADSTXjNal\\/8d9wCByr30Qh+FYPxvqVUOWR7f56Zb21kuJGKmLEM=}]",
        "content": "/8ge+gugqP5+glgze:K2:KgugFis\"MMMMMMMMMonzJU2ps\\{S6NvsmOk]ZIn}h}oM\"p\"L\"RYXqFqB5ZCWM4]C4+fOvFXDXW{Y==jSsqhJThsX0VW[W6N6NhWbb[W6N6N3W6NUFiP6N6NxJhTbS:a{iW6Nn2m3D3XvKfz=JT3}UXb{xSbG4Vib5V36NTFXbYIQesiQjz6N6Nv6N93C\\[vV{f[y94PVb3EwL6N,q,GFA3V+4Yk5a43ejUyR


so we have a structure with op, mapTo, content, mapFrom

the slashes look like escape sequences, wondering what this is.

Could be some object dumped to json, what structure uses op:map, mapTo, content and mapFrom?

JSON patch? RFC 6902 Does not really work though as we were only given one file

binwalk seems to think there is some data hidden in here?

[tom@devbox Day9]$ binwalk jsonion.json 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
253450        0x3DE0A         StuffIt Deluxe Segment (data): f2M+PvPf+C3dw,sJB}A]WAm5HFfZzjeoKVcn3}vOz12o}{Q,jOsb[6NBq6NqWKoL\"[14jTh}Ue\\jU\"\\SnBFihchfcIMFEc5}K,yAjweQvTPyTWKYsJc,cjV:IAIe
484298        0x763CA         StuffIt Deluxe Segment (data): fdQRx2soUVz3F6NXPaUq6NQf2zIsJwzR{s{kBodEmUyGDZ,vz}:v\"SFb]OzBjcv,K5:JvF]MLdY}qQsm{JMhIeA:Mi1J}6N+zRjmYkGAxj\"qOsFpc{Q:hIOv0G=M22
511693        0x7CECD         StuffIt Deluxe Segment (data): fpmK3kq4yB9VX]4+sQom6NGcIU1IYACseDMwYj6N5Ekb6Np[\"AfDGdF10,aV=iO+p04VYROm4Qkwb{35Yn33Uh\":MP0xvbxJ,cx]X\\KxRCYx=1iB,veAD:fnGc
810942        0xC5FBE         StuffIt Deluxe Segment (data): fFwY\\HV}kv\"O[,zn:fWddsUWaez0=sUHo31{q1kbKDCOsbc5KB4P\"ddIB4P9qVmAM:iziyzFXUE9a]cPEobPp04TfMxkK1WLH0]=KT:SQ3cJHiw,{EYcp6NL5xKE9
1313695       0x140B9F        StuffIt Deluxe Segment (data): f=mnV3\":Dw]Z}mUxeVqAxwPb1bHH\"wbfhRqXI]BX[:[{H4SUiWLoq44yX9wnSfk\"UqdP}31CX4v5HVT2qmOF}[0PJbyCUT}ezvfy2ESMO}YWRKov0vbF=P23FphpD


Lets extract?

Info on Stuffit Archives:

ftp://linuxmafia.com/kb/Apps/stuffit-archives.html

Trying to open with unar, this could be a false positive we just know it is compressed data
From quick google stuffit is old and not very supported format

Ok so assuming the binwalk stuffit is a false positive



