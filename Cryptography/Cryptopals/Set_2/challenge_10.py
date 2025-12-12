#!/usr/bin/python3

# Implement CBC mode

# Implement CBC mode by hand by taking the ECB function you wrote earlier, 
# making it encrypt instead of decrypt (verify this by decrypting whatever you encrypt to test), 
# and using your XOR function from the previous exercise to combine them. 

# The file here is intelligible (somewhat) when CBC decrypted against 
# "YELLOW SUBMARINE" with an IV of all ASCII 0 (\x00\x00\x00 &c) 

import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from challenge_9 import pkcs7_pad, pkcs7_unpad

def get_filedata(filename: str) -> bytes:
    with open(filename, "rb") as fp:
        data = fp.read()
    return base64.b64decode(data)

def pkcs7(block: bytes, blocksize: int) -> bytes:
    if len(block) % blocksize != 0:
        padsize = (blocksize - len(block) % blocksize)
        padding = padsize.to_bytes() * padsize
        return block + padding 
    else:
        return block

def decrypt_cbc_data(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    blocksize = 16
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()
    iv_int = int.from_bytes(iv)
    pt0_int = int.from_bytes(decryptor.update(ciphertext[0:blocksize]))
    plaintext = (pt0_int ^ iv_int).to_bytes(length=blocksize)
    for ct in range(blocksize,len(ciphertext),blocksize):
        pt_blk_i_int = int.from_bytes(decryptor.update(ciphertext[ct:ct+blocksize]))
        ct_blk_i_int = int.from_bytes(ciphertext[(ct-blocksize):(ct-blocksize)+blocksize])
        plaintext += (pt_blk_i_int ^ ct_blk_i_int).to_bytes(length=blocksize) 
    return  pkcs7_unpad(plaintext + decryptor.finalize()).decode('ascii')
    

def encrypt_cbc_data(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    blocksize = 16
    pt = pkcs7_pad(plaintext) # padded plaintext
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    pt_blk_0_int = int.from_bytes(pt[0:blocksize])
    iv_int = int.from_bytes(iv)
    ciphertext = encryptor.update((pt_blk_0_int ^ iv_int).to_bytes(length=blocksize))
    for block in range(blocksize,len(pt),blocksize):
        pt_blk_i_int = int.from_bytes(pt[block:(block+blocksize)])
        ct_blk_i_int = int.from_bytes(ciphertext[(block-blocksize):(block-blocksize)+blocksize])
        pt_ct_xor = (pt_blk_i_int ^ ct_blk_i_int).to_bytes(length=blocksize)
        ciphertext += encryptor.update(pt_ct_xor)
    return ciphertext + encryptor.finalize()
        
if __name__ == "__main__":
    IV = b"\x00"*3
    KEY = b"YELLOW SUBMARINE"
    PT1 = get_filedata("./test.txt")
    ENC_DATA = get_filedata("./10.txt")
    CT1 = encrypt_cbc_data(PT1, KEY, IV)
    print(f"Decrypted Plaintext 1:\n{decrypt_cbc_data(CT1, KEY, IV)}")
    print(f"Decrypted Plaintext 2:\n{decrypt_cbc_data(ENC_DATA, KEY, IV)}")


# Expected Output:

#root-at-iyn@Ubuntu-220403-x86-64:~/Cryptography/Cryptopals/Set2$ ./challenge_10.py 
#Decrypted Plaintext 1:
#CRYPTOPALS CHALLENGE 10
#
#Decrypted Plaintext 2:
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

