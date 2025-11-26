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
