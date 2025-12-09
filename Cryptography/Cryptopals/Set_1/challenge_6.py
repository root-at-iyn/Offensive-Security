#!/usr/bin/python3

# Break repeating-key XOR

# There's a file here. It's been base64'd after being encrypted with repeating-key XOR.
# Decrypt it. 

import base64
import string
import math
from challenge_3 import single_byte_xor

def get_file_data(filename: str) -> bytes:
    with open(filename, 'rb') as fp:
        data = base64.b64decode(fp.read())
        return data

def hamming_distance(b_str1: bytes, b_str2: bytes) -> dict:
    """Computes the hamming distance between two sets of bytes"""
    if len(b_str1) != len(b_str2):
        print(f"Error: The byte buffers must be the same length")
        exit()
    str1 = [[] for x in b_str1] # show value of each bit set per byte
    str2 = [[] for x in b_str2] # show value of each bit set per byte
    distance = 0 
    for byte in range(len(str1)):
        for bit_position in range(8):
            s1 = (b_str1[byte] & (1 << bit_position))
            s2 = (b_str2[byte] & (1 << bit_position))
            if s1 != s2:
                distance += 1
            str1[byte].append(s1)
            str2[byte].append(s2)
    h_map = {"hamming":distance,"s1":str1,"s2":str2}
    return distance

def get_blk_hamming_normalised(block: bytes, keylen: int) -> int:
    """
    Gets the hamming distance between two keylen sized 
    blocks of block and returns noralised value
    Max keylen is half of block length
    """
    # Error checks
    if keylen > len(block)/2:
        print(f"Error: keylen greater than 1/2 block length")
        exit()
    if len(block) < 1:
        print(f"Error: block length must be greater than 1")
    # Work
    blk_range = math.floor(len(block) / keylen)
    hd = 0
    for i in range(blk_range):
        blk1 =  block[keylen*i:keylen*i+keylen]
        blk2 =  block[keylen*i+keylen:keylen*i+(2*keylen)]
        if len(blk1) != len(blk2):
            break
        res = hamming_distance(blk1, blk2)
        hd += res/keylen
    return hd/blk_range

def find_repkey_xor_keysize(block: bytes, begin: int, end: int) -> int:
    """
    Find the probable repeating-xor key-length 
    for a range of lengths from begin to end"""
    keysize_map = {i:0 for i in range(begin, end, 1)}
    for kl in keysize_map:
        keysize_map[kl] = get_blk_hamming_normalised(block, kl)
    min_normalised = min(keysize_map.values())
    # convert dict to list to get orginal key from value
    keysize = list(keysize_map)[ list(keysize_map.values()).index(min_normalised) ]
    return keysize 

def transpose_blocks(block: bytes, keylen: int) -> list:
    """
    Transpose block into keylen number of blocks
    with each byte of block round-robined between
    number of blocks
    """
    blks = []
    idx = 0
    for i in range(len(block)):
        if i % keylen == 0:
            blks.append([])
            blks[idx].append(block[i].to_bytes())
            idx += 1
        else:
            blks[idx-1].append(block[i].to_bytes())
    ordered_blks = [[] for x in range(keylen)]
    for blk in blks:
        for byte in range(len(blk)):
            ordered_blks[byte % keylen].append(blk[byte].hex())
    transposed = ["".join(x) for x in ordered_blks]
    return transposed

def decode_transposed_str(transposed_list: list, char: int) -> list:
    decoded_strings = []
    for hex_str in transposed_list:
        decoded_strings.append(single_byte_xor(bytes.fromhex(hex_str), char.to_bytes()).encode("utf-8"))
    return decoded_strings 

def find_key(transposed: list, keylen: int, search_chars: str = string.ascii_uppercase) -> bytes:
    """
    Enumerates the key based on ascii letter frequency 
    from decrypted blocks"""
    decryption_keys = {k:[] for k in search_chars}
    KEY = [{"char":"","count":1000000} for x in range(keylen)]
    for char in search_chars:
        decoded = decode_transposed_str(transposed, ord(char))
        decoded_map_list = []
        for i in range(len(decoded)):
            d_map = {i:{"decoded":decoded[i], "count":0}}
            ascii_range = [x for x in range(32,123)]
            ascii_punctuation = [x for x in string.punctuation.encode("utf-8")]
            decoded_ascii_num = [x for x in decoded[i]]
            good_chars = [ord("'"), ord(","), ord("!"), ord("\n")] 
            for n in decoded_ascii_num:
                if (n not in ascii_range) and (n != ord("\n")):
                   d_map[i]["count"] += 100
                if n in ascii_punctuation:
                    if n not in good_chars:
                        d_map[i]["count"] += 10
                    else:
                        d_map[i]["count"] += 1
            decoded_map_list.append(d_map)
            if d_map[i]["count"] < KEY[i]["count"]:
                KEY[i]["char"] = char
                KEY[i]["count"] = d_map[i]["count"]
        decryption_keys[char].extend(decoded_map_list)
    return "".join([KEY[x]["char"] for x in range(len(KEY))]).encode("utf-8")


