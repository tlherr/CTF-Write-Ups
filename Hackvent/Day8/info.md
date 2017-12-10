# Day 08: True 1337s
## ... can read this instantly
### I found this obfuscated code on a public FTP-Server. But I don't understand what it's doing...

Get file that runs exec and chr functions, I know php has both of those and does strange shit with type conversions. Lets try it

Nothing, perhaps python?

chr(i)
Return a string of one character whose ASCII code is the integer i. For example, chr(97) returns the string 'a'. This is the inverse of ord(). The argument must be in the range [0..255], inclusive; ValueError will be raised if i is outside that range. See also unichr().

>>> chr(True)
'\x01'

>>> chr(True+True)
'\x02'


So the first part turns into:

'\nA=chr;__1337=exec;SANTA=input;FUN=print\ndef _1337(B):return A(B//1337)'

Followed by a newline character

So we now know that __1337 means exec, SANTA is the input, not sure what FUN=print means, I guess we just want to print it. We also know that we have a function defined as

_1337(B): return A(B//1337)


Now the second half starts to make sense so if we just print it out we get

C=SANTA("?")
if C=="1787569":FUN(''.join(chr(ord(a) ^ ord(b)) for a,b in zip("{gMZF_MC_X\ERF[X","31415926535897932384626433832")))

