#!/usr/bin/python3

# An ECB/CBC detection oracle

# Now that you have ECB and CBC working:
# Write a function to generate a random AES key; that's just 16 random bytes.
# Write a function that encrypts data under an unknown key --- that is, a function that generates a random key and encrypts under it.

# Under the hood, have the function append 5-10 bytes (count chosen randomly) before the plaintext and 5-10 bytes after the plaintext.
# Now, have the function choose to encrypt under ECB 1/2 the time, and under CBC the other half (just use random IVs each time for CBC). 
# Use rand(2) to decide which to use.
# Detect the block cipher mode the function is using each time. You should end up with a piece of code that, 
# pointed at a black box that might be encrypting ECB or CBC, tells you which one is happening.

import secrets
import random
from utils.ecb_ops import decrypt_ecb_data, encrypt_ecb_data
from utils.cbc_ops import decrypt_cbc_data, encrypt_cbc_data
from utils.padding import pkcs7_pad, pkcs7_unpad

def generate_key(keysize_bytes: int = 16) -> bytes:
    return secrets.token_bytes(keysize_bytes)

def encryption_oracle(plaintext: bytes) -> bytes:
    key = generate_key()
    blk_sz_bytes = 16
    prefix_bytes = random.randbytes(random.randint(5,10))
    postfix_bytes = random.randbytes(random.randint(5,10))
    selection = (random.randint(1,2))
    # data to encrypt
    pt = prefix_bytes + plaintext + postfix_bytes
    # cipher selection
    if selection == 1:
        #print("ECB Selected")
        return encrypt_ecb_data(pkcs7_pad(pt), key)
    elif selection == 2:
        #print("CBC Selected")
        return encrypt_cbc_data(pt, key, secrets.token_bytes(blk_sz_bytes))
    else:
        print("ERROR: Incorrect selection!")
        exit()

def detection_oracle(encryption_oracle: bytes, blk_sz: int = 16) -> bytes:
    blocks = [encryption_oracle[x:x+blk_sz] for x in range(0,len(encryption_oracle),16)]
    if blocks[1] == blocks[2]:
        print(f"ECB: {encryption_oracle}")
    else:
        print(f"CBC: {encryption_oracle}")
    return 

if __name__ == "__main__":
    # If we control the data then we can input >= 32 bytes of the same value,
    # which if encrypted by ECB will result in two 16 byte blocks of the same
    # ciphertext.
    # We need to account for the 5-10 random bytes prefixed before the plaintext
    # Assuming the minimum prefix bytes, we'd have to account for 11 bytes to complete
    # the first block, then append 2 * 16 byte blocks of our chosen plaintext, so
    # we need to send at least 43 bytes of plaintext to guarantee ECB detection
    attacker_controlled = b"A" * 43
    oracle = (encryption_oracle(attacker_controlled))
    detection_oracle(oracle)

# Expected Output:
#
#root-at-iyn@Ubuntu-220403-x86-64:~/Cryptography/Cryptopals/Set2$ for i in {1..7}; do ./challenge_11.py; done
#CBC: b'\xc1g\xfbN\xf2\xef[Z\xb4\x00\x1b\x0f\xfdbG\xf0\xdcJ\x06a#xp\xe0\xd3\xfag{\x12<S\xdfx\x95\\\x0e\x12\x99p\x93Z\xa0\x9e\xaa%G\xb7\xcb$\xf2 \x05\x87u}\xe2w\x98\xa7\x12v\xf63J'
#ECB: b'\xb3\xa0u\x87\xf9\xf1/\x14\x86g8\xa7\xb2\xe9\xec\\\xfa\xad3\xe7g\xb9\xac<\x9f\xe7\xa6\x19E\xebZ\x9b\xfa\xad3\xe7g\xb9\xac<\x9f\xe7\xa6\x19E\xebZ\x9bq\xbfV8z\xe8\xae\xea4\xe51\xc6\xa2\xbd\xd4 '
#ECB: b'=@\xc0\x18\x19\x82\x00B1\x90\n6\x9c._6>k\x8b\xcbC\x17\x83\xc5!\x81,\x9f\xe2}q\x01>k\x8b\xcbC\x17\x83\xc5!\x81,\x9f\xe2}q\x01\x0c\xd6\xc7\x08H\xa0,M\x01\xe0\xf2\xd2\xd5\x9c\x90\xe0'
#CBC: b'\xe0\xcf\x9fwe\xabUz\x84\xf4\xeb\xe6\x93B\xc2\x84\xe8\x84j\xfe\xca"*).\xba\x12\xa8\xd3\x84\xba\xa3\xee\xf8V]\xb4\xb1\xc4\x8e\xb2YY\xd7\xcam\xd9]\xa0\x88\xeb\xa4\xa3, z\x81\xce\x83E\x02\xf5\xad\x15'
#CBC: b'\x02M\x82\xb1\xd4\x83\xe4\xc8\xfb\xa5[\x1a^D*lZ\x00\x14\xef/\xf4\xca\xbb5\xe8\x13YN\xb0g\xd6\n\xf5\xb5\xe6\x16/u[\xb5\xbb\xf4\xde\xfe\xf3\x0fi\xcf\x04p\xf3\x12\x8c\xb02\x1a\xc0\xa9\xf5l\xa4\xd7\x8f'
#ECB: b'\xf1e(\xd0Y(" U"6\x865L(\xee2\x97\xe8\xd0!\xe2f\xd6\xb9\xa3*\xd87\x94\xfa\xc32\x97\xe8\xd0!\xe2f\xd6\xb9\xa3*\xd87\x94\xfa\xc3\x84}(\xbdIK\xa0\x0f\x92\x98\xf26\x95\x8f\x07\x83'
#ECB: b'HTfi\xe1>\x9e\xa9{\xb8J\x9a\x81\xdd0y\x0c\x14\x814fsp\xf9\xde\x06R\xd0\x97Wmd\x0c\x14\x814fsp\xf9\xde\x06R\xd0\x97Wmd`\xde\xe2;GJyq.j\x1a\x84\xf0\xa1\xe2%'

