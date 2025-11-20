# Hashing

## Intro

Cryptographic hashes are designed to take any input small or large (e.g. file, text, etc) and represent it in a fixed size space. The result of this called a hash, digest, sum, checksum, or a fingerprint. For any cryptographic hashing algorithm it should have the following:

- **Preimage Resistance:** Given a digest, it should not be possible to derive the source input for that digest.
- **Second-Preimage Resitance:** If the source input for a single digest is known, it should not be possible to derive the source input for any other digest.
- **Collision Resistance:** It should be hard to find two source inputs that produce the same digest.
- **Avalanche Property:** A change to the source input should create a large and unpredictable change in the output (ideally >=50%  of the output bits should be modified). This also helps collision resistance.

## MD5

MD5 is a cryptgraphic algorithm that hashes source input producing an output of 16 bytes (128-bits). Generally, preimage resistance for an `n-bit` digest means you would expect an attacker to compromise the hash after `2**n`attempts, however, to find a collision it would only take `2**1/2n` attempts. This means for MD5 which has 128 bit digests, it should take within `2**64` attempts to find a collision. MD5's collision resistance has been found to be even worse in practice with other discovered attack techniques that could find collisions in fewer attempts than the expected `2**64`. This is one of the reasons why MD5 is considered broken. If MD5 is used for security purposes where the hash determines whether the source input is correct, a collision could be used fraudulently meet this check. For example, application passwords are usually stored in a database as a hashed value, so when a user authenticates to the app their input is run through the same hashing algorithm. If resulting the hash matches the hash in the database the user is authenticated. So if we can produce input that derives the same hash we would be authenticated. 


Another issue with MD5 is that it is deterministic, meaning the same source input always produces the same source output. This is also a problem for SHA-1 and SHA-256. Again using the password scenario, if the hashes are stolen from the database, and attacker could check password dumps for MD5 hashes that have already been cracked. Alternatively, they could get a wordlist of potential passwords and hash each one to see whether it produces the same hash. This would determine what the original password is likely to have been (minus any other possible collision). 


A soloution to mitigate deterministic hashes is to use salted hashes. Where salted hashes are concerned they prevent two users with the same password having the same hash (assuming the salt is unique for each user). However, salts are not secret and are saved with the hash in the database for each user. So if the hashes and salts are stolen and the user has a weak password, they could still be compromised using wordlists.


To demonstrate how password length and complexity affect time taken to invert a hash, I created a program that generates a permuatation of a ascii letters and numbers upto a max word length. The script uses randint to select an index from the permutation list and uses this as a preimage to the hash. Finally, another function is called to bruteforce the test hash by testing every possible permutation: 

```bash
root-at-iyn@Ubuntu-220403-x86-64:~/Cryptography/Hashing$ cat MD5BruteForcer.py
#!/usr/bin/python3

import hashlib
import random
import string
from datetime import datetime
from typing import Generator

def generate(alphabet: str|list, max_len: int) -> object:
    """
    Permutates a list or str to all
    possible combinations given
    """
    if max_len <= 0: return
    for c in alphabet:
        yield c
    for c in alphabet:
        for next in generate(alphabet, max_len -1):
            yield c + next

def getPreimageSeed(combinations: list, char_len: int) -> str:
    """Get a random preimage that is size char_len"""
    x = random.randint(0, len(combinations))
    if len(combinations[x]) == char_len:
        preimage = x
    else:
        getPreimageSeed(combinations, char_len)
    return combinations[preimage]

def getTestHash(preimage):
    return hashlib.md5(preimage).hexdigest()

def findHash(combinations: list, _hash: str):
    start = datetime.now()
    for c in combinations:
       print(f"Trying preimage: {c}")
       t = hashlib.md5(c.encode("utf-8")).hexdigest()
       print(f"Testing hash: {t}")
       if t == _hash:
           stop = datetime.now()
           print(f"Found hash: {_hash}")
           print(f"Time: {(stop - start)}")
           return

def main():
    l = 4
    cmb = [x for x in generate(string.ascii_letters + string.digits, l)]
    pImg = getPreimageSeed(cmb, l).encode("utf-8")
    print(f"Preimage: {pImg.decode('utf-8')}")
    test_hash = getTestHash(pImg)
    print(f"Test Hash: {test_hash}")
    print("")
    findHash(cmb, test_hash)
    print(len(cmb))

if __name__ == "__main__":
    main()
```

When setting the script to use a 4 character length preimage with the MD5 hashing algorithm, it only takes 4 minutes to find the hash:

```bash
Trying preimage: NTVM
Testing hash: e133b7ed7e0e03385b338d027b1d0f4e
Trying preimage: NTVN
Testing hash: e0c732e6abfa87ea275e730aa591f754
Trying preimage: NTVO
Testing hash: e0ff265bd431ea0d26e1a592a60982cc
Trying preimage: NTVP
Testing hash: 5c457d88d8d8ab5ae1f7251be2eea9e4
Trying preimage: NTVQ
Testing hash: f83b1b2bcc5f13fb9534b7feba4c688e
Trying preimage: NTVR
Testing hash: b830dd72d741a30e899a0c6237834e1a
Trying preimage: NTVS
Testing hash: 040d3584bc4daf3dc74fc6012ae9ff62
Trying preimage: NTVT
Testing hash: 722eb06d3c25eeca49bb7b7393a08456
Trying preimage: NTVU
Testing hash: fe88cf6d2f64bd16bfc8df7169723b92
Trying preimage: NTVV
Testing hash: bf64b56f1d9c6f82e34c41d5d7bb1627
Trying preimage: NTVW
Testing hash: 743b49e654e2865621dfa2db853f2c41
Trying preimage: NTVX
Testing hash: 998aadf01a8566ccae61cddd79c0b29b
Trying preimage: NTVY
Testing hash: 520b87dbba833c4f67381c7787b7565d
Trying preimage: NTVZ
Testing hash: 9da732a8529fd98e4a33a4370d248f46
Trying preimage: NTV0
Testing hash: 8becf366be11724e45c43f376c41ad73
Trying preimage: NTV1
Testing hash: 54d463e484de20b846a40d8e728c8459
Trying preimage: NTV2
Testing hash: 7258152ea59be8c52de040879fecd81f
Trying preimage: NTV3
Testing hash: b3e5c8cbfe376982d3238cbabe4fd938
Trying preimage: NTV4
Testing hash: 6972d241b3abb0f8c361cab145c5a996
Found hash: 6972d241b3abb0f8c361cab145c5a996
Time: 0:04:20.593597
```

