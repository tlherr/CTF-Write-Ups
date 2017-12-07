import os

# Read binary file as input
# Read every 32 bits and convert it to a decimal number then print it

input_file = open('files/4C59', 'r')
input_file_size = os.path.getsize('files/4C59')
l_pos = input_file.tell()
r_pos = input_file.seek(32)

while(input_file.seekable()):
    print()