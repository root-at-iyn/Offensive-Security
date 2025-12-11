#!/usr/bin/python3

# Implement CBC mode

# Implement CBC mode by hand by taking the ECB function you wrote earlier, 
# making it encrypt instead of decrypt (verify this by decrypting whatever you encrypt to test), 
# and using your XOR function from the previous exercise to combine them. 

# The file here is intelligible (somewhat) when CBC decrypted against 
# "YELLOW SUBMARINE" with an IV of all ASCII 0 (\x00\x00\x00 &c) 

import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

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
    return  plaintext + decryptor.finalize()
    

def encrypt_cbc_data(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    blocksize = 16
    pt = pkcs7(plaintext, blocksize) # padded plaintext
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
    print(f"Decrypted Plaintext 1: {decrypt_cbc_data(CT1, KEY, IV)}\n")
    print(f"Decrypted Plaintext 2:\n {decrypt_cbc_data(ENC_DATA, KEY, IV)}")


# Expected Output:

#root-at-iyn@Ubuntu-220403-x86-64:~/Cryptography/Cryptopals/Set2$ ./challenge_10.py
#Decrypted Plaintext 1: b'CRYPTOPALS CHALLENGE 10\n\x08\x08\x08\x08\x08\x08\x08\x08'
#
#Decrypted Plaintext 2:
# b"I'm back and I'm ringin' the bell \nA rockin' on the mike while the fly girls yell \nIn ecstasy in the back of me \nWell that's my DJ Deshay cuttin' all them Z's \nHittin' hard and the girlies goin' crazy \nVanilla's on the mike, man I'm not lazy. \n\nI'm lettin' my drug kick in \nIt controls my mouth and I begin \nTo just let it flow, let my concepts go \nMy posse's to the side yellin', Go Vanilla Go! \n\nSmooth 'cause that's the way I will be \nAnd if you don't give a damn, then \nWhy you starin' at me \nSo get off 'cause I control the stage \nThere's no dissin' allowed \nI'm in my own phase \nThe girlies sa y they love me and that is ok \nAnd I can dance better than any kid n' play \n\nStage 2 -- Yea the one ya' wanna listen to \nIt's off my head so let the beat play through \nSo I can funk it up and make it sound good \n1-2-3 Yo -- Knock on some wood \nFor good luck, I like my rhymes atrocious \nSupercalafragilisticexpialidocious \nI'm an effect and that you can bet \nI can take a fly girl and make her wet. \n\nI'm like Samson -- Samson to Delilah \nThere's no denyin', You can try to hang \nBut you'll keep tryin' to get my style \nOver and over, practice makes perfect \nBut not if you're a loafer. \n\nYou'll get nowhere, no place, no time, no girls \nSoon -- Oh my God, homebody, you probably eat \nSpaghetti with a spoon! Come on and say it! \n\nVIP. Vanilla Ice yep, yep, I'm comin' hard like a rhino \nIntoxicating so you stagger like a wino \nSo punks stop trying and girl stop cryin' \nVanilla Ice is sellin' and you people are buyin' \n'Cause why the freaks are jockin' like Crazy Glue \nMovin' and groovin' trying to sing along \nAll through the ghetto groovin' this here song \nNow you're amazed by the VIP posse. \n\nSteppin' so hard like a German Nazi \nStartled by the bases hittin' ground \nThere's no trippin' on mine, I'm just gettin' down \nSparkamatic, I'm hangin' tight like a fanatic \nYou trapped me once and I thought that \nYou might have it \nSo step down and lend me your ear \n'89 in my time! You, '90 is my year. \n\nYou're weakenin' fast, YO! and I can tell it \nYour body's gettin' hot, so, so I can smell it \nSo don't be mad and don't be sad \n'Cause the lyrics belong to ICE, You can call me Dad \nYou're pitchin' a fit, so step back and endure \nLet the witch doctor, Ice, do the dance to cure \nSo come up close and don't be square \nYou wanna battle me -- Anytime, anywhere \n\nYou thought that I was weak, Boy, you're dead wrong \nSo come on, everybody and sing this song \n\nSay -- Play that funky music Say, go white boy, go white boy go \nplay that funky music Go white boy, go white boy, go \nLay down and boogie and play that funky music till you die. \n\nPlay that funky music Come on, Come on, let me hear \nPlay that funky music white boy you say it, say it \nPlay that funky music A little louder now \nPlay that funky music, white boy Come on, Come on, Come on \nPlay that funky music \n\x04\x04\x04\x04"

