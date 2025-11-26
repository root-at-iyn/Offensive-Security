#!/usr/bin/python3

import json
import argparse
from ShiftCipherEncoder import shift_char, encode, decode

# word list
# https://github.com/dwyl/english-words/blob/master/words_dictionary.json

def wordlist(path):
    try:
        with open(path,"r") as fp:
            wordlist_dict = json.load(fp)
        return list(wordlist_dict)
    except OSError as e:
        return e.strerror 

def get_decoded_list(message):
    decoded_list = [decode(x, message) for x in range(len(shift_char(0).keys()))]
    return decoded_list 

def find_possible_words(decoded_list, word_list):
    decoded_msg_words = {x:[] for x in decoded_list}
    for w in word_list:
        for d in decoded_msg_words.keys():
            if w.upper() in d:
                decoded_msg_words[d].append(w)
    return decoded_msg_words 

def decode_message(decoded_msg_w_dict):
    most_words = 0
    msg = ""
    for x in decoded_msg_w_dict.keys():
        if len(decoded_msg_w_dict[x]) > most_words: 
            most_words = len(decoded_msg_w_dict[x])
            msg = x
    return msg

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--message", required=True, help="message to decrypt")
    parser.add_argument("--debug", choices=["1","2"], help="debug level for decoder")
    parser.add_argument("--wordlist", help="dictionary wordlist to check", default="./words_dictionary.json")
    args = parser.parse_args()


    dmw_dict =  find_possible_words(get_decoded_list(args.message),wordlist(args.wordlist))
    if args.debug == "1":
        print("\nListing all decoded message variants:")
        for d in dmw_dict.keys():
            print(d)
        print("\n")
    elif args.debug == "2":
        print("\nListing all decoded message variants and matched words:")
        for k,v in dmw_dict.items():
            print(f"{k}: {v}")
            print("\n")
        print("\n\n")

    print(f"Decoded message: {decode_message(dmw_dict)}")

    



    
