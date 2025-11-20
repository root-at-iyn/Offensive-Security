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
