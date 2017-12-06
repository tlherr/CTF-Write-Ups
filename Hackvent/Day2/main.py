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


# Maybe it is bitmap image?
# No idea what size, and RGB vs grayscale etc

# img_size = 2
# max_img_size = 65536
# counter = 1
#
# img_types = ['I','F']
#
# while img_size < max_img_size:
#     for img_type in img_types:
#         print("Generating a {} x {} image of type {}".format(img_size, img_size, img_type))
#         out_image = Image.frombytes(img_type, (img_size, img_size), b64decodedstring)
#         if out_image.mode != 'RGB':
#             out_image = out_image.convert('RGB')
#         out_image.save("generated/foo{}x{}-{}.png".format(img_size, img_size, img_type))
#         img_size = pow(counter, 2)
#         counter += 1