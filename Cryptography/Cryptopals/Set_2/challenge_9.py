#!/usr/bin/python3

# Implement PKCS#7 padding


def pkcs7_pad(data: bytes, blocksize: int = 16) -> bytes:
    padsize = blocksize - (len(data) % blocksize)
    padding = padsize.to_bytes() * padsize
    return data + padding 

def pkcs7_unpad(data: bytes) -> bytes:
    last_byte = data[-1]
    if data.endswith(bytes(chr(last_byte).encode('ascii') *last_byte)):
        return data[:-last_byte]

if __name__ == "__main__":
    ys = b"YELLOW SUBMARINE"
    blksize = 16
    print(pkcs7_pad(ys))
    print(f"Bytes Length: {len(ys)}")
    print(f"Pad Length: {blksize - (len(ys) % blksize)}")
    print(f"Block Size: {blksize}")
    print(f"Data Unpadded: {pkcs7_unpad(pkcs7_pad(ys))}")


# Expected Output:

#root-at-iyn@Ubuntu-220403-x86-64:~/Cryptography/Cryptopals/Set2$ ./challenge_9.py
#b'YELLOW SUBMARINE AND 12345\x07\x07\x07\x07\x07\x07'
#Bytes Length: 26
#Pad Length: 6
#Block Size: 16

