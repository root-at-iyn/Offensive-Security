#!/usr/bin/python3

# FIXED XOR
# Write a function that takes two equal-length buffers and produces their XOR combination.
# If your function works properly, then when you feed it the string: 1c0111001f010100061a024b53535009181c
# ... after hex decoding, and when XOR'd against: 686974207468652062756c6c277320657965
# ... should produce: 746865206b696420646f6e277420706c6179

def fixed_xor(hex_str1: str, hex_str2) -> int:
    return int(hex_str1,16) ^ int(hex_str2,16)

if __name__ == "__main__":
    s1 = "1c0111001f010100061a024b53535009181c"
    s2 = "686974207468652062756c6c277320657965"
    xor_str = fixed_xor(s1, s2)
    print(hex(xor_str))


# Expected output:
# root-at-iyn@Ubuntu-220403-x86-64:~/Cryptography/Cryptopals/Set1$ ./challenge_2.py 
# 0x746865206b696420646f6e277420706c6179

