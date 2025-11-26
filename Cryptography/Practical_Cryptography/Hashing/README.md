# Hashing

## Intro

Cryptographic hashes are designed to take any input small or large (e.g. file, text, etc) and represent it in a fixed size space. The result of this called a hash, digest, sum, checksum, or a fingerprint. For any cryptographic hashing algorithm it should have the following:

- **Preimage Resistance:** Given a digest, it should not be possible to derive the source input for that digest.
- **Second-Preimage Resitance:** If the source input for a single digest is known, it should not be possible to derive the source input for any other digest.
- **Collision Resistance:** It should be hard to find two source inputs that produce the same digest.
- **Avalanche Property:** A change to the source input should create a large and unpredictable change in the output (ideally >=50%  of the output bits should be modified). This also helps collision resistance.

## MD5

MD5 is a cryptgraphic algorithm that hashes source input producing an output of 16 bytes (128-bits). Generally, preimage resistance for an `n-bit` digest means you would expect an attacker to compromise the hash after `2**n`attempts, however, to find a collision it would only take `2**1/2n` attempts. This means for MD5 which has 128 bit digests, it should take within `2**64` attempts to find a collision. MD5's collision resistance has been found to be even worse in practice with other discovered attack techniques that could find collisions in fewer attempts than the expected `2**64`. This is one of the reasons why MD5 is considered broken. If MD5 is used for security purposes where the hash determines whether the source input is correct, a collision could be used fraudulently meet this check. For example, application passwords are usually stored in a database as a hashed value, so when a user authenticates to the app their input is run through the same hashing algorithm. If resulting the hash matches the hash in the database the user is authenticated. So if we can produce input that derives the same hash we would be authenticated. 


Another issue with MD5 (also SHA-1 and SHA-256) is that it is deterministic, meaning the same source input always produces the same source output. Again using the password scenario, if the hashes are stolen from the database, and attacker could check password dumps for MD5 hashes that have already been cracked. Alternatively, they could get a wordlist of potential passwords and hash each one to see whether it produces the same hash. This would determine what the original password is likely to have been (minus any other possible collision). 


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

## Hashing used in Proof of Work (Blockchain)

Hashing is used as a way proving the integrity of data, due to the difficulty of inverting the hash to find the source input. If I send you a piece of data over an untrusted network like the internet, its possible it could be modified in transit. To verify it hasn't been modified, I could compute the hash of the data using a cryptographic algorithm (e.g. SHA-256) and provide this to you out-of-band (e.g. my public website). When you receive the data I sent you, you would be able to confirm it has not been tampered with by using SHA-256 to compute the hash of the data and comparing it to the out-of-band hash. 


For similar reasons Bitcoin uses SHA-256 in the Bitcoin network to preserve the integrity of transactions and to verify valid blocks in the blockchain. Each hashed transaction is encrypted with the user's private key to produce a digital signature. A transaction is stored within a block which also includes some metadata, and the overall block structure is preserved by a hash. The transaction data within the block is hashed with other transaction data which produces a Merkle Tree structure. For example, say we have 4 transactions T1, T2, T3, and T4, the tree would look like as follows: 

|Hash |Src Data |
|-----|---------|
|H(T1)|T1       |
|H(T2)|T2       |
|H(T3)|T3       |
|H(T4)|T4       |

These transactions would be classed as leaf nodes and would hashed with other leaf nodes the root node is reached:

|Hash     |Src Data     |
|---------|-------------|
|H(T1+T2) |H(T1) + H(T2)|
|H(T3+T4) |H(T3) + H(T4)|
|H(T1+T2+T3+T4)|H(T1+T2) + H(T3+T4)|

The Merkle Root (hash) is added to the block header, so if anyone tries to modify the blocks transactions it will invalidate the block because the Merkle Root of the data will no longer match the header. 


