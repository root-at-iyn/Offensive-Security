#!/usr/bin/python3

# Convert hex to base64
# The string: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# Should produce: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

# Cryptopals Rule:
# Always operate on bytes, never on encoded strings.
# Only use hex for pretty printing

import base64

def encode_b64(data: str) -> bytes:
    return base64.b64encode(bytes.fromhex(data))

if __name__ == "__main__":
    s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    s_b64encoded = encode_b64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
    print(f"Hex string to encode: {s}")
    print(f"Base64 hex string: {s_b64encoded.decode('utf-8')}")


#Expected output:
#root-at-iyn@Ubuntu-220403-x86-64:~/Cryptography/Cryptopals/Set1$ ./challenge_1.py 
#Hex string to encode: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
#Base64 hex string: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
