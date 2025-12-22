# Offensive Security Notes

## Overview

### This repo is my playground for all things Offensive Security related. 

It contains:

- resources 
- writeups to challenges I've done 

Hopefully it will be helpful to someone searching for answers or examples of security topics in the same way I am.

## Topics

### [Web Security](./Web-Security/README.md)
### [Exploit Development](./Exploit-Dev/README.md)
### [MacOS](./MacOS/README.md)
### [Malware Development](./Mal-Dev/README.md)
### [Vulnerability Research](./VR/README.md)
### [Android](./Android)
### [Cryptography](./Cryptography/Cryptopals/Set_1/README.md)

## Challenges / Writeups

### Web

#### [Portswigger - Blind SQLi with conditional responses](./Web-Security/Writeups/Web-Security-Academy/Scripts/SQLi/blindSQLi_conditional_res.py)
#### [Portswigger - Blind SQLi with conditional errors](./Web-Security/Writeups/Web-Security-Academy/Scripts/SQLi/blindSQLi_conditional_errors.py)
#### [Portswigger - Blind SQLi with visible errors](./Web-Security/Writeups/Web-Security-Academy/Scripts/SQLi/blindSQLi_visible_errors.py)
#### [Portswigger - Blind SQLi with time delays](./Web-Security/Writeups/Web-Security-Academy/Scripts/SQLi/blindSQLi_time_delays.py)
#### [Portswigger - Blind SQLi with time delays (Data Exfiltration)](./Web-Security/Writeups/Web-Security-Academy/Scripts/SQLi/blindSQLi_time_delays_exploit.py)
#### [Portswigger - Blind SQLi with out-of-band interaction](./Web-Security/Writeups/Web-Security-Academy/Scripts/SQLi/blindSQLi_OOB.py)
#### [Portswigger - Blind SQLi with out-of-band interaction (Data Exfiltration)](./Web-Security/Writeups/Web-Security-Academy/Scripts/SQLi/blindSQLi_OOB_exploit.py)
#### [Portswigger - SQLi with filter bypass via XML encoding](./Web-Security/Writeups/Web-Security-Academy/Scripts/SQLi/SQLi_filter_bypass_xml.py)
#### [Portswigger - SQLi listing the database contents on Oracle and Non-Oracle databases](./Web-Security/Writeups/Web-Security-Academy/Scripts/SQLi/SQLi_examine_db.py)
#### [Portswigger - Broken brute force protection - IP block](./Web-Security/Writeups/Web-Security-Academy/Scripts/Authentication/Broken_bruteforce_protect_IP_block.py)
#### [Portswigger - Username Enumeration via response timing](./Web-Security/Writeups/Web-Security-Academy/Scripts/Authentication/Username_Enum_response_times.py)
#### [Portswigger - User Enumeration via response timing](./Web-Security/Writeups/Web-Security-Academy/Labs/Authentication/Username_Enum_via_response_times.md)
#### [JuiceShop - DOM-XSS](./Web-Security/Writeups/JuiceShop/Writeups/DOM-XSS.md)
#### [JuiceShop - SQL Injection](./Web-Security/Writeups/JuiceShop/Writeups/SQL_Injection.md)
#### [JuiceShop - Database Schema](./Web-Security/Writeups/JuiceShop/Writeups/Database_Schema.md)

### Exploit Dev

