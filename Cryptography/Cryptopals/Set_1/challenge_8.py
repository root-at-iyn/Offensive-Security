#!/usr/bin/python3

# Detect AES in ECB mode

# In this file are a bunch of hex-encoded ciphertexts.
# One of them has been encrypted with ECB.
# Detect it.

import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def get_filedata(filename: str) -> list:
    """
    Return a list of bytes for each line
    of hex encoded ciphertext
    """
    with open(filename) as fp:
        hex_ct_list = fp.readlines()
        return [bytes.fromhex(ct) for ct in hex_ct_list]

def transpose_blocks(ciphertext_list: list, blksize: int = 16):
    ciphertext_blocks = []
    for ct in ciphertext_list:
        blocks = [ct[blk:blk+blksize] for blk in range(0,len(ct),blksize)]
        ciphertext_blocks.append(blocks)
    return ciphertext_blocks

if __name__ == "__main__":
    data = (get_filedata("./8.txt"))
    t = transpose_blocks(data)
    for i in range(len(t)):
        if len(set(t[i])) != len(t[i]):
            print()
            print(f"ECB Detected!: Line {i}")
            for x in t[i]:
                print(x)
            for ct in t[i]:
                if t[i].count(ct) > 1:
                    print(f"Same {len(t[i][0])} byte ciphertext: {ct}")
                    break
            break

# Expected Output:
#
#root-at-iyn@Ubuntu-220403-x86-64:~/Cryptography/Cryptopals/Set1$ ./challenge_8.py
#
#ECB Detected!: Line 132
#b'\xd8\x80a\x97@\xa8\xa1\x9bx@\xa8\xa3\x1c\x81\n='
#b'\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83'
#b'\xe2\xdd\x05/kd\x1d\xbf\x9d\x11\xb04\x85B\xbbW'
#b'\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83'
#b'\x94u\xc9\xdf\xdb\xc1\xd4e\x97\x94\x9d\x9c~\x82\xbfZ'
#b'\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83'
#b'\x97\xa9>\xab\x8dj\xec\xd5fH\x91Tx\x9ak\x03'
#b'\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83'
#b'\xd4\x03\x18\x0c\x98\xc8\xf6\xdb\x1f*?\x9c@@\xde\xb0'
#b'\xabQ\xb2\x993\xf2\xc1#\xc5\x83\x86\xb0o\xba\x18j'
#Same 16 byte ciphertext: b'\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83'

