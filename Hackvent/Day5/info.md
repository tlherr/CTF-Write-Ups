# Day 05: Only one hint
## OK, 2nd hint: Its XOR not MOD

### Here is your flag: 

```
0x69355f71
0xc2c8c11c
0xdf45873c
0x9d26aaff
0xb1b827f4
0x97d1acf4
```
and the one and only hint:
```
0xFE8F9017 XOR 0x13371337
```

Binary XOR (exclusive OR) operation has two inputs and one output.

For the hint if we take 

0xFE8F9017 (4270821399 in base10)
and XOR it with
0x13371337 (322376503 in base10)

we get 0xEDB88320 (3988292384 in base10)

We were given the flag Im assuming because we got 6 hexidecimal numbers and each flag is 6 groups of 4. So we can conclude that somehow we have to reduce each hex number to 4 characters?


With the hint we get 11101101101110001000001100100000 from the XOR so would that characters are:

11101101	237	ED
10111000	184	B8
10000011	131	83
00100000	32	20

As UFT8 - Garbage
As ASCII - Garbage


