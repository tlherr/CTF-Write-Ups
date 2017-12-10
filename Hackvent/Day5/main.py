import binascii

flags = [
    0x69355f71,
    0xc2c8c11c,
    0xdf45873c,
    0x9d26aaff,
    0xb1b827f4,
    0x97d1acf4
]

hint = [
    0xFE8F9017,
    0x13371337
]


if __name__ == "__main__":

    hint_result = bin(hint[0] ^ hint[1])[2:]
    print(hint_result)
    print(hint_result[:8])
    print(hint_result[8:16])
    print(hint_result[16:24])
    print(hint_result[24:32])
