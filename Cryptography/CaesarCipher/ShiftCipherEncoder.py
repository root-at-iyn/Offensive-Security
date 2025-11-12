#!/usr/bin/python3

import string
import argparse


def shift_char(shift):
    shift_alphabet = [
    string.ascii_uppercase[(x + shift) % len(string.ascii_uppercase)] 
        for x in range(len(string.ascii_uppercase))
        ] # use modulus (%) to keep the alphabets the same length
    shift_map = {
            k:v for k,v in zip(string.ascii_uppercase, shift_alphabet)
            }
    return shift_map 


def encode(shift, message):
    shift_map = shift_char(shift)
    ciphertext = [shift_map[x] if x in shift_map.keys() else x for x in message.upper()]
    return "".join(ciphertext)


def decode(shift, ciphertext):
    shift_map = shift_char(shift)
    message = [
            # convert shift_map to list to use the index method
            # so we can find the key that maps to the value
            list(shift_map)[list(shift_map.values()).index(x)] 
            if x in shift_map.values() else x for x in ciphertext
            ]
    return "".join(message)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=["encrypt", "decrypt"], help="encrypt/decrypt operation")
    parser.add_argument("--shift", type=int, help="shift char by (n) chars", default=3)
    parser.add_argument("--message",type=str, help="message to encrypt", required=True)
    args = parser.parse_args()

    # encrypt ops
    if args.operation == "encrypt":
        print(encode(args.shift, args.message))
    # decrypt ops
    elif args.operation == "decrypt":
        print(decode(args.shift, args.message))
    # print usage catch-all
    else:
        parser.print_usage()


    
if __name__ == "__main__":
    main()


