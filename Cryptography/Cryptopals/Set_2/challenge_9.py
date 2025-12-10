#!/usr/bin/python3

# Implement PKCS#7 padding


def pkcs7(block: bytes, blocksize: int) -> bytes:
    if len(block) % blocksize != 0:
        padsize = blocksize - (len(block) % blocksize)
        padding = padsize.to_bytes() * padsize
        return block + padding 
    else:
        return block

if __name__ == "__main__":
    ys = b"YELLOW SUBMARINE AND 12345"
    blksize = 16
    print(pkcs7(ys, 16))
    print(f"Bytes Length: {len(ys)}")
    print(f"Pad Length: {blksize - (len(ys) % blksize)}")
    print(f"Block Size: {blksize}")


# Expected Output:

#root-at-iyn@Ubuntu-220403-x86-64:~/Cryptography/Cryptopals/Set2$ ./challenge_9.py
#b'YELLOW SUBMARINE AND 12345\x07\x07\x07\x07\x07\x07'
#Bytes Length: 26
#Pad Length: 6
#Block Size: 16

