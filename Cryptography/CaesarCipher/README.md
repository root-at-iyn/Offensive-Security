# The Caesar Cipher

## Intro

The caeser cipher is often taught as an introductionary point to cryptography. It has no practical use today but it's flaws point out some interesting principles in cryptography that we need to be aware of:

- Key Size 
- Block Size
- Preserved Structure
- Brute-Force Attacks

The caesar cipher is attributed to Roman emporer Julius Caesar, which makes it over 2000 years old. It is a simple algorithm where messages are encoded by substituting each character in the message with another character. The character is shifted from it's position in the alphabet to a fixed numerical distance. In this case, the distance becomes the key to encrypting and decrypting the message. For example, if we had a message with the text `apple` and substitution shift of `3`, the encoded message would become `dssoh`:

|Letter|Shift 1| Shift 2|Shift 3|
|------|-------|--------|-------|
|a     |b      |c       |`d`    |
|p     |q      |r       |`s`    |  
|p     |q      |r       |`s`    | 
|l     |m      |n       |`o`    |
|e     |f      |g       |`h`    |


There are some problems with this approach in the age of modern computing: 

1. Since we are just shifting the character by `n`, we are limited to choosing a key within the length of the alphabet. This makes the key space 26 for just lowercase letters, 42 for lower and uppercase, 52 if we include digits 0 - 9, and 62 if we also include punctuation chararacters. Obviously this is a small key space which makes it easier to brute force.
2. When we encode a word there is no padding to make the encoded block a fixed size. If the blocks lengths vary in size, it could help is deduce what they may be (word or phrase patterns).

## Example Implementation

This example is taken from Practical Cryptography in Python, exercise 1.1 - 1.2. In the example below I've created a version of the caeaser cipher which has an alpahbet of only uppercase letters. If there are other characters outside of this alphabet then I do not substitute them. Any lowercase letters will be converted to uppercase and the output returned is in upper case.


*ShiftCipherEncoder.py*
```python
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
    return "".join(ciphertext).replace(" ", "") 
    # use replace to remove any spaces between words


def decode(shift, ciphertext):
    shift_map = shift_char(shift)
    message = [
            # convert shift_map to list to use the index method
            # so we can find the key that maps to the value
            list(shift_map)[list(shift_map.values()).index(x)]
            if x in shift_map.values() else x for x in ciphertext
            ]
    return "".join(message)

```

If I run the program with a shift of `7` and a message of `YOU WILL NEVER FIND ME` we get the following:

```bash
$ ./ShiftCipherEncoder.py encrypt --shift 7 --message "YOU WILL NEVER FIND ME"
FVBDPSSULCLYMPUKTL
```

## Brute-force Attack

We get the encoded output `FVBDPSSULCLYMPUKTL` which ommits spaces, but even without spaces we can easily derive the source input. We can start by trying different keys in the range of 0 - 25 (which is the full key space for this alphabet). Next, we review the result of each shift to see if there are any recognisible English words. We can automate finding the whether the words are english by checking a dictionary wordlist, and counting how many english words appear in the encoded text. We will presume the shift that produces the highest number of english words will be the correct encoded output. To demonstrate this I have written the python script below:

*DecodeShiftCipher.py*
```python
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
```

The script utilises the decode function from the *ShiftCipherEncoder.py* file to save duplication. It gets the alphabet length from `shift_char` function and iterates through the keys to get the length of that alphabet. For each iteration it runs the `decode` function and saves the output to a list. The `find_possible_words` function takes in the dictionary wordlist and the list of variants of the decoded message (decoded_list). It will iterate over every word in the wordlist and for each decoded_list item it will check if that word is a substring in that word. The map is created for each decoded_list item as the `key` and the list of found words as the `value`. Finally, the `decoded_message` function takes map as input and calculates which decoded message has the highest number of words that were found.


When we run the script on the commandline after adding python argparse library to make it a cli tool, we can see the output of all the decoded_list items, the words that were found for each one, and the selected decoded_list item that was chosen as being the correct plaintext.


