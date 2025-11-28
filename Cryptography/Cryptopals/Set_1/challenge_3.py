#!/usr/bin/python3

# Single Byte XOR

# The hex encoded string: 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.

import string
import json

def single_byte_xor(b_str1: bytes, b_str2: bytes) -> str:
    """
    XOR's each byte of a byte encoded string `b_str1`
    with byte string `b_str2`
    """
    x = ""
    for b in b_str1:
        x += (b ^ int.from_bytes(b_str2)).to_bytes(length=len(b_str2)).decode("utf-8")    
    
    return x

def find_key(hex_str: str) -> list:
    """ 
    Finds the single character key used to XOR encrypt
    a hex encoded string
    """
    decoded_strings = []
    chars = string.ascii_uppercase.encode("utf-8")
    for char in chars:
        decoded_strings.append(single_byte_xor(bytes.fromhex(hex_str), char.to_bytes() ))

    decoded_str_map = {k: {"length":0, "words":[]} for k in decoded_strings}
    with open("./words_dictionary.json") as wordlist:
        for w in json.load(wordlist):
            for s in decoded_str_map.keys():
                if w in s.lower():
                    decoded_str_map[s]["words"].append(w)
                    decoded_str_map[s]["length"] += 1
                    decoded_str_map[s]["key"] = chr(chars[decoded_strings.index(s)])
    
    return decoded_str_map


if __name__ == "__main__":
    string_to_xor = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    res = find_key(string_to_xor)
    xor_key = None
    count = 0
    message = ""
    for k in res:
        print(f"{k}: \tlength: {res[k]["length"]} \tkey: {res[k]["key"]}")
        if res[k]["length"] > count:
            count = res[k]["length"]
            xor_key = res[k]["key"]
            message = k

    print(f"\nDecrypted Message: {message}")
    print(f"XOR Key: {xor_key}")

# Expected output:
#Zvvrpw~9TZ>j9upr|9x9ivlw}9v9{xzvw: 	length: 17 	key: A
#Yuuqst}:WY=i:vsq:{:juot~:u|:x{yut: 	length: 19 	key: B
#Xttpru|;VX<h;wrp~;z;ktnu;t};yzxtu: 	length: 19 	key: C
#_sswur{<Q_;o<puwy<}<lsirx<sz<~}sr: 	length: 24 	key: D
#^rrvtsz=P^:n=qtvx=|=mrhsy=r{=|~rs: 	length: 20 	key: E
#]qquwpy>S]9m>rwu{>>nqkpz>qx>|}qp: 	length: 15 	key: F
#\pptvqx?R\8l?svtz?~?opjq{?py?}~|pq: 	length: 20 	key: G
#S{y~w0]S7c0|y{u0q0`e~t0v0rqs~: 	length: 11 	key: H
#R~~zxv1\R6b1}xzt1p1a~du1~w1spr~: 	length: 14 	key: I
#Q}}y{|u2_Q5a2~{yw2s2b}g|v2}t2psq}|: 	length: 13 	key: J
#P||xz}t3^P4`3zxv3r3c|f}w3|u3qrp|}: 	length: 12 	key: K
#W{{}zs4YW3g4x}q4u4d{azp4{r4vuw{z: 	length: 16 	key: L
#Vzz~|{r5XV2f5y|~p5t5ez`{q5zs5wtvz{: 	length: 15 	key: M
#Uyy}xq6[U1e6z}s6w6fycxr6yp6twuyx: 	length: 16 	key: N
#Txx|~yp7ZT0d7{~|r7v7gxbys7xq7uvtxy: 	length: 19 	key: O
#Kggcafo(EK/{(dacm(i(xg}fl(gn(jikgf: 	length: 27 	key: P
#Jffb`gn)DJ.z)e`bl)h)yf|gm)fo)khjfg: 	length: 22 	key: Q
#Ieeacdm*GI-y*fcao*k*zedn*el*hkied: 	length: 30 	key: R
#Hdd`bel+FH,x+gb`n+j+{d~eo+dm+ijhde: 	length: 21 	key: S
#Occgebk,AO+,`egi,m,|cybh,cj,nmocb: 	length: 27 	key: T
#Nbbfdcj-@N*~-adfh-l-}bxci-bk-olnbc: 	length: 23 	key: U
#Maaeg`i.CM)}.bgek.o.~a{`j.ah.loma`: 	length: 23 	key: V
#L``dfah/BL(|/cfdj/n/`zak/`i/mnl`a: 	length: 24 	key: W
#Cooking MC's like a pound of bacon: 	length: 44 	key: X
#Bnnjhof!LB&r!mhjd!`!qntoe!ng!c`bno: 	length: 28 	key: Y
#Ammikle"OA%q"nkig"c"rmwlf"md"`caml: 	length: 31 	key: Z
#
#Decrypted Message: Cooking MC's like a pound of bacon
#XOR Key: X
#
