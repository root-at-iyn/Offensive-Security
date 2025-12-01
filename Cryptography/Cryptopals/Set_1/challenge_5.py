#!/usr/bin/python3

# Implement repeating-key XOR

# Here is the opening stanza of an important work of the English language: 
# Burning 'em, if you ain't quick and nimble
# I go crazy when I hear a cymbal

# Encrypt it, under the key "ICE", using repeating-key XOR.
# In repeating-key XOR, you'll sequentially apply each byte of the key; the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on. 

# It should come out to: 
# 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f

# Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your mail. Encrypt your password file. Your .sig file. Get a feel for it. I promise, we aren't wasting your time with this. 


def repeating_key_xor(data: bytes, key: bytes) -> bytes:
    encrypted_bytes = b""
    _key = b""
    for b in range(len(data)):
        i = b % len(key)
        _key += key[i].to_bytes()
        encrypted_bytes += (data[b] ^ key[i]).to_bytes()
    return encrypted_bytes, _key

def solve_challenge_5():
    d = b"Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
    k = b"ICE"
    res, xor_key = repeating_key_xor(d, k)
    print(f"Plaintext: {d} ")
    print(f"Encrypted Target: 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f")
    print(f"Repeated XOR Key: {xor_key}")
    print(f"Repeating Key XOR Result: {res.hex()}")


if __name__ == "__main__":
    solve_challenge_5()

# Expected Output:
#
# root-at-iyn@Ubuntu-220403-x86-64:~/Cryptography/Cryptopals/Set1$ ./challenge_5.py 
# Plaintext: b"Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal" 
# Encrypted Target: 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
# Repeated XOR Key: b'ICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEIC'
# Repeating Key XOR Result: 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20690a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