def decrypt(encrypted_data: bytes, key: bytes) -> bytes:
    decrypted_bytes = b""
    for b in range(len(encrypted_data)):
        i = b % len(key)
        decrypted_bytes += (encrypted_data[b] ^ key[i]).to_bytes()
    return decrypted_bytes


if __name__ == "__main__":

    blk = get_file_data("./Data/6.txt")
    key_size = find_repkey_xor_keysize(blk, 1, 41)
    t = transpose_blocks(blk,key_size)
    key = find_key(t,key_size,search_chars=string.printable)
    print(f"====== KEY ======")
    print(f"{key}\n")
    print(f"====== DECRYPTED DATA =======")
    print(decrypt(blk, key).decode("utf-8"))


# Expected Output:
#root-at-iyn@Ubuntu-220403-x86-64:~/Cryptography/Cryptopals/Set1$ ./challenge_6.py
#====== KEY ======
#b'Terminator X: Bring the noise'
#
#====== DECRYPTED DATA =======
#I'm back and I'm ringin' the bell
#A rockin' on the mike while the fly girls yell
#In ecstasy in the back of me
#Well that's my DJ Deshay cuttin' all them Z's
#Hittin' hard and the girlies goin' crazy
#Vanilla's on the mike, man I'm not lazy.
#
#I'm lettin' my drug kick in
#It controls my mouth and I begin
#To just let it flow, let my concepts go
#My posse's to the side yellin', Go Vanilla Go!
#
#Smooth 'cause that's the way I will be
#And if you don't give a damn, then
#Why you starin' at me
#So get off 'cause I control the stage
#There's no dissin' allowed
#I'm in my own phase
#The girlies sa y they love me and that is ok
#And I can dance better than any kid n' play
#
#Stage 2 -- Yea the one ya' wanna listen to
#It's off my head so let the beat play through
#So I can funk it up and make it sound good
#1-2-3 Yo -- Knock on some wood
#For good luck, I like my rhymes atrocious
#Supercalafragilisticexpialidocious
#I'm an effect and that you can bet
#I can take a fly girl and make her wet.
#
#I'm like Samson -- Samson to Delilah
#There's no denyin', You can try to hang
#But you'll keep tryin' to get my style
#Over and over, practice makes perfect
#But not if you're a loafer.
#
#You'll get nowhere, no place, no time, no girls
#Soon -- Oh my God, homebody, you probably eat
#Spaghetti with a spoon! Come on and say it!
#
#VIP. Vanilla Ice yep, yep, I'm comin' hard like a rhino
#Intoxicating so you stagger like a wino
#So punks stop trying and girl stop cryin'
#Vanilla Ice is sellin' and you people are buyin'
#'Cause why the freaks are jockin' like Crazy Glue
#Movin' and groovin' trying to sing along
#All through the ghetto groovin' this here song
#Now you're amazed by the VIP posse.
#
#Steppin' so hard like a German Nazi
#Startled by the bases hittin' ground
#There's no trippin' on mine, I'm just gettin' down
#Sparkamatic, I'm hangin' tight like a fanatic
#You trapped me once and I thought that
#You might have it
#So step down and lend me your ear
#'89 in my time! You, '90 is my year.
#
#You're weakenin' fast, YO! and I can tell it
#Your body's gettin' hot, so, so I can smell it
#So don't be mad and don't be sad
#'Cause the lyrics belong to ICE, You can call me Dad
#You're pitchin' a fit, so step back and endure
#Let the witch doctor, Ice, do the dance to cure
#So come up close and don't be square
#You wanna battle me -- Anytime, anywhere
#
#You thought that I was weak, Boy, you're dead wrong
#So come on, everybody and sing this song
#
#Say -- Play that funky music Say, go white boy, go white boy go
#play that funky music Go white boy, go white boy, go
#Lay down and boogie and play that funky music till you die.
#
#Play that funky music Come on, Come on, let me hear
#Play that funky music white boy you say it, say it
#Play that funky music A little louder now
#Play that funky music, white boy Come on, Come on, Come on
#Play that funky music