```bash
$ ./DecodeShiftCipher.py --message FVBDPSSULCLYMPUKTL --debug 2

Listing all decoded message variants and matched words:
FVBDPSSULCLYMPUKTL: ['b', 'bd', 'c', 'cl', 'cly', 'd', 'dp', 'f', 'fv', 'y', 'ym', 'k', 'kt', 'l', 'lc', 'ly', 'lym', 'm', 'mp', 'p', 'ps', 'pu', 's', 'ss', 'ssu', 'su', 't', 'u', 'v', 'vb']

EUACORRTKBKXLOTJSK: ['a', 'ac', 'acor', 'b', 'bk', 'c', 'co', 'cor', 'corr', 'e', 'eu', 'j', 'js', 'k', 'kb', 'l', 'lo', 'lot', 'o', 'or', 'ot', 'r', 'rt', 's', 'sk', 't', 'tk', 'u', 'x']

DTZBNQQSJAJWKNSIRJ: ['a', 'b', 'bn', 'd', 'dt', 'i', 'ir', 'j', 'ja', 'k', 'kn', 'n', 'ns', 'q', 'qs', 'r', 's', 'si', 'sir', 't', 'w', 'wk', 'z']

CSYAMPPRIZIVJMRHQI: ['a', 'am', 'amp', 'c', 'cs', 'h', 'hq', 'i', 'y', 'ya', 'yam', 'yamp', 'iv', 'j', 'm', 'mp', 'mr', 'p', 'pp', 'ppr', 'pr', 'q', 'r', 'rh', 's', 'v', 'z']

BRXZLOOQHYHUILQGPH: ['b', 'br', 'g', 'gp', 'gph', 'h', 'hy', 'hu', 'hui', 'i', 'y', 'il', 'l', 'lo', 'loo', 'o', 'p', 'ph', 'q', 'qh', 'r', 'u', 'ui', 'x', 'z']

AQWYKNNPGXGTHKPFOG: ['a', 'aq', 'f', 'fo', 'fog', 'g', 'gt', 'h', 'y', 'k', 'kn', 'n', 'np', 'o', 'og', 'p', 'pf', 'pg', 'q', 't', 'th', 'w', 'wy', 'x']

ZPVXJMMOFWFSGJOENF: ['e', 'en', 'f', 'fs', 'fw', 'g', 'j', 'jo', 'joe', 'm', 'mm', 'mo', 'n', 'o', 'oe', 'of', 'p', 's', 'sg', 'v', 'w', 'wf', 'x', 'z']

YOUWILLNEVERFINDME: ['d', 'dm', 'e', 'er', 'erf', 'eve', 'ever', 'f', 'fi', 'fin', 'find', 'i', 'y', 'il', 'ill', 'in', 'ind', 'yo', 'you', 'l', 'll', 'ln', 'm', 'me', 'n', 'nd', 'ne', 'neve', 'never', 'o', 'r', 'rf', 'u', 'v', 'ver', 'w', 'wi', 'will']

XNTVHKKMDUDQEHMCLD: ['c', 'cl', 'd', 'du', 'dud', 'e', 'eh', 'h', 'hm', 'k', 'km', 'l', 'ld', 'm', 'mc', 'md', 'n', 'nt', 'q', 'qe', 't', 'tv', 'u', 'ud', 'v', 'x']

WMSUGJJLCTCPDGLBKC: ['b', 'bk', 'c', 'cp', 'cpd', 'ct', 'd', 'dg', 'g', 'gl', 'glb', 'j', 'k', 'kc', 'l', 'lb', 'lc', 'm', 'ms', 'p', 'pd', 's', 'su', 't', 'tc', 'u', 'ug', 'w', 'wm']

VLRTFIIKBSBOCFKAJB: ['a', 'b', 'bo', 'boc', 'bs', 'c', 'cf', 'f', 'fi', 'i', 'ii', 'ik', 'j', 'k', 'ka', 'kaj', 'kb', 'l', 'lr', 'o', 'oc', 'r', 'rt', 's', 'sb', 't', 'v', 'vl']

UKQSEHHJARANBEJZIA: ['a', 'an', 'ar', 'ara', 'b', 'be', 'e', 'eh', 'h', 'i', 'ia', 'j', 'ja', 'jar', 'jara', 'k', 'n', 'nb', 'q', 'qs', 'r', 'ra', 'ran', 's', 'se', 'u', 'z']

TJPRDGGIZQZMADIYHZ: ['a', 'ad', 'd', 'dg', 'di', 'g', 'gi', 'h', 'i', 'y', 'j', 'm', 'ma', 'mad', 'madi', 'p', 'pr', 'q', 'r', 'rd', 't', 'z']

SIOQCFFHYPYLZCHXGY: ['c', 'cf', 'ch', 'f', 'ff', 'g', 'h', 'hy', 'hyp', 'i', 'y', 'io', 'l', 'o', 'p', 'q', 's', 'si', 'x', 'z']

RHNPBEEGXOXKYBGWFX: ['b', 'be', 'bee', 'bg', 'e', 'ee', 'eg', 'f', 'g', 'h', 'y', 'k', 'ky', 'n', 'np', 'o', 'ox', 'p', 'r', 'rh', 'w', 'wf', 'x']

QGMOADDFWNWJXAFVEW: ['a', 'ad', 'add', 'af', 'd', 'dd', 'e', 'ew', 'f', 'fv', 'fw', 'g', 'gm', 'j', 'm', 'mo', 'moa', 'n', 'o', 'oad', 'q', 'v', 'w', 'x']

PFLNZCCEVMVIWZEUDV: ['c', 'cc', 'ce', 'd', 'e', 'eu', 'f', 'fl', 'i', 'iw', 'l', 'ln', 'm', 'mv', 'n', 'p', 'pf', 'u', 'ud', 'v', 'vi', 'w', 'z']

OEKMYBBDULUHVYDTCU: ['b', 'bb', 'bd', 'c', 'cu', 'd', 'dt', 'du', 'e', 'h', 'hv', 'hvy', 'y', 'yd', 'k', 'km', 'l', 'lu', 'm', 'my', 'o', 'oe', 't', 'tc', 'u', 'uh', 'ulu', 'v']

NDJLXAACTKTGUXCSBT: ['a', 'aa', 'ac', 'act', 'b', 'bt', 'c', 'cs', 'ct', 'd', 'dj', 'g', 'gu', 'j', 'k', 'kt', 'l', 'lx', 'n', 'nd', 's', 'sb', 't', 'tg', 'tk', 'tkt', 'u', 'ux', 'x', 'xc']

MCIKWZZBSJSFTWBRAS: ['a', 'as', 'b', 'br', 'bra', 'bras', 'bs', 'c', 'f', 'ft', 'i', 'ik', 'j', 'js', 'k', 'kw', 'm', 'mc', 'r', 'ra', 'ras', 's', 'sf', 't', 'w', 'wb', 'z']

LBHJVYYARIRESVAQZR: ['a', 'aq', 'ar', 'b', 'e', 'es', 'h', 'i', 'y', 'ya', 'yar', 'ir', 'ire', 'ires', 'j', 'l', 'lb', 'q', 'r', 're', 'res', 's', 'sv', 'v', 'va', 'z']

KAGIUXXZQHQDRUZPYQ: ['a', 'ag', 'd', 'dr', 'g', 'gi', 'h', 'hq', 'i', 'y', 'k', 'ka', 'p', 'q', 'qh', 'r', 'u', 'ux', 'x', 'xx', 'z']

JZFHTWWYPGPCQTYOXP: ['c', 'cq', 'f', 'g', 'gp', 'h', 'ht', 'y', 'yo', 'yox', 'j', 'o', 'ox', 'p', 'pc', 'pg', 'q', 'qt', 'qty', 't', 'w', 'wy', 'x', 'z']

IYEGSVVXOFOBPSXNWO: ['b', 'bp', 'bps', 'e', 'eg', 'f', 'fo', 'fob', 'g', 'gs', 'i', 'y', 'ye', 'n', 'o', 'ob', 'of', 'ofo', 'p', 'ps', 's', 'sv', 'v', 'vv', 'w', 'wo', 'x']

HXDFRUUWNENAORWMVN: ['a', 'ao', 'aor', 'd', 'e', 'en', 'f', 'fr', 'h', 'm', 'mv', 'n', 'na', 'ne', 'o', 'or', 'r', 'u', 'v', 'w', 'wm', 'x', 'xd']

GWCEQTTVMDMZNQVLUM: ['c', 'ce', 'd', 'dm', 'e', 'eq', 'g', 'l', 'lu', 'lum', 'm', 'md', 'n', 'q', 'qt', 'qv', 't', 'tv', 'u', 'um', 'v', 'vl', 'w', 'wc', 'z', 'zn']


Decoded message: YOUWILLNEVERFINDME
```

This is a simple example for demonstration purposes. We could have added all printable characters to increase the key space to a length of `100`, but this does not solve the padding issues, or the fact we can still use a dictionary to brute force the message. Excercise 1.3 of the same book also suggests increasing the difficulty by randomly jumbling the letters of the alphabet instead of just shifting them. To do this, you would have create a permuation of all the characters in the chosen alphabet, i.e (the factorial `!n`). Once you have this list you can use python's `random.randint()` in the range of the key space `!n`. This would select the alphabet to encrypt the message with. Obviously the larger the alphabet size the longer is would take to bruteforce the message due to the number of keys you would have to try, but still this is not unbreakble, just slower. For example, the factorial of size of only uppercase letters is:

```bash
$ python3 -c "import math; print(math.factorial(26))"
403291461126605635584000000
```
So if the random number chosen is closer to the latter half of that range it will take longer, but its also possible a random integer could be chosen closer to the beginning of the range. Even if we set the key space to start from half way through the range, if an attacker is aware of this you have essentially halved the amount of effort required to crack the message. If you know what function is being used to pick a random number, you can generate a large sample size and see if there are any patterns within a set range of the key space where numbers a likely to be chosen.
