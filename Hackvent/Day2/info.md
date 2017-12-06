# Day 2

Given link to a file that appears to be encrypted/encoded wishlist
Clue given: The fifth power of two

2^5 is 32

Just looking at this text it looks like base64 encoding (no special chars, only upper/lower alpha
and digits). Also notice == at the end which I am guessing is padding. From Wikipedia:
"The '==' and '=' sequence indicate that the last group contained only 8 or 16 bits, respectively."

What happens if we just treat it as base64
```
cat Wishlist.txt | base64 --decode
```

Still have a giant mess of ASCII text, what if this was an image?

Have no idea what size it should be. If it were a bitmap how large would it be? Assuming 32 bits per pixel

```
[tom@devbox Day2]$ cat Wishlist.txt | base64 --decode | wc -c
400567
```

4005667 bytes so if we assume 32 bits per pixel that would give us 12517.71875 possible pixel values. This would mean largest
32 bit image would could produce would be 104976 or 324 x 324 (assuming it is a square), the lack of a 
round number is concerning. From the pillow docs we can use the following modes:

    1 (1-bit pixels, black and white, stored with one pixel per byte)
    L (8-bit pixels, black and white)
    P (8-bit pixels, mapped to any other mode using a color palette)
    RGB (3x8-bit pixels, true color)
    RGBA (4x8-bit pixels, true color with transparency mask)
    CMYK (4x8-bit pixels, color separation)
    YCbCr (3x8-bit pixels, color video format)
        Note that this refers to the JPEG, and not the ITU-R BT.2020, standard
    LAB (3x8-bit pixels, the L*a*b color space)
    HSV (3x8-bit pixels, Hue, Saturation, Value color space)
    I (32-bit signed integer pixels)
    F (32-bit floating point pixels)

Also potential for filters like bilinear etc.

Pillow lists the following as fully supported filetypes:

    BMP
    EPS
    GIF
        Reading sequences
        Saving sequences
        Reading local images
    ICNS
    IM
    JPEG
    JPEG 2000
    MSP
    PCX
    PNG
    PPM
    SPIDER
        Writing files in SPIDER format
    TIFF
        Saving Tiff Images
    WebP
    XBM

Ok images not working, lets rethink this. The only clue we have been given is 32. So far we have assumed that 32 is
bits per pixel etc but what if 32 was the number of times a string was base64 encoded?

```python
import os, base64

input_file_path = 'Wishlist.txt'

input_file = open(input_file_path, 'r')
input_file_data = input_file.read()

input_bytes = bytes(input_file_data, 'ASCII')
input_file.close()
result = ''

# Run the decoding 32 times
for i in range(1, 33):
    if i == 1:
        result = base64.decodebytes(input_bytes)
    else:
        result = base64.decodebytes(result)

print(result)
```

HV17-Th3F-1fth-Pow3-r0f2-is32

IT WORKS!