#### [Nightmare - Helithumper](./Exploit-Dev/CTF-Labs/Nightmare/Challenges/helithumper_re.md)
#### [Nightmare - Csaw19 Beleaf](./Exploit-Dev/CTF-Labs/Nightmare/Challenges/csaw19_beleaf.md)
#### [Nightmare - Pwn1](./Exploit-Dev/CTF-Labs/Nightmare/Challenges/pwn1.md)
#### [Nightmare - Just do it](./Exploit-Dev/CTF-Labs/Nightmare/Challenges/just_do_it.md)
#### [Nightmare - Boi](./Exploit-Dev/CTF-Labs/Nightmare/Challenges/csaw18_boi.md)
#### [Nightmare - Csaw16 Warmup](./Exploit-Dev/CTF-Labs/Nightmare/Challenges/csaw16_warmup.md)
#### [Nightmare - Csaw18 Get It](./Exploit-Dev/CTF-Labs/Nightmare/Challenges/csaw18_getit.md)
#### [Nightmare - Tuctf17 Vulnchat](./Exploit-Dev/CTF-Labs/Nightmare/Challenges/tuctf17_vulnchat.md)
#### [Nightmare - Csaw17 Pilot](./Exploit-Dev/CTF-Labs/Nightmare/Challenges/csaw17_pilot.md)
#### [Nightmare - Tamu19 Pwn3](./Exploit-Dev/CTF-Labs/Nightmare/Challenges/tamu19_pwn3.md)
#### [Nightmare - Tamu19 Shella Easy](./Exploit-Dev/CTF-Labs/Nightmare/Challenges/tu18_shellaeasy.md)
#### [Nightmare - Bkp16 Simple Calc](./Exploit-Dev/CTF-Labs/Nightmare/Challenges/bkp16_simplecalc.md)
#### [ROP Emporium - Ret2Win (32-bit)](./Exploit-Dev/CTF-Labs/ROP-Emporium/Challenges/ret2win.md)
#### [ROP Emporium - Ret2Win (64-bit)](./Exploit-Dev/CTF-Labs/ROP-Emporium/Challenges/ret2win64.md)
#### [ROP Emporium - Split32 (32-bit)](./Exploit-Dev/CTF-Labs/ROP-Emporium/Challenges/split32.md)
#### [ROP Emporium - Split64 (64-bit)](./Exploit-Dev/CTF-Labs/ROP-Emporium/Challenges/split64.md)
#### [ROP Emporium - Callme (32-bit)](./Exploit-Dev/CTF-Labs/ROP-Emporium/Challenges/callme32.md)
#### [ROP Emporium - Callme (64-bit)](./Exploit-Dev/CTF-Labs/ROP-Emporium/Challenges/callme64.md)
#### [ROP Emporium - Write4 (32-bit)](./Exploit-Dev/CTF-Labs/ROP-Emporium/Challenges/write432.md)
#### [ROP Emporium - Write4 (64-bit)](./Exploit-Dev/CTF-Labs/ROP-Emporium/Challenges/write464.md)
#### [ROP Emporium - Badchars (32-bit)](./Exploit-Dev/CTF-Labs/ROP-Emporium/Challenges/badchars32.md)
#### [ROP Emporium - Badchars (64-bit)](./Exploit-Dev/CTF-Labs/ROP-Emporium/Challenges/badchars64.md)
#### [ROP Emporium - Fluff (32-bit)](./Exploit-Dev/CTF-Labs/ROP-Emporium/Challenges/fluff32.md)
#### [ROP Emporium - Fluff (64-bit)](./Exploit-Dev/CTF-Labs/ROP-Emporium/Challenges/fluff64.md)
#### [ROP Emporium - Pivot (32-bit)](./Exploit-Dev/CTF-Labs/ROP-Emporium/Challenges/pivot32.md)
#### [ROP Emporium - Pivot (64-bit)](./Exploit-Dev/CTF-Labs/ROP-Emporium/Challenges/pivot64.md)
#### [ROP Emporium - Ret2Csu (64-bit)](./Exploit-Dev/CTF-Labs/ROP-Emporium/Challenges/ret2csu.md)

### Cryptography

### [Cryptopals - Convert hex to base64](./Cryptography/Cryptopals/Set_1/challenge_1.py)
### [Cryptopals - Fixed XOR](./Cryptography/Cryptopals/Set_1/challenge_2.py)
### [Cryptopals - Single-byte XOR cipher](./Cryptography/Cryptopals/Set_1/challenge_3.py)
### [Cryptopals - Detect single-character XOR](./Cryptography/Cryptopals/Set_1/challenge_4.py)
### [Cryptopals - Implement reapeating-key XOR](./Cryptography/Cryptopals/Set_1/challenge_5.py)
### [Cryptopals - Break repeating-key XOR](./Cryptography/Cryptopals/Set_1/challenge_6.py)
### [Cryptopals - AES in ECB mode](./Cryptography/Cryptopals/Set_1/challenge_7.py)
### [Cryptopals - Detect AES in ECB mode](./Cryptography/Cryptopals/Set_1/challenge_8.py)
### [Cryptopals - Implement PKCS#7 padding](./Cryptography/Cryptopals/Set_2/challenge_9.py)
### [Cryptopals - Implement CBC mode](./Cryptography/Cryptopals/Set_2/challenge_10.py)
### [Cryptopals - An ECB/CBC detection oracle](./Cryptography/Cryptopals/Set_2/challenge_11.py)


