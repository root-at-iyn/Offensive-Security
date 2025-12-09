#!/usr/bin/python3

import json
import string

# Detect single-character XOR
# One of the 60-character strings in this file has been encrypted by single-character XOR. 
# Find it. 


def single_byte_xor(b_str1: bytes, b_str2: bytes) -> str:
    """
    XOR's each byte of a byte encoded string `b_str1`
    with byte string `b_str2`
    """
    x = b""
    for b in b_str1:
        x += (b ^ int.from_bytes(b_str2)).to_bytes(length=len(b_str2))
    return x

def find_key(hex_str: str) -> list:
    """
    Finds the single character key used to XOR encrypt
    a hex encoded string
    """
    decoded_strings = []
    chars = string.digits.encode("utf-8")
    for char in chars:
        decoded_strings.append(single_byte_xor(bytes.fromhex(hex_str), char.to_bytes() ))

    return decoded_strings

def decrypt_single_char_xor():
    with open("./Data/4.txt") as f:
        hex_strings = [x.rstrip() for x in f]
    
    decoded_hex_strings = []
    for line in hex_strings:
        decoded_hex_strings.append(find_key(line))
    utf8_strs = [] 
    for i in decoded_hex_strings:
        for j in i:
            try:
                utf8_strs.append(j.decode("utf-8"))
            except UnicodeDecodeError as e:
                pass
    decoded_str_map = {k: {"length":0, "words":[]} for k in utf8_strs}
    with open("./Data/words_dictionary.json") as wordlist:
        for w in json.load(wordlist):
            for s in decoded_str_map.keys():
                if w in s.lower():
                    decoded_str_map[s]["words"].append(w)
                    decoded_str_map[s]["length"] += 1


    return decoded_str_map

if __name__ == "__main__":
    res = decrypt_single_char_xor()
    count = 0
    message = ""
    for k in res:
        #print(f"{k}: length: {res[k]['length']}")
        if res[k]["length"] > count:
            count = res[k]["length"]
            message = k
    print(f"Decrypted Message: {message}")
    

# Expected output
#
#root-at-iyn@Ubuntu-220403-x86-64:~/Cryptography/Cryptopals/Set1$ ./challenge_4.py
#Decrypted Message: Now that the party is jumping


