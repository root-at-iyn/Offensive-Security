#!/usr/bin/python3

# FIXED XOR
# Write a function that takes two equal-length buffers and produces their XOR combination.
# If your function works properly, then when you feed it the string: 1c0111001f010100061a024b53535009181c
# ... after hex decoding, and when XOR'd against: 686974207468652062756c6c277320657965
# ... should produce: 746865206b696420646f6e277420706c6179

def fixed_xor(hex_str1: str, hex_str2) -> int:
    """Return the xor result of 2 hex encoded strings"""
    # XOR operation works on numbers only
    # so we convert the string to an int
    # using base 16 representation
    return int(hex_str1,16) ^ int(hex_str2,16)

def fixed_xor_bytes(b_str1: bytes, b_str2: bytes):
    """Return the xor result of 2 byte encoded strings"""
    res = int.from_bytes(b_str1) ^ int.from_bytes(b_str2)
    return res.to_bytes(length=len(b_str1))


if __name__ == "__main__":
    s1 = "1c0111001f010100061a024b53535009181c"
    s2 = "686974207468652062756c6c277320657965"
    
    # fixed_xor
    xor_str = fixed_xor(s1, s2)
    print(f"XOR'd String (Int as Hex): {hex(xor_str)}")
    print(f"XOR'd String as (UTF-8): {int.to_bytes(xor_str,length=32).decode("utf-8")}\n")

    # fixed_xor_bytes
    result = fixed_xor_bytes(bytes.fromhex(s1), bytes.fromhex(s2))
    print(f"XOR'd String (Bytes as Hex): {result.hex()}")
    print(f"XOR'd String (UTF-8): {result}")
    


# Expected output:
#root-at-iyn@Ubuntu-220403-x86-64:~/Cryptography/Cryptopals/Set1$ ./challenge_2.py 
#XOR'd String (Int as Hex): 0x746865206b696420646f6e277420706c6179
#XOR'd String as (UTF-8): the kid don't play
#
#XOR'd String (Bytes as Hex): 746865206b696420646f6e277420706c6179
#XOR'd String (UTF-8): b"the kid don't play"
#
