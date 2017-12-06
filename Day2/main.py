import os, base64
# Looking for key in format: HV17-xxxx-xxxx-xxxx-xxxx-xxxx

# This looks like base32 or base64 bit encoded text

path = 'Wishlist.txt'

chunk_start = 0
chunk_size = 32

file_size = os.path.getsize(path)
f = open(path,'r')


last_position = f.tell()

while last_position < file_size:
    # Read the first chunk
    f.seek(last_position + chunk_size)
    data = f.readlines(last_position)
    print(data)