Now the blockchain user can request to make this transaction apart of the distributed ledger. The transactions and the hash of the previous block are added to a new candidate block. For the block to be accepted it must solve a cryptographic puzzle which is called a Proof of Work. The users transaction request is sent to miners who are willing to solve the puzzle to get rewarded bitcoin in return. The puzzle is designed to be computationally expensive, enough so that on average it takes around 10 min to solve for the target. The target is a particular number which is a power of 2, and the puzzle is solved by finding a SHA-256 hash of the candidate block that is numberically under that value. Since SHA-256 hashes are designed to compute bits randomly throughout the 32 bytes of space, finding a hash that is numerically less than a particular power of 2 increases in diffculty as the powers of 2 decrease. For example it will be quick to find a hash under `2**256`-1 since SHA-256 has a max of `(2**256)-1`. It would take 1 try on average. However, solving for a hash under `(2**240)-1` would take longer. The lower the power of 2 down from 256 the more leading zeros a hash will need to start with to solve the puzzle. At the time of writing the [current target](https://learnmeabitcoin.com/explorer/924643) is `00000000000000000001d9360000000000000000000000000000000000000000` which is 19 leading 0's (or the 1st 76 bits), meaning a valid hash will be a under `2**176`. 


Since the data in the block must remain the same, the miner has to use a (nonce) random value on each hash attempt to find the target. When the puzzle is solved the miner sends the hashed block to the blockchain and other participants validate the block by checking the hash solves the target number, which is quick to check. Once verified, the block has reached consensus and the block is added to the blockchain. 


### Proof of Work Example

To simulate a proof of work example, I created a program that generates random bytes (block data) and an initial nonce. The two are hashed together with SHA-256 in an attempt to find a number under `2**236`. If the first attempt fails the process is repeated with nonce being incremented and hashed again with the block data until an output hash is numerically lower than the target.

*ProofOfWork.py*

```python
#!/usr/bin/python3

import hashlib
import secrets

def compute_hash(ctr: bytes, data: bytes) -> bytes:
    digest = hashlib.sha256(ctr + data)
    return digest

def find_target(ctr: bytes, target: int):
    block_data = secrets.token_bytes(1024)
    candidate = compute_hash(
            ctr.to_bytes(length=4),
            block_data
            ).digest()
    while (int.from_bytes(candidate) > target):
        print(candidate.hex())
        ctr += 1
        candidate = compute_hash(
                ctr.to_bytes(length=4),
                block_data
                ).digest()
    print(candidate.hex())
    print(f"\nHashes: {ctr}")
    return int.from_bytes(candidate)


if __name__ == "__main__":
    counter = 0
    target = (2**236)-1
    print(f"Found!: {hex(find_target(counter, target))}")
    print(f"Target: {hex(target)}")
```

When the script is run it prints each hash attempt to find the target, the number of hashes attempted, and the final hash that met the criteria:

```bash
---- SNIPPED OUTPUT ----
91fa1c54a290aa9b918aa62aa79fd17d06dff60e2228ea6d97b927c56a91897a
e685e71bb2542b7a2726f2f9d5542b24ff7de831b7f778615b572d654b5ec3d7
c08a5fb8466f5d9f7ba0addbb91db88d1d929cce37a873afe2766a1030762d7e
f1a474e76aba2aa56c404d6b70cd87e55810f0678f407b12ea3efae30c8b5e40
40da976f76b96db293fd1939a05c026e70194ce4dbffba8058efb2cdbe4e4218
ba07b96ff674539267825c8b9b746618a6f74addd8188d1552623a34f3cd8185
657b440dc9d121cb48374ec9f68860496ef434b9bc17f5031b1fdb3b4eae103d
71a548bb73650901a5abc8b930d47bdf07e68d22fdd5f021056bebeaf87e4686
ee4dead42a0f747eff0a3f35d1d844962cddf5e352a3863d11ef00e6aaad583a
86a2dbdb5f8aed6078c5d3f1a5fa8b5de6ccb293d1dc56a1801d7e55ffdeabb3
bdc90be8ac9cc0b1ccaa2f21265f52ee7d010e929f50e5913fa9e35b0c9a9464
981a332caa3e1835d101b0cee3826ed247620ceeb4cc4d753ba6c64f721accb0
6ceb0e9126bf3d0f6ab6a74631a508c483a7301c51709c75d63671f6746e2fef
71b9f0a9769506f3d8df79cd1d168a5b3d9b6f7d48b484a1513e1add9d5c9c75
78925500a594736ff2ebe98181ffb853c667d59d5db02c0b49f018fa05427eec
b9f3d3b2eda9577956e2ed8446ffc56e448b70e74441b946a1b105e7243b8eef
9c38247a0708341e57031c60deaa88019fafdbab598ca7099f4a3369a8c2814c
fad8ad112c4845a3f32423c85232aae2cbe5fcac51b5c84bbb2afb7e210f6227
7d6d8b7fea26a8a7039931647c870253812f22c93af51614e499d83f53bb4b8d
00000a786692b3bf635a5160221fc83fefb1d7fe2de99ad41f014092adb7c6af

Hashes: 1808245
Found!: 0xa786692b3bf635a5160221fc83fefb1d7fe2de99ad41f014092adb7c6af
Target: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
```
