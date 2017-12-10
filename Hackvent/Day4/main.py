import os, binascii, struct

# the b opens file in binary mode
input_file = open('files/4C59', 'rb')
input_file_size = os.path.getsize('files/4C59')


try:
    byte = input_file.read(4)
    print(struct.unpack('>I', byte))
    # while byte != "":
    #     byte = input_file.read(1)
    #     print(byte)
finally:
    input_file.close()