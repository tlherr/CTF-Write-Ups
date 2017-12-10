# Day 04: HoHoHo
## NOTE: New easyfied attachment available
## Hint: Santa has hidden something for you

Link is to a PDF document. File info:
HoHoHo_medium.pdf: PDF document, version 1.4

Checking it with binwalk:

```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PDF document, version: "1.4"
278           0x116           Zlib compressed data, default compression
1687          0x697           Unix path: /Subtype/Image/Type/XObject/Filter/FlateDecode/Width 179/Height 278/BitsPerComponent 8/Length 17539/ColorSpace/DeviceRGB/SMask 1
1831          0x727           Zlib compressed data, default compression
19416         0x4BD8          Unix path: /Subtype/Image/Type/XObject/Filter/FlateDecode/Width 179/Height 278/BitsPerComponent 8/Length 949/ColorSpace/DeviceGray>>stream
19545         0x4C59          Zlib compressed data, default compression
20583         0x5067          Zlib compressed data, default compression
30744         0x7818          Zlib compressed data, default compression
31451         0x7ADB          Unix path: /Type/EmbeddedFile/Subtype/text#2Fplain/Length 23780/Params<</Size 97873/CreationDate(D:20171204092920+01'00')/ModDate(D:2017120
31671         0x7BB7          Zlib compressed data, default compression
55554         0xD902          Zlib compressed data, default compression
56801         0xDDE1          Zlib compressed data, default compression
```

I dont know much about the PDF spec, the images make sense and the embeded file

Lets pull out the other stuff:

Scan Time:     2017-12-06 19:16:08
Target File:   /Users/tom/Documents/CTF-Write-Ups/Hackvent/Day4/_HoHoHo_medium.pdf.extracted/116
MD5 Checksum:  d92dae33e1b1f143e5eb8f202c197aa6
Signatures:    344

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------


Scan Time:     2017-12-06 19:16:08
Target File:   /Users/tom/Documents/CTF-Write-Ups/Hackvent/Day4/_HoHoHo_medium.pdf.extracted/727
MD5 Checksum:  e1f118bf4f059491d659e56c36db5d25
Signatures:    344

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------


Scan Time:     2017-12-06 19:16:08
Target File:   /Users/tom/Documents/CTF-Write-Ups/Hackvent/Day4/_HoHoHo_medium.pdf.extracted/4C59
MD5 Checksum:  4bdc41747f42ca6aac85e37abcb39887
Signatures:    344

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------


Scan Time:     2017-12-06 19:16:08
Target File:   /Users/tom/Documents/CTF-Write-Ups/Hackvent/Day4/_HoHoHo_medium.pdf.extracted/5067
MD5 Checksum:  92f930f551b9a7ae24bf0a1b527e585d
Signatures:    344

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------


Scan Time:     2017-12-06 19:16:08
Target File:   /Users/tom/Documents/CTF-Write-Ups/Hackvent/Day4/_HoHoHo_medium.pdf.extracted/7818
MD5 Checksum:  fffc62a8630884fa49129b242d173e06
Signatures:    344

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------


Scan Time:     2017-12-06 19:16:08
Target File:   /Users/tom/Documents/CTF-Write-Ups/Hackvent/Day4/_HoHoHo_medium.pdf.extracted/7BB7
MD5 Checksum:  98ed0a60368e68bb74e91dcb18bdf691
Signatures:    344

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
115           0x73            Copyright string: "Copyright: Digitized data copyright (c) 2007, Google Corporation."
141           0x8D            Copyright string: "copyright (c) 2007, Google Corporation."
15735         0x3D77          Copyright string: "copyright +AKkA 2007, Google Corporation." "" "" "FontForge 2.0 : Droid Sans Regular : 27-7-2017" "" "Version 1.00 build 114" """


Scan Time:     2017-12-06 19:16:08
Target File:   /Users/tom/Documents/CTF-Write-Ups/Hackvent/Day4/_HoHoHo_medium.pdf.extracted/D902
MD5 Checksum:  296a636f850a97eace0c4d049cac5b6f
Signatures:    344

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
231           0xE7            Unix path: /Type/Action/S/URI>>>><</Subtype/Link/Border[ 0 0 0]/Type/Annot/Rect[ 129.9 269.3 317.3 281]/A<</URI(https://en.wikipedia.org/wi


Scan Time:     2017-12-06 19:16:08
Target File:   /Users/tom/Documents/CTF-Write-Ups/Hackvent/Day4/_HoHoHo_medium.pdf.extracted/DDE1
MD5 Checksum:  709b6dcf4a8319bd418e311b1c959359
Signatures:    344


116:       ASCII text, with very long lines	from google search these appear to be pdf coordinates
116.zlib:  data
4C59:      DOS executable (device driver)	this appears to be best bet	
4C59.zlib: data
5067:      data
5067.zlib: data
727:       data
727.zlib:  data
7818:      ASCII text				cid to unicode map
7818.zlib: data
7BB7:      Spline Font Database  version 3.0
7BB7.zlib: data
D902:      data
D902.zlib: data
DDE1:      data
DDE1.zlib: data


DOS executable eh? what is in that? Checking in xxd there are lots of zeros at the top and lots of fs at the bottom, there must be some sort of pattern?
What is in the other files? Two files of ASCII text


7818 appears to be a cid to unicode map

Each row is 32 bits
what are the numbers from this
with no discernable header this file just appears to be raw binary data

tried reading it in various chunks such as 16 bits, 32 bits and 64 bits

How did binwalk know this is a windows binary? How would a linux binary look

readelf: 4C59: Error: Not an ELF file - it has the wrong magic bytes at the start

so it has the wrong magic bytes at the start

Can we run this thing, attach to a debugger or something